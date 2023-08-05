# Copyright 2023 Viktor Krückl. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================


# tensorflow imports
from ._mapping import _Mapping
import numpy as _np
import tensorflow as _tf
import tensorflow_probability as _tfp
from tensorflow.keras.constraints import NonNeg as _NonNeg
from tensorflow.keras.constraints import MinMaxNorm as _MinMaxNorm
from mixturemapping.distributions import createCovMatrix as _createCovMatrix
_tfd = _tfp.distributions


class _GMRmapping(_Mapping):

    def invert_indices(self, indices):
        n_features = self.model_m.shape[3]
        inv = _np.ones(n_features, dtype=bool)
        inv[indices] = False
        inv, = _np.where(inv)
        return inv


    def _to_np(self, a):
        if isinstance(a, _np.ndarray):
            return a
        else:
            return _np.array(a, dtype=self.dtype)

    def __init__(self, output_indices, n_components=None, **kwargs):
        self.output_indices = output_indices
        
        self.output_dim = len(self.output_indices)       
        self.n_components = n_components

        super(_GMRmapping, self).__init__(len(output_indices), **kwargs)

    def _update_matrices(self):

        self.input_indices = self.invert_indices(self.output_indices)

        self.s11 = _tf.gather(_tf.gather(self.model_cov, self.input_indices, axis=3), self.input_indices, axis=4)
        self.s22 = _tf.gather(_tf.gather(self.model_cov, self.output_indices, axis=3), self.output_indices, axis=4)

        self.s11I = _tf.linalg.pinv(self.s11)
        self.s21 = _tf.gather(_tf.gather(
            self.model_cov, self.output_indices, axis=3), self.input_indices, axis=4)
        self.s12 = _tf.linalg.matrix_transpose(self.s21)

        self.mu1 = _tf.gather(self.model_m, self.input_indices, axis=3)
        self.mu2 = _tf.gather(self.model_m, self.output_indices, axis=3)

        self.p = _tfd.MultivariateNormalTriL(
            loc=self.mu1,
            scale_tril=_tf.linalg.cholesky(self.s11)
        )

        self.model_mix_dim = _tf.shape(self.mu1)[1]
        
        self._update_matrices = True


    def call(self, x, **kwargs):
        """Compute the output distribution layer based on `x` (dict of `tf.Tensors`)

        Parameters:
            means: Instance of `tf.Tensor`
                Means `tf.Tensor` of the input mixture distribution
                shape: [batch, mix, inDim]
            stdDevs: Instance of `tf.Tensor`
                Std Deviation `tf.Tensor` of the input mixture distribution
                shape: [batch, mix, inDim]
            covariances : Instance of `tf.Tensor`
                Cov Matrix Tensor of the input mixture distribution
                shape: [batch, mix, inDim, inDim]
            weights: Instance of `tf.Tensor`
                Weight `tf.Tensor` ot the mixture components
                shape: [batch, mix]

        Returns:
            means: Instance of `tf.Tensor`
                Means `tf.Tensor` of the output mixture distribution
                shape: [batch, mix, outDim]
            covariances: Instance of `tf.Tensor`
                Covariance matrix `tf.Tensor` of the output mixture distribution
                shape: [batch, mix, outDim, outDim]
            weights: Instance of `tf.Tensor`
                Weight `tf.Tensor` ot the mixture components
                shape: [batch, mix]
        """


        means = x["means"]
        covariances = x["covariances"]
        weights = x["weights"]

        # TODO implement stdDevs case


        shape = _tf.shape(means)
        batch_dim = shape[0]
        input_mix_dim = shape[1]

        m = _tf.expand_dims(means, 1)
        cov = _tf.expand_dims(covariances, 1)
        w = _tf.expand_dims(weights, 1)

        out_m = self.mu2 + _tf.linalg.matmul(
            _tf.linalg.matmul(self.s21, self.s11I),
            _tf.expand_dims((m - self.mu1), 4)
        )[:, :, :, :, 0]

        sigma_addon = _tf.linalg.matmul(_tf.linalg.matmul(_tf.linalg.matmul(
            _tf.linalg.matmul(self.s21, self.s11I),
            cov),
            self.s11I), self.s12)

        out_cov = self.s22 - \
            _tf.matmul(_tf.matmul(self.s21, self.s11I), self.s12) + sigma_addon

        prop = self.model_w * self.p.prob(m)

        total_prop = _tf.reduce_sum(prop, axis=1, keepdims=True)
        prop = prop/total_prop
        prop *= w

        out_m = _tf.reshape(
            out_m, shape=[batch_dim, input_mix_dim*self.model_mix_dim, self.output_dim])
        out_cov = _tf.reshape(out_cov, shape=[
                              batch_dim, input_mix_dim*self.model_mix_dim, self.output_dim, self.output_dim])
        out_w = _tf.reshape(
            prop, shape=[batch_dim, input_mix_dim*self.model_mix_dim])

        if self.n_components:
            k = _tf.minimum(self.n_components,
                            input_mix_dim*self.model_mix_dim)
            topk = _tf.math.top_k(out_w, k=k)

            out_w = topk.values
            total_prop = _tf.reduce_sum(out_w, axis=1, keepdims=True)
            out_w = out_w/total_prop

            out_m = _tf.gather(out_m, topk.indices, axis=1, batch_dims=1)
            out_cov = _tf.gather(out_cov, topk.indices, axis=1, batch_dims=1)

        return {
            "means": out_m,
            "covariances": out_cov,
            "weights": out_w

        }

    @property
    def means_(self):
        return _tf.keras.backend.eval(self.model_m)[0, :, 0, :]

    @property
    def covariances_(self):
        return _tf.keras.backend.eval(self.model_cov)[0, :, 0, :, :]   

    @property
    def weights_(self):
        return _tf.keras.backend.eval(self.model_w)[0, :, 0]

    def get_config(self):
        config = super().get_config().copy()
        config.update({
            'output_indices': list(self.output_indices),
            'means': self.means_.tolist(),
            'covariances': self.covariances_.tolist(),
            'weights': self.weights_.tolist(),
            'n_components': self.n_components
        })
        return config        

class ConstGMR(_GMRmapping):
    """ A constant mapping layer using gaussian mixtures.

    This layers can be used if a trained Gaussian mixture of the combined input and output coordinates are available.


    Example::

        import mixturemapping as mm
        from sklearn.mixture import GaussianMixture

        baseModel = GaussianMixture(n_components=50)
        baseModel.fit(combinedSamples)

        gmr = mm.layers.ConstGMR(
            output_indices=[2, 3],
            means=baseModel.means_,
            covariances=baseModel.covariances_,
            weights=baseModel.weights_,
        )


    Parameters
    ----------
    output_indices : array 
        Array of the indices in the following distribution, which will server as output
    means : numpy array 
        Means array of the combined mixture distribution
        shape: [mix, inDim]
    covariances : numpy array 
        Covariances array of the combined mixture distribution
        shape: [mix, inDim, inDim]    
    weights : numpy array 
        Weights array of the combined mixture distribution
        shape: [mix]                    
        

    Returns
    -------
    {
        "means" : Tensorflow Tensor
            Centers of the mixture distributions
        "covariances" : Tensorflow Tensor
            Covariance matrices of the distributions
        "weights" : Tensorflow Tensor
            Weights of the mixture components
    }
    """
    def __init__(self, output_indices, means, covariances, weights, n_components=None, **kwargs):
        super(ConstGMR, self).__init__(output_indices, n_components, **kwargs)

        self.set_gmm(self._to_np(means), self._to_np(covariances), self._to_np(weights))
        self._update_matrices()

    def set_gmm(self, means, covariances, weights):
        """ Set the initial GMM parameters
        
        Parameters
        ----------
        means : numpy array 
            Means array of the combined mixture distribution
            shape: [mix, inDim]
        covariances : numpy array 
            Covariances array of the combined mixture distribution
            shape: [mix, inDim, inDim]    
        weights : numpy array 
            Weights array of the combined mixture distribution
            shape: [mix]           
        """
        self.model_m = _tf.expand_dims(_tf.expand_dims(means, 0), 2)
        self.model_cov = _tf.expand_dims(_tf.expand_dims(covariances, 0), 2)
        self.model_w = _tf.expand_dims(_tf.expand_dims(weights, 0), 2)


class DynamicGMR(_GMRmapping):
    """ A constant mapping layer using gaussian mixtures.

    This layers can be used if a trained Gaussian mixture of the combined input and output coordinates is available.
    In a further step the model can be also trained on samples.


    Example::

        import mixturemapping as mm
        from sklearn.mixture import GaussianMixture

        baseModel = GaussianMixture(n_components=50)
        baseModel.fit(combinedSamples)

        gmr = mm.layers.DynamicGMR(
            output_indices=[2, 3],
            means=baseModel.means_,
            covariances=baseModel.covariances_,
            weights=baseModel.weights_,
        )

        transformedDist = gmr({"means": inMeans, "covariances": cov, "weights": inWeight})

        distLayer = mm.layers.Distribution(dtype=dataType, regularize_cov_epsilon=0.95)
        dist = distLayer(transformedDist)

        sample_loss = distLayer.sample_loss(inTsamples)  


    Parameters
    ----------
    output_indices : array 
        Array of the indices in the following distribution, which will server as output
    means : numpy array 
        Means array of the combined mixture distribution
        shape: [mix, inDim]
    covariances : numpy array 
        Covariances array of the combined mixture distribution
        shape: [mix, inDim, inDim]    
    weights : numpy array 
        Weights array of the combined mixture distribution
        shape: [mix]                    
        

    Returns
    -------
    {
        "means" : Tensorflow Tensor
            Centers of the mixture distributions
        "covariances" : Tensorflow Tensor
            Covariance matrices of the distributions
        "weights" : Tensorflow Tensor
            Weights of the mixture components
    }
    """
    def __init__(self, output_indices, means, covariances, weights, n_components=None, **kwargs):
        super(DynamicGMR, self).__init__(output_indices, n_components, **kwargs)

        self.set_gmm(self._to_np(means), self._to_np(covariances), self._to_np(weights))
        self._update_matrices()


    def set_gmm(self, means, covariances, weights):
        """ Set the initial GMM parameters
        
        Parameters
        ----------
        means : numpy array 
            Means array of the combined mixture distribution
            shape: [mix, inDim]
        covariances : numpy array 
            Covariances array of the combined mixture distribution
            shape: [mix, inDim, inDim]    
        weights : numpy array 
            Weights array of the combined mixture distribution
            shape: [mix]           
        """
        # extract sizes
        self._mix_size = means.shape[0]
        self._var_size = means.shape[1]
        self._corr_size = int(self._var_size * (self._var_size-1) / 2)

        self.input_indices = [i for i in range(self._var_size) if i not in self.output_indices]


        # transform inputs into the right shape
        input_spread = _np.array([_np.sqrt(_np.diagonal(m)) for m in covariances ])
        input_corr = covariances / _np.reshape(input_spread, [self._mix_size, 1, self._var_size]) / _np.reshape(input_spread, [self._mix_size, self._var_size, 1])
        triu_indices = _np.triu_indices(5, 1)
        input_corr = input_corr[:, triu_indices[0], triu_indices[1]]
        
        const_input_corr_idx = [idx for idx, (x, y) in enumerate(_np.transpose(triu_indices)) if x in self.input_indices and y in self.input_indices]
        var_input_corr_idx = [idx for idx in range(self._corr_size) if idx not in const_input_corr_idx]

        # create the trainable means
        self._tf_means_var = self.add_weight(
            name='mean_var',
            shape=(self._mix_size, len(self.output_indices)),
            initializer='uniform',
            trainable=True            
        )
        self._tf_means_const = _tf.constant(
            means[:, self.input_indices],
            name='means_const'
        )
        # join the trainable and constant parts together
        self._tf_means = _tf.transpose([
            self._tf_means_var[:, self.output_indices.index(i)] if i in self.output_indices else self._tf_means_const[:, self.input_indices.index(i)]
            for i in range(self._var_size)
        ], name="means" )

        # create the trainable standard deviations
        self._tf_spread_var_log = self.add_weight(
            name='spread_var_log',
            shape=(self._mix_size, len(self.output_indices)),
            initializer='uniform',
            trainable=True
        )
        self._tf_spread_var = _tf.exp(self._tf_spread_var_log, name="spread_var")

        # create the constant parts
        self._tf_spread_const = _tf.constant(
            input_spread[:, self.input_indices],
            name='spread_const'
        )

        # join the trainable and constant parts together
        self._tf_spread = _tf.transpose([
            self._tf_spread_var[:, self.output_indices.index(i)] if i in self.output_indices else self._tf_spread_const[:, self.input_indices.index(i)]
            for i in range(self._var_size)
        ], name="spread" )


        # create the trainable part of the correlation
        self._tf_corr_var_atanh = self.add_weight(
            name='corr_var',
            shape=(self._mix_size, len(var_input_corr_idx)),
            initializer='uniform',
            trainable=True
        )
        self._tf_corr_var = _tf.tanh(self._tf_corr_var_atanh, name="corr_var")
        self._tf_corr_const = _tf.constant(
            input_corr[:, const_input_corr_idx],
            name='corr_const'
        )
        # join the trainable and constant parts together
        self._tf_corr = _tf.transpose([
            self._tf_corr_var[:, var_input_corr_idx.index(i)] if i in var_input_corr_idx else self._tf_corr_const[:, const_input_corr_idx.index(i)]
            for i in range(self._corr_size)
        ], name="spread" )        

        # create the constant part of the correlation

        # compute the full [var_size x var_size] matrix from the stdDev tensor
        baseCovMatrix = _tf.matmul(_tf.reshape(self._tf_spread, [self._mix_size, self._var_size, 1], name="colVec"),
                                   _tf.reshape(self._tf_spread, [self._mix_size, 1, self._var_size], name="rowVec"),
                                   name="baseCovMatrix")

        # offset matrix used to compute the index of the correlationTensor entry for the final matrix
        step = self._var_size-1
        offset = [-1]
        for i in range(self._var_size-1):
            step = step - 1
            offset.append(offset[-1] + step)

        # apply the correlation
        with _tf.name_scope("TransposedCorrelation"):
            output = [[baseCovMatrix[:, x, y] if x == y else
                       baseCovMatrix[:, x, y] * self._tf_corr[:, y + offset[x]] if x < y else
                       baseCovMatrix[:, x, y] * self._tf_corr[:, x + offset[y]]
                       for x in range(self._var_size)] for y in range(self._var_size)]
        self._tf_covariances = _tf.transpose(output, name="TransposeBack")


        # create the trainable part of the correlation
        self._tf_weights_raw = self.add_weight(
            name='weights_raw',
            shape=(self._mix_size,),
            initializer='uniform',
            trainable=True,
        ) 
        weights_comp = _tf.abs(self._tf_weights_raw)
        weights_total = _tf.reduce_sum(weights_comp)
        self._tf_weights = weights_comp / weights_total
        

        # set the trainable variable parts
        _tf.keras.backend.set_value(self._tf_spread_var_log, _np.log(input_spread[:, self.output_indices]))
        _tf.keras.backend.set_value(self._tf_means_var, means[:, self.output_indices])
        _tf.keras.backend.set_value(self._tf_corr_var_atanh, _np.arctanh(input_corr[:, var_input_corr_idx]))
        _tf.keras.backend.set_value(self._tf_weights_raw, weights)


        self.model_m = _tf.expand_dims(_tf.expand_dims(self._tf_means, 0), 2)
        self.model_cov = _tf.expand_dims(_tf.expand_dims(self._tf_covariances, 0), 2)
        self.model_w = _tf.expand_dims(_tf.expand_dims(self._tf_weights, 0), 2)


    def set_gmm_values(self, means, covariances, weights):
        """ Set the GMM parameters without creating new tensorflow operations
        
        Parameters
        ----------
        means : numpy array 
            Means array of the combined mixture distribution
            shape: [mix, inDim]
        covariances : numpy array 
            Covariances array of the combined mixture distribution
            shape: [mix, inDim, inDim]    
        weights : numpy array 
            Weights array of the combined mixture distribution
            shape: [mix]           
        """        


        # transform inputs into the right shape
        input_spread = _np.array([_np.sqrt(_np.diagonal(m)) for m in covariances ])
        input_corr = covariances / _np.reshape(input_spread, [self._mix_size, 1, self._var_size]) / _np.reshape(input_spread, [self._mix_size, self._var_size, 1])
        triu_indices = _np.triu_indices(5, 1)
        input_corr = input_corr[:, triu_indices[0], triu_indices[1]]
        
        const_input_corr_idx = [idx for idx, (x, y) in enumerate(_np.transpose(triu_indices)) if x in self._input_indices and y in self._input_indices]
        var_input_corr_idx = [idx for idx in range(self._corr_size) if idx not in const_input_corr_idx]

        # set the trainable variable parts
        _tf.keras.backend.set_value(self._tf_spread_var_log, _np.log(input_spread[:, self.output_indices]))
        _tf.keras.backend.set_value(self._tf_means_var, means[:, self.output_indices])
        _tf.keras.backend.set_value(self._tf_corr_var_atanh, _np.arctanh(input_corr[:, var_input_corr_idx]))
        _tf.keras.backend.set_value(self._tf_weights_raw, weights)

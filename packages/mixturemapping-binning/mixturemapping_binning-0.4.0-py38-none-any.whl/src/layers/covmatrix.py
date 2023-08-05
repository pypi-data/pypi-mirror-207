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
import tensorflow as _tf
import tensorflow_probability as _tfp
from tensorflow.keras.layers import Layer as _Layer
from tensorflow.keras.constraints import NonNeg as _NonNeg
from tensorflow.keras.constraints import MinMaxNorm as _MinMaxNorm
import tensorflow as _tf


# mixturemapping imports
from mixturemapping.distributions import createCovMatrix as _createCovMatrix
from mixturemapping.distributions import regularizeCovMatrix as _regularizeCovMatrix


class TrainableCovMatrix(_Layer):
    """Generates an independently trainable covariance matrix

    Important symmetry properties are generated automatically because the covariance matrix
    is built up from standard deviations `TrainableCovMatrix.spread`
    and correlations `TrainableCovMatrix.corr`.
    
    Params:
      output




    """

    def __init__(self, output_dim, regularize=None,  **kwargs):
        self._output_dim = output_dim
        self._regularize = regularize
        super(TrainableCovMatrix, self).__init__(**kwargs)

    def build(self, input_shapes):
        input_shape = input_shapes[0]

        # Create trainable weighs
        self.spread = self.add_weight(name='spread', shape=(
            1,  self._output_dim), initializer='uniform', trainable=True, constraint=_NonNeg())
        correlationSize = int(self._output_dim * (self._output_dim-1) / 2)
        if correlationSize > 0:
            self.corr = self.add_weight(name='correlation', shape=(
                correlationSize,), initializer='uniform', trainable=True, constraint=_MinMaxNorm(-1.0, 1.0))
        else:
            self.corr = [0]

        # Create the compute graph for the covariance addon part
        matrix = _createCovMatrix(self.spread, self.corr, self._output_dim)

        if(self._regularize):
            matrix = _regularizeCovMatrix(matrix, self._regularize)

        self.matrix = matrix

        # call build of the base Layer class
        super(TrainableCovMatrix, self).build(input_shape)

    def call(self, x, **kwargs):
        batch_size = _tf.shape(x)[0]
        return _tf.tile(self.matrix, [batch_size, 1, 1])

    def compute_output_shape(self, input_shape):
        return (input_shape[0], self._output_dim, self._output_dim)


    def get_config(self):
        config = super().get_config().copy()
        config.update({
            'output_dim': self._output_dim,
            'regularize': self._regularize
        })
        return config

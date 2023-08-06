# Copyright 2022 Intrinsic Innovation LLC.
# Copyright 2022 DeepMind Technologies Limited.
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

"""A sub-package defining different types of factors."""

import collections
from typing import Callable, OrderedDict, Type

import jax.numpy as jnp
from pgmax.factor import enum
from pgmax.factor import logical
from pgmax.factor import pool
from pgmax.factor.enum import EnumFactor
from pgmax.factor.enum import EnumWiring
from pgmax.factor.factor import concatenate_var_states_for_edges
from pgmax.factor.factor import Factor
from pgmax.factor.factor import Wiring
from pgmax.factor.logical import ANDFactor
from pgmax.factor.logical import LogicalFactor
from pgmax.factor.logical import LogicalWiring
from pgmax.factor.logical import ORFactor
from pgmax.factor.pool import PoolFactor
from pgmax.factor.pool import PoolWiring

FAC_TO_VAR_UPDATES: OrderedDict[Type[Factor], Callable[..., jnp.ndarray]] = (
    collections.OrderedDict([
        (EnumFactor, enum.pass_enum_fac_to_var_messages),
        (ORFactor, logical.pass_logical_fac_to_var_messages),
        (ANDFactor, logical.pass_logical_fac_to_var_messages),
        (PoolFactor, pool.pass_pool_fac_to_var_messages),
    ])
)

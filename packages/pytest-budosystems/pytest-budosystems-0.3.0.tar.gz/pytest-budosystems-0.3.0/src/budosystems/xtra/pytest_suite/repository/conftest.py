#
#  Copyright (c) 2022.  Budo Systems
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
"""Pytest configuration for this package."""

from typing import Optional, Union
from collections.abc import Mapping, Sequence
from attr import define
from pytest import fixture

from budosystems.models.core import Entity, BasicInfo
from budosystems.storage.repository import SaveOption

# pylint: disable=redefined-outer-name

__all__ = [
        "OneIntFieldEntity", "OneRefFieldEntity", "OneComplexFieldEntity",
        "SimpleUnionFieldEntity", "OptionalFieldEntity", "MappingFieldEntity",
        "SequenceFieldEntity", "KitchenSinkEntity",
        "init_data", "one_int_ent", "one_ref_ent", "one_complex_ent",
        "simple_union_ent", "opt_f_ent", "map_ent", "seq_ent", "kitchen_sink_ent",
        "params_list", "Params", "SaveParams", "LoadParams", "DeleteParams",
]

class OneIntFieldEntity(BasicInfo):
    """Sample Entity with an integer field."""
    i_var: int

class OneRefFieldEntity(BasicInfo):
    """Sample Entity with an Entity reference field."""
    ent_var: OneIntFieldEntity

class OneComplexFieldEntity(BasicInfo):
    """Sample Entity with a complex field."""
    c_var: complex

class SimpleUnionFieldEntity(BasicInfo):
    """Sample Entity with a simple Union field."""
    u_var: Union[int, str]

class OptionalFieldEntity(BasicInfo):
    """Sample Entity with an Optional field."""
    opt_var: Optional[float]

class MappingFieldEntity(BasicInfo):
    """Sample Entity with a Mapping field."""
    map_var: Mapping[str, int]

class SequenceFieldEntity(BasicInfo):
    """Sample Entity with a Sequence field."""
    seq_var: Sequence[int]

class KitchenSinkEntity(BasicInfo):
    """Sample Entity with just about every type of field we can think of."""
    s_var: str
    i_var: int
    f_var: float
    c_var: complex
    ent_var: OneIntFieldEntity
    u_var: Union[int, str]
    opt_var: Optional[float]
    map_var: Mapping[str, int]
    seq_var: Sequence[int]
    none_var: None
    b_var: bool
    opt_num_var: Union[int, float, complex, None]


@fixture(scope="class")
def one_int_ent() -> type[OneIntFieldEntity]:
    """Fixture returning an Entity type."""
    return OneIntFieldEntity

@fixture(scope="class")
def one_ref_ent() -> type[OneRefFieldEntity]:
    """Fixture returning an Entity type."""
    return OneRefFieldEntity

@fixture(scope="class")
def one_complex_ent() -> type[OneComplexFieldEntity]:
    """Fixture returning an Entity type."""
    return OneComplexFieldEntity


@fixture(scope="class")
def simple_union_ent() -> type[SimpleUnionFieldEntity]:
    """Fixture returning an Entity type."""
    return SimpleUnionFieldEntity


@fixture(scope="class")
def opt_f_ent() -> type[OptionalFieldEntity]:
    """Fixture returning an Entity type."""
    return OptionalFieldEntity

@fixture(scope="class")
def map_ent() -> type[MappingFieldEntity]:
    """Fixture returning an Entity type."""
    return MappingFieldEntity


@fixture(scope="class")
def seq_ent() -> type[SequenceFieldEntity]:
    """Fixture returning an Entity type."""
    return SequenceFieldEntity

@fixture(scope="class")
def kitchen_sink_ent() -> type[KitchenSinkEntity]:
    """Fixture returning an Entity type."""
    return KitchenSinkEntity


@fixture(scope="class")
def init_data(one_int_ent: type[OneIntFieldEntity],
              one_ref_ent: type[OneRefFieldEntity]) -> list[Entity]:
    """Fixture returning a list of data to initialize a `Repository`."""
    entities: list[Entity] = []

    for i in range(20):
        name = slug = f"int_{i}"
        e1 = one_int_ent(name=name, slug=slug, i_var=i)
        name = slug = f"ref_{i}"
        e2 = one_ref_ent(name=name, slug=slug, ent_var=e1)
        entities.append(e1)
        entities.append(e2)

    return entities


create_or_update = SaveOption.create_or_update
create_only = SaveOption.create_only
update_only = SaveOption.update_only

@define
class Params:
    """Base class for operation parameters."""
    label: str
    name_slug: str

@define
class SaveParams(Params):
    """Parameters for a Save operation."""
    new_val: int
    old_val: Optional[int]
    save_option: SaveOption

@define
class LoadParams(Params):
    """Parameters for a Load operation."""
    expected_val: int

@define
class DeleteParams(Params):
    """Parameters for a Delete operation."""
    must_exist: bool

@fixture(scope="class")
def params_list() -> list[Params]:
    """Fixture returning a list of Params."""
    p_list: list[Params] = [
        SaveParams("save_new_create_only", "int_100", 100, None, create_only),
    ]
    return p_list

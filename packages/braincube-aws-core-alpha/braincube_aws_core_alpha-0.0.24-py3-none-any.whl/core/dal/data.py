from enum import Enum
from dataclasses import dataclass

from ..utils.data import Order


class Key:
    def __init__(self, *args):
        self.values = list(args)


class SaveType(Enum):
    insert = "INSERT"
    update = "UPDATE"


class JoinType(Enum):
    inner = ""
    left = "LEFT"
    right = "RIGHT"
    outer = "FULL OUTER"
    left_outer = "LEFT OUTER"
    right_outer = "RIGHT OUTER"
    full_outer = "FULL OUTER"
    cross = "CROSS"
    hash = "HASH"


@dataclass()
class JoinThrough:
    from_column_name: str
    to_column_name: str


@dataclass()
class SimpleColumn:
    name: str
    alias: str | None = None


@dataclass()
class Column:
    name: str
    alias: str | None = None
    updatable: bool = True
    insertable: bool = True


@dataclass()
class StatementField:
    alias: str
    statement: str
    relations_aliases: list[str]


@dataclass()
class Relation:
    table: str
    alias: str | None
    force_join: bool
    columns: list[SimpleColumn]
    join_type: JoinType
    through: JoinThrough


@dataclass()
class Schema:
    table: str
    alias: str | None
    primary_key: list[str]
    order: list[Order]
    statement_fields: list[StatementField]
    columns: list[Column]
    relations: list[Relation]

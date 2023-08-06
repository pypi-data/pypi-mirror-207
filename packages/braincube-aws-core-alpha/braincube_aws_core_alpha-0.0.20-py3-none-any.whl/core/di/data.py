from enum import Enum
from typing import List, Dict, Tuple, Optional, Generic, TypeVar, Type
from dataclasses import dataclass


class Scope(Enum):
    request = "REQUEST"
    singleton = "SINGLETON"


T = TypeVar("T")


@dataclass()
class Dependency(Generic[T]):
    scope: Scope
    cls: Type[T]
    params: List[Tuple[type, Optional[str]]] = None
    name: Optional[str] = None
    instance: Optional[T] = None
    factory: Optional[callable] = None


def qualifier_to_data(qualifier: str) -> Dict[str, str]:
    d = dict()
    for s in qualifier.split(","):
        q = s.split(":")
        d[q[0]] = q[1]
    return d

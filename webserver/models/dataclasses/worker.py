import numpy as np
import numpy.typing as npt
from pymongo import MongoClient
from dataclasses import dataclass
from typing import List, Any, TypeVar, Callable, Type, cast
from uuid import uuid4

# dataclasses generated with Quicktype https://github.com/quicktype/quicktype
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = scene_from_dict(json.loads(json_string))

@dataclass
class Worker:
    id: Optional[str] = None
    api_key: Optional[str] = None
    owner_id: Optional[str] = None
    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Worker':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("_id"))
        api_key = from_union([from_str, from_none], obj.get("api_key"))
        owner_id = from_union([from_str, from_none], obj.get("owner_id"))
        type = from_union([from_str, from_none], obj.get("type"))
        return Worker(id, api_key, owner_id, type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["_id"] = from_union([from_str, from_none], self.id)
        if self.api_key is not None:
            result["api_key"] = from_union([from_str, from_none], self.api_key)
        if self.owner_id is not None:
            result["owner_id"] = from_union([from_str, from_none], self.owner_id)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        return result


def worker_from_dict(s: Any) -> Worker:
    return Worker.from_dict(s)


def worker_to_dict(x: Worker) -> Any:
    return to_class(Worker, x)
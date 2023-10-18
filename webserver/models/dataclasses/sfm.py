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
class Sfm:
    intrinsic_matrix: Optional[npt.NDArray] = None
    frames: Optional[List[Frame]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Sfm':
        assert isinstance(obj, dict)
        intrinsic_matrix = np.array(from_union([lambda x: from_list(lambda x: from_list(from_float, x), x), from_none], obj.get("intrinsic_matrix")))
        frames = from_union([lambda x: from_list(Frame.from_dict, x), from_none], obj.get("frames"))
        return Sfm(intrinsic_matrix, frames)

    def to_dict(self) -> dict:
        result: dict = {}
        result["intrinsic_matrix"] = from_union([lambda x: from_list(lambda x: from_list(from_float, x), x), from_none], self.intrinsic_matrix.tolist())
        result["frames"] = from_union([lambda x: from_list(lambda x: to_class(Frame, x), x), from_none], self.frames)

        #ingnore null
        result = {k:v for k,v in result.items() if v}
        return result
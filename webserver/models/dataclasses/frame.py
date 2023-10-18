import numpy as np
import numpy.typing as npt
from dataclasses import dataclass
from typing import Optional, Any, TypeVar
from webserver.models.dataclasses.helper import from_union,\
    from_float,from_str,from_list,from_none

# dataclasses generated with Quicktype https://github.com/quicktype/quicktype
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = scene_from_dict(json.loads(json_string))



T = TypeVar("T")

@dataclass
class Frame:
    file_path: Optional[str] = None
    extrinsic_matrix: Optional[npt.NDArray] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Frame':
        assert isinstance(obj, dict)
        file_path = from_union([from_str, from_none], obj.get("file_path"))

        extrinsic_matrix = np.array(from_union(\
            [lambda x: from_list(lambda x: from_list(from_float, x), x), from_none], obj.get("extrinsic_matrix")))
        
        return Frame(file_path, extrinsic_matrix)

    def to_dict(self) -> dict:
        result: dict = {}
        result["file_path"] = from_union([from_str, from_none], self.file_path)

        result["extrinsic_matrix"] = from_union(\
            [lambda x: from_list(lambda x: from_list(from_float, x), x), from_none], self.extrinsic_matrix.tolist())

        #ingnore null
        result = {k:v for k,v in result.items() if v}
        return result

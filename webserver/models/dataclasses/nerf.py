from dataclasses import dataclass
from typing import  Any, Optional, TypeVar
from webserver.models.dataclasses.helper import from_union,\
    from_str,from_none

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
class Nerf:
    model_file_path: Optional[str] = None
    rendered_video_path: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Nerf':
        assert isinstance(obj, dict)
        model_file_path = from_union([from_str, from_none], obj.get("model_file_path"))
        rendered_video_path = from_union([from_str, from_none], obj.get("rendered_video_path"))
        return Nerf(model_file_path, rendered_video_path)

    def to_dict(self) -> dict:
        result: dict = {}
        result["model_file_path"] = from_union([from_str, from_none], self.model_file_path)
        result["rendered_video_path"] = from_union([from_str, from_none], self.rendered_video_path)

        #ingnore null
        result = {k:v for k,v in result.items() if v}
        return result
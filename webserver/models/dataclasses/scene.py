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


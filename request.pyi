from enum import Enum
from .result import APIResultObject, APIPOSTResponse, APIPUTResponse, APIDELETEResponse
from typing import Dict, Any


class APIServer(Enum):
    def __getattr__(self, item) -> str:
        pass


class UNIRIOAPIRequest(object):
    def __init__(self, api_key: str, server: APIServer, debug: bool, cache):
        pass

    def get(self, path: str, params: Dict[str:Any], fields: list, cache_time: int) -> APIResultObject:
        pass

    def post(self, path: str, params: Dict[str:Any]) -> APIPOSTResponse:
        pass

    def delete(self, path: str, params: Dict[str:int]) -> APIDELETEResponse:
        pass

    def put(self, path: str, params: Dict[str:Any]) -> APIPUTResponse:
        pass

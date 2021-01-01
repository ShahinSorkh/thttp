from enum import Enum
from typing import Dict


class HttpStatus(Enum):
    OK = 200
    Created = 201
    Accepted = 202
    No_Content = 204
    Moved_Permanently = 301
    Moved_Temporarily = 302
    Not_Modified = 304
    Bad_Request = 400
    Unauthorized = 401
    Forbidden = 403
    Not_Found = 404
    Internal_Server_Error = 500
    Not_Implemented = 501
    Bad_Gateway = 502
    Service_Unavailable = 503

    @property
    def name(self):
        return super().name.replace('_', ' ')


class Response:
    def __init__(self, http_version: str, status: HttpStatus, headers: Dict[str, str], body: str):
        self.status = status
        self.http_version = http_version
        self.headers = headers
        self.body = body

    @property
    def headers_str(self):
        return '\r\n'.join(f'{k}: {v}' for k, v in self.headers.items())

    @property
    def status_line(self):
        return f'{self.http_version} {self.status.value} {self.status.name}'

    def tostring(self) -> str:
        return f'{self.status_line}\r\n{self.headers_str}\r\n\r\n{self.body}'

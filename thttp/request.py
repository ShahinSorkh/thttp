import json
from typing import Dict


class Request:
    def __init__(self, method: str, uri: str, http_version: str, headers: Dict[str, str], body: str):
        self.method = method
        self.uri = uri
        self.http_version = http_version
        self.headers = headers
        self.body = body

    def json(self):
        return json.loads(self.body)

    @classmethod
    def parse(cls, request_str: str):
        body, head_lines = _cut_request_head(request_str)
        [method, uri, http_version] = _extract_request_line_parts(head_lines)
        headers = _extract_headers(head_lines)

        return cls(method, uri, http_version, headers, body)


def _cut_request_head(request_str):
    [head, body] = request_str.split('\r\n\r\n')
    head_lines = head.split('\r\n')
    return body, head_lines


def _extract_headers(head_lines):
    headers_lines = [li for li in head_lines[1:] if li != '']
    headers = {k: v.strip() for [k, v] in (h.split(':') for h in headers_lines)}
    return headers


def _extract_request_line_parts(head_lines):
    request_line = head_lines[0]
    req_line_parts = request_line.split(' ')
    return req_line_parts

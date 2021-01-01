from unittest import TestCase

from thttp.request import Request


class RequestTest(TestCase):

    def test_simple_get_request(self):
        request_str = 'GET / HTTP/1.0\r\nAccept: text/html\r\nUser-Agent: foo/bar\r\n\r\n'
        request = Request.parse(request_str)

        self.assertEqual('GET', request.method)
        self.assertEqual('/', request.uri)
        self.assertEqual('HTTP/1.0', request.http_version)

        self.assertEqual({'Accept': 'text/html', 'User-Agent': 'foo/bar'}, request.headers)
        self.assertEqual('', request.body)

    def test_simple_post_request(self):
        request_str = 'POST /users HTTP/1.0\r\nAccept: text/html\r\nUser-Agent: foo/bar\r\n\r\n{"name": "foo"}'
        request = Request.parse(request_str)

        self.assertEqual('POST', request.method)
        self.assertEqual('/users', request.uri)
        self.assertEqual('HTTP/1.0', request.http_version)

        self.assertEqual({'Accept': 'text/html', 'User-Agent': 'foo/bar'}, request.headers)
        self.assertEqual('{"name": "foo"}', request.body)
        self.assertEqual({'name': 'foo'}, request.json())

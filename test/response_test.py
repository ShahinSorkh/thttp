from unittest import TestCase

from thttp.response import Response, HttpStatus


class ResponseTest(TestCase):

    def test_404_response(self):
        response = Response('HTTP/1.0', HttpStatus.Not_Found, {'Content-Type': 'text/html'}, '<html></html>')
        self.assertEqual('HTTP/1.0 404 Not Found\r\nContent-Type: text/html\r\n\r\n<html></html>', response.tostring())

    def test_200_response(self):
        response = Response('HTTP/1.0', HttpStatus.OK, {'Content-Type': 'text/html'}, '<html></html>')
        self.assertEqual('HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\n<html></html>', response.tostring())

import unittest
import requests
from nginxtest.server import NginxServer


class TestMyNginx(unittest.TestCase):

    def setUp(self):
        self.nginx = NginxServer()
        self.nginx.start()

    def tearDown(self):
        self.nginx.stop()

    def testHello(self):
        resp = requests.get(self.nginx.root_url)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('Welcome to nginx!' in resp.text)

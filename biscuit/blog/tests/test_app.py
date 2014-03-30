import unittest
import webtest


class DummyAssets(object):
    def urls(self):
        return []


class TestApp(unittest.TestCase):
    def test_it(self):
        from biscuit.blog import Application
        assets = {
            'css-all': DummyAssets(),
            'js-all': DummyAssets(),
        }
        app = Application(assets)
        app = webtest.TestApp(app)
        app.get('/')

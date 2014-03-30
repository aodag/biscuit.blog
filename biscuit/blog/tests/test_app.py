import unittest
import webtest
from ..testing import DummyAssets, use_database, _makeBlog

class TestApp(unittest.TestCase):
    def test_it(self):
        from biscuit.blog import Application
        assets = {
            'css-all': DummyAssets(),
            'js-all': DummyAssets(),
        }
        app = Application(assets)
        app = webtest.TestApp(app)
        with use_database('sqlite:///'):
            _makeBlog(name='default')
            app.get('/')

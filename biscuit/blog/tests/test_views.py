import unittest
from testfixtures import compare
from ..testing import DummyAssets, use_database, _makeBlog


class DummyTemplateLookup(object):
    def get_template(self, name):
        return DummyTemplate()

class DummyTemplate(object):
    def render(self, *args, **kwargs):
        return args, kwargs

class Testindex(unittest.TestCase):

    def _callFUT(self, *args, **kwargs):
        from biscuit.blog.views import index
        return index(*args, **kwargs)

    def test_it(self):
        import webob
        request = webob.Request.blank('/')
        assets = {}
        request.environ['webassets.assets'] = assets
        request.environ['mako.lookup.templates'] = DummyTemplateLookup()
        with use_database('sqlite:///'):
            _makeBlog(name='default')
            result = self._callFUT(request)

        compare(result, ((), {'assets': assets,
                              'message': 'Hello'}))

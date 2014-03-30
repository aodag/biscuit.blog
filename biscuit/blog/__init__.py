import os
from webdispatch.urldispatcher import URLDispatcher
from webdispatch import MethodDispatcher
from webob.dec import wsgify
from mako.lookup import TemplateLookup
from . import views

here = os.path.dirname(__file__)
templates = TemplateLookup(os.path.join(here, "templates"))


class Application(URLDispatcher):
    def __init__(self, assets):
        super(Application, self).__init__()
        self.assets = assets
        self.add_url('top', '/', wsgify(views.index))

    def get_extra_environ(self):
        return {"webassets.assets": self.assets,
                "mako.lookup.templates": templates}

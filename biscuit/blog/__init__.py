import os
from webob.dec import wsgify
from webdispatch.urldispatcher import URLDispatcher
from webdispatch import MethodDispatcher
from mako.lookup import TemplateLookup


here = os.path.dirname(__file__)
templates = TemplateLookup(os.path.join(here, "templates"))

@wsgify
def index(request):
    assets = request.environ['webassets.assets']
    tmpl = templates.get_template('index.html')
    return tmpl.render(message="Hello", assets=assets)


class Application(URLDispatcher):
    def __init__(self, assets):
        super(Application, self).__init__()
        self.assets = assets
        self.add_url('top', '/', index)

    def get_extra_environ(self):
        return {"webassets.assets": self.assets}

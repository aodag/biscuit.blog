from webob.dec import wsgify
from webdispatch.urldispatcher import URLDispatcher
from webdispatch import MethodDispatcher


@wsgify
def index(request):
    return "Hello"


class Application(URLDispatcher):
    def __init__(self):
        super(Application, self).__init__()
        self.add_url('top', '/', index)

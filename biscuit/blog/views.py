from .models import Blog


def index(request):
    blog = Blog.query.filter(Blog.default).one()
    assets = request.environ['webassets.assets']
    tmpl = request.environ['mako.lookup.templates'].get_template('index.html')
    return tmpl.render(message="Hello", assets=assets)


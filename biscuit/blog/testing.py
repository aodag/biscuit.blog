import contextlib


class DummyAssets(object):
    def urls(self):
        return []


@contextlib.contextmanager
def use_database(url):
    from sqlalchemy import create_engine
    from .models import DBSession, Base
    engine = create_engine(url)
    Base.metadata.create_all(bind=engine)
    DBSession.remove()
    DBSession.configure(bind=engine)
    try:
        yield engine
    finally:
        import transaction
        transaction.abort()
        DBSession.remove()
        Base.metadata.drop_all(bind=engine)


def _makeBlog(*args, **kwargs):
    from .models import DBSession, Blog
    blog = Blog(*args, **kwargs)
    DBSession.add(blog)
    return blog

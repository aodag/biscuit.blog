from sqlalchemy import (
    Column,
    Date,
    Integer,
    Unicode,
)
from sqlalchemy.orm import (
    relationship,
    scoped_session,
    sessionmaker,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from zope.sqlalchemy import ZopeTransactionExtension


Base = declarative_base()
DBSession = scoped_session(
    sessionmaker(extension=ZopeTransactionExtension()))


class Blog(Base):
    __tablename__ = 'blogs'
    query = DBSession.query_property()
    id = Column(Integer, primary_key=True)
    name = Column(Unicode)
    title = Column(Unicode)

    @hybrid_property
    def default(self):
        return self.name == 'default'


class Entry(Base):
    __tablename__ = 'entries'
    query = DBSession.query_property()
    id = Column(Integer, primary_key=True)
    name = Column(Unicode)
    title = Column(Unicode)
    date = Column(Date)


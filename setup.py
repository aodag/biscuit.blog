from setuptools import setup


requires = [
    "webob",
    "webdispatch",
    "mako",
    "sqlalchemy",
    "zope.sqlalchemy",
    "repoze.tm2",
    "docutils",
    "webhelpers2>=2.0b5",
    "babel",
]

tests_require = [
    "testfixtures",
    "webtest",
]


setup(name="biscuit.blog",
      packages=["biscuit"],
      namespace_packages=["biscuit"],
      install_requires=requires,
      tests_require=tests_require,
      test_suite="biscuit.blog",
      extras_require={
          "testing": tests_require,
      },
)

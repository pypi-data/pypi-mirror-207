from setuptools import setup

name = "types-beautifulsoup4"
description = "Typing stubs for beautifulsoup4"
long_description = '''
## Typing stubs for beautifulsoup4

This is a PEP 561 type stub package for the `beautifulsoup4` package. It
can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
PyCharm, etc. to check code that uses
`beautifulsoup4`. The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/beautifulsoup4. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit `d1bfd08b4bc843227d097decfd99d70272a1f804`.
'''.lstrip()

setup(name=name,
      version="4.12.0.5",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/beautifulsoup4.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=['types-html5lib'],
      packages=['bs4-stubs'],
      package_data={'bs4-stubs': ['__init__.pyi', 'builder/__init__.pyi', 'builder/_html5lib.pyi', 'builder/_htmlparser.pyi', 'builder/_lxml.pyi', 'dammit.pyi', 'diagnose.pyi', 'element.pyi', 'formatter.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)

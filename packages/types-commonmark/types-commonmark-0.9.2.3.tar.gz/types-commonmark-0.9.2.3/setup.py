from setuptools import setup

name = "types-commonmark"
description = "Typing stubs for commonmark"
long_description = '''
## Typing stubs for commonmark

This is a PEP 561 type stub package for the `commonmark` package. It
can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
PyCharm, etc. to check code that uses
`commonmark`. The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/commonmark. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit `d1bfd08b4bc843227d097decfd99d70272a1f804`.
'''.lstrip()

setup(name=name,
      version="0.9.2.3",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/commonmark.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['commonmark-stubs'],
      package_data={'commonmark-stubs': ['__init__.pyi', 'blocks.pyi', 'cmark.pyi', 'common.pyi', 'dump.pyi', 'entitytrans.pyi', 'inlines.pyi', 'main.pyi', 'node.pyi', 'normalize_reference.pyi', 'render/__init__.pyi', 'render/html.pyi', 'render/renderer.pyi', 'render/rst.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)

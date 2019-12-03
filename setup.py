#!/usr/bin/env python

import io
import os
import re

from setuptools import setup

package_name = "py7zr"

root_dir = os.path.abspath(os.path.dirname(__file__))


def readme():
    with io.open(os.path.join(os.path.dirname(__file__), 'README.rst'), mode="r", encoding="UTF-8") as readmef:
        return readmef.read()


with open(os.path.join(root_dir, package_name, '__init__.py')) as f:
    init_text = f.read()
    license = re.search(r'__license__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    author = re.search(r'__author__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    author_email = re.search(r'__author_email__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    url = re.search(r'__url__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)

assert license
assert author
assert author_email
assert url

setup(name=package_name,
      use_scm_version=True,
      description='Pure python 7-zip decompression(restricted) library',
      url='http://github.com/miurahr/py7zr',
      license=license,
      long_description_content_type='text/x-rst',
      long_description=readme(),
      keywords='compression, 7zip, lzma',
      author=author,
      author_email=author_email,
      packages=[package_name],
      install_requires=['texttable', 'pathlib2>=2.2.0;python_version<"3.6"'],
      setup_requires=['setuptools-scm>=3.3', 'setuptools>=42.0'],
      extras_require={'dev': ['pytest']},
      scripts=["bin/py7zr"],
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Console',
                   'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
                   'Operating System :: MacOS :: MacOS X',
                   'Operating System :: Microsoft :: Windows',
                   'Operating System :: POSIX',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   'Programming Language :: Python :: 3.8',
                   'Programming Language :: Python :: 3 :: Only',
                   'Topic :: System :: Archiving :: Compression',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   ]
      )

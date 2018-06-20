# encoding: utf-8
from setuptools import find_packages
from setuptools import setup
import os

version = '0.1.dev0'

setup(name='python.tools',
      version=version,
      description="Python Tools",
      long_description=open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
          "Programming Language :: Python",
      ],
      keywords=['python', 'tools'],
      author='FBruynbroeck',
      author_email='francois.bruynbroeck@hotmail.com',
      url='https://github.com/FBruynbroeck/python-tools',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['python', 'python.tools'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zest.releaser',
          'GitPython',
      ],
      extras_require={
      },
      entry_points={
          'zest.releaser.releaser.middle': [
              'datacheck = python.tools.release:datacheck',
          ],
          'console_scripts': [
              'reload_hooks = python.tools.hooks:reload_hooks',
              'remove_hooks = python.tools.hooks:remove_hooks',
              'changelogrelease = python.tools.release:change_log',
          ],
      },
      )

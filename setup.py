from setuptools import setup, Extension

setup(
  name = 'bfac',
  packages=['bfac'],
  version = '1.1',
  scripts=['bfac/bfac'],
  description = "An automated tool that checks for backup artifacts that may discloses the web-application's source code.",
  long_description=open('README.md').read(),
  author = 'Mazin Ahmed',
  author_email = 'mazin@mazinahmed.net',
  url = 'https://github.com/mazen160/bfac',
  keywords = ['backup','artifacts','checker','web scanner','web vulnerability scanner','bfac'],
  install_requires = ['argparse', 'requests'],
  license="GPL-3.0"
)







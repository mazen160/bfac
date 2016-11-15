from distutils.core import setup

setup(
  name = 'bfac',
  packages=['bfac'],
  version = '1.1',
  scripts=['bfac'],
  description = "An automated tool that checks for backup artifacts that may discloses the web-application's source code.",
  long_description=open('README.txt').read(),
  author = 'Mazin Ahmed',
  author_email = 'mazin@mazinahmed.net',
  url = 'https://github.com/mazen160/bfac',
  keywords = ['backup'],
  install_requires = ['argparse', 'request'],
  license="GPL-3.0"
)
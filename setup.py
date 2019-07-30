from distutils.core import setup

name = 'torrsearch'
version = '0.0.1'
setup(
  name=f'{name}',
  packages=['pytorrsearch'],  # this must be the same as the name above
  version=f'{version}',
  description='Module for searching in popular Russian torrent trackers',
  author='Sheludchenkov Aleksey',
  author_email='aleshkashell@gmail.com',
  url=f'https://github.com/aleshkashell/pytorrsearch',
  download_url=f'https://github.com/aleshkashell/pytorrsearch/tarball/{version}',
  keywords=['torrent', 'rutor', 'rutracker'],
  classifiers=[],
  install_requires=[
          'requests',
      ],
)
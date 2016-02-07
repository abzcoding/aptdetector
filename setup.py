"""Advanced Persistent Threat Detection by
Using Network Analysis.

used as a package or independently. `documented on Read
the Docs <http://aptdetector.readthedocs.org>`_.
"""

from setuptools import setup


__author__ = 'Abouzar Parvan'
__version__ = '0.1'
__contact__ = 'abzcoding@gmail.com'
__url__ = 'https://github.com/abzcoding/APTDetector'
__license__ = 'BSD'


setup(name='APTDetector',
      version=__version__,
      description="Advanced Persistent Threat Detection by Using Network Analysis.",
      long_description=__doc__,
      author=__author__,
      author_email=__contact__,
      url=__url__,
      packages=['aptdetector'],
      include_package_data=True,
      zip_safe=False,
      license=__license__,
      platforms='linux_x86_64',
      classifiers=[
          'Topic :: Security',
          'Intended Audience :: Education',
          'Topic :: System :: Networking',
          'Development Status :: 1 - Planning',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5', ]
      )

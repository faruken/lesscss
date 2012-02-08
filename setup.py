"""

lesscss

"""

from setuptools import (setup, find_packages)
from lesscss import (__version__, __doc__)

setup(

    name='lesscss',
    version=__version__,
    url='http://github.com/faruken/lesscss',
    license='BSD',
    author='Faruk Akgul',
    author_email='me@akgul.org',
    description='A helper which automatically compiles LESS files to CSS.',
    long_description=__doc__,
    zip_safe=False,
    packages=find_packages(exclude=['examples']),
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

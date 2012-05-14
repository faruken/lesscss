"""

lesscss

"""

__doc__ = """

About
=====

LessCSS is a helper which automatically compiles LESS files to CSS when LESS
files are modified. It works with Brubeck and web.py web frameworks. Although
it's not tested on other frameworks such as bottle, it should work without any
problems.

**Note:** You need to install LESS before using this.

Installation
============

::

    $ pip install lesscss


Usage
=====

::

    from lesscss import LessCSS
    LessCSS(media_dir='media', exclude_dirs=['img', 'src'], based=True, compressed=True, compression='x', output_dir=None)


Parameters
==========

- **media_dir:** Directory where you put static/media files such as css/js/img.
- **exclude_dirs:** Directories you don't want to be searched. It'd be pointless to search for less files in an images directory. This parameter is expected to be a list.
- **based:** If it's set True then LessCSS will generate the style-(base60).css version as well (for example; style-dHCFD.css). This is useful if you set expire times of static files to a distant future since browsers will not retrieve those files unless the name is different or the cache has expired. This parameter is expected to be a boolean value.
- **compressed**: If it's set `True` then LessCSS will minimize the generated CSS files. This parameter is expected to be a boolean value.
- **compression**: Specifies the type of compression to use. Default to the normal compression, 'x'. Other option is to use the [YUI Compressor](http://developer.yahoo.com/yui/compressor/css.html), 'yui'. See "Command-line Usage" at http://lesscss.org/.
- **output_dir:** Directory where you put compiled CSS files if different than location of .less file.


Links
=====

* `Developer Release <http://github.com/faruken/lesscss>`_

"""

from setuptools import (setup, find_packages)

setup(

    name='lesscss',
    version='0.1.2',
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

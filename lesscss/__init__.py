# -*- coding: utf-8 -*-

"""
    lesscss
    ~~~~~~~
    A small helper which automatically compiles LESS files to CSS when you
    modify LESS files of your project.

    :copyright: (c) 2012 Faruk Akgul.
    :license: BSD, see LICENSE for more details.
"""

import os
import re
import subprocess
from uuid import uuid4


class LessCSS(object):

    """LessCSS is a helper which automatically compiles LESS files to CSS when
    the LESS files are modified. It works with Brubeck and web.py web
    frameworks. Although it's not tested on other frameworks such as bottle,
    it should work without any problems.

    Sample Brubeck and web.py projects are in `examples` folder.
    """

    def __init__(self, media_dir='static', exclude_dirs=None, based=True,
                compressed=True, compression='x', output_dir=None):
        """ Initialize LessCSS. When you wrap your web application you need to
        define the following parameters:

        ``media_dir``
            Define the absolute path of the folder where you put all your
            static files such as css/js.

        ``exclude_dirs``
            If you don't want certain folders to be checked (such as a folder
            where you put your image and javascript files), put folder names
            into the list. LessCSS will not check those folders.

        ``based``
            If this is set to `True`, then LessCSS will generate
            `style-base.css` as well (for example; `style-dHCFD.css`). This is
            useful if you set expire times of static files for a long time
            since browsers will not retrieve those files unless the name is
            different or the cache has expired.

        ``compressed``
            If this is set to `True`, then the compiled CSS file will be
            minimized.

        ``compression``
            The type of compression to use. Default to standard 'x' compression.
            Set to 'yui' to use YUI Compressor
            (http://developer.yahoo.com/yui/compressor/css.html).
            See "Command-line Usage" at http://lesscss.org/

        ``output_dir``
            Define the absolute path of the folder where compiled CSS files
            should be put.

        """
        self._media = media_dir
        self._based = based
        self._compressed = compressed
        self._compression = compression
        self._excluded = exclude_dirs
        self._output = output_dir.rstrip('/') if output_dir else None
        self.compile()

    @classmethod
    def to60(cls, val):
        """Base60 generator.

        ``val``
            Parameter which its base64 value is generated. This is expected to
            be an integer.

        """
        CHARS = '0123456789ABCDEFGHJKLMNPQRSTUVWXYZ_abcdefghijkmnopqrstuvwxyz'
        LEN = len(CHARS)
        l = []
        while val > 0:
            val, rem = divmod(val, LEN)
            l.insert(0, CHARS[rem])
        return ''.join(l)

    def get_less(self):
        """Walks through subdirectories and puts LESS files into a list.
        """
        media_dir = self._media
        less = []
        REGEX = re.compile(r'^.*[.](?P<ext>less|\w+)$', re.I)
        for root, dirs, files in os.walk(media_dir):
            if self._excluded is not None and isinstance(self._excluded, list):
                [dirs.remove(exclude)
                                        for exclude in self._excluded
                                        if exclude in dirs]
            less.extend([
                            os.path.join(root, i)
                            for i in files
                            if REGEX.match(i).group('ext') == 'less'
                        ])
        return less

    def compile(self):
        """Compiles LESS files to CSS if necessary. It does it by checking
        the last modified time. If `based` is `True` then base60 filename of
        LESS file is generated as well.

        #TODO: Automatically set CSS name in HTML templates.
        """
        less = self.get_less()
        command_opt = ['lessc', '-x']
        if not self._compressed:
            del command_opt[-1]
        if self._compressed and self._compression.lower() == 'yui':
            command_opt[1] = '--yui-compress'
        for i in less:
            filename = os.path.splitext(i)[0]
            css = '%s.css' % filename
            if self._output:
                css = css.split('/')[-1]
                css = '%s/%s' % (self._output, css)
            css_time = -1  # Poor man's Integer.MIN_VALUE
            if os.path.isfile(css):
                css_time = os.path.getmtime(css)
            less_time = os.path.getmtime(i)
            if less_time >= css_time:
                command_opt.append(i)
                command_opt.append(css)
                subprocess.call(command_opt, shell=False)
                if self._based:
                    del command_opt[-1]
                    css_based = '%s-%s.css' % (filename,
                                                LessCSS.to60(uuid4().time_low))
                    if self._output:
                        css_based = css_based.split('/')[-1]
                        css_based = '%s/%s' % (self._output, css_based)
                    command_opt.append(css_based)
                    subprocess.call(command_opt, shell=False)

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

    def __init__(self, media_dir='static', exclude_dirs=None, based=True):
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
        """
        self._media = media_dir
        self._based = based
        self._excluded = exclude_dirs
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
        for i in less:
            filename = os.path.splitext(i)[0]
            css = '%s.css' % filename
            css_time = -1  # Poor man's Integer.MIN_VALUE
            if os.path.isfile(css):
                css_time = os.path.getmtime(css)
            less_time = os.path.getmtime(i)
            if less_time >= css_time:
                subprocess.call(['lessc', i, css], shell=False)
                if self._based:
                    css_based = '%s-%s.css' % (filename,
                                                LessCSS.to60(uuid4().time_low))
                    subprocess.call(['lessc', i, css_based], shell=False)

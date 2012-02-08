#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web

render = web.template.render('templates')


class Index(object):
  def GET(self):
    return render.index()

DEBUG = True
web.config.debug = DEBUG
app = web.application((r'^/', 'Index'), globals(), autoreload=True)


if __name__ == '__main__':
  if DEBUG:
    from lesscss import LessCSS
    LessCSS(compressed=False)
  app.run()

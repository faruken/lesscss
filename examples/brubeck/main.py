#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from brubeck.templating import load_jinja2_env
from brubeck.connections import Mongrel2Connection
from brubeck.request_handling import Brubeck
from brubeck.templating import Jinja2Rendering


class IndexHandler(Jinja2Rendering):
  def get(self):
    return self.render_template('index.html')


config = {
  'mongrel2_pair': Mongrel2Connection('ipc://127.0.0.1:9999', 'ipc://127.0.0.1:9998'),
  'handler_tuples': [(r'^/$', IndexHandler)],
  'log_level': logging.DEBUG,
  'template_loader': load_jinja2_env('templates'),
}

app = Brubeck(**config)

if __name__ == '__main__':
  DEBUG = True
  if DEBUG:
    from lesscss import LessCSS
    LessCSS(media_dir='static', exclude_dirs=['.fr'], based=False)

  app.run()

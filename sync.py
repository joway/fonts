#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse
import errno
import re
import requests
import os
import json

FONTS_DOMAIN = 'fonts.joway.io'

FONTS = [
  'Noto+Sans+TC',
  'Permanent+Marker',
  'Arvo',
]

def get_font_urls(content):
  return re.findall('url\((.+?)\)', content)

def fetch_data(url):
  req = requests.get(url)
  return req.text

def write_file(fn, data):
  if not os.path.exists(os.path.dirname(fn)):
    try:
        os.makedirs(os.path.dirname(fn))
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
  with open(fn, 'w') as f:
    f.write(data.encode('utf-8'))

def main():
  for font in FONTS:
    filename = './css/{0}.css'.format(font)
    css_content = fetch_data(
      'https://fonts.googleapis.com/css?family={0}'.format(font),
    )
    font_urls = get_font_urls(css_content)
    for url in font_urls:
      print('downloading font: {0}'.format(url))
      # download font
      font_content = fetch_data(url)
      parsed_uri = urlparse(url)
      font_filename = parsed_uri.path
      write_file('.' + font_filename, font_content)
      
      # rewrite css
      domain = parsed_uri.netloc
      css_content = css_content.replace(domain, FONTS_DOMAIN)

    with open(filename, 'w') as file:
      file.write(css_content)

  write_file('./fonts.json', json.dumps(FONTS))

main()

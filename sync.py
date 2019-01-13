#!/usr/bin/env python3
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

def get_font_urls(content):
  return re.findall('url\((.+?)\)', content)

def fetch_data(url, count=3):
  try:
    req = requests.get(url)
    return req.text
  except Exception as e:
    if count <= 0:
      raise e
    return fetch_data(url, count - 1)

def read_file(fn):
  with open(fn, 'r') as f:
    return f.read()

def write_file(fn, data):
  if not os.path.exists(os.path.dirname(fn)):
    try:
        os.makedirs(os.path.dirname(fn))
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
  with open(fn, 'w') as f:
    f.write(data)

def main():
  fonts_content = read_file('./fonts.json')
  fonts = json.loads(fonts_content)
  css_contents = []

  for item in fonts:
    try:
      font = item['family']
      font_plus = font.replace(' ', '+')
      filename = './css/{0}.css'.format(font)
      filename_plus = './css/{0}.css'.format(font_plus)

      css_content = fetch_data(
        'https://fonts.googleapis.com/css?family={0}'.format(font),
      )
      css_contents.append(css_content)
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
      
      write_file(filename, css_content)
      write_file(filename_plus, css_content)

    except Exception as e:
      print(e)

  write_file('./css/index.css', '\n'.join(css_contents))

main()

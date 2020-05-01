#!/usr/bin/python3

import requests
import xml.etree.ElementTree as ET 
import logging
import os
import re

def displaymatch(match):
  if match is None:
    return None
  return '<Match: %r, groups=%r>' % (match.group(), match.groups())

def download(link, torrent):
  r = requests.get(link)
  logging.info("write content to file")
  
  with open(('/watch/' + torrent), 'wb') as f:
    f.write(r.content)

  done = "Torrents should be downloading now!"
  logging.info(done)

def rss(url, regex):
  logmsg = "We're pulling the bookmarks from " + url 
  logging.info(logmsg)

  logging.info("getting url content")
  r = requests.get(url)

  logging.info("setting root var from r.content")
  root = ET.fromstring(r.content)

  logging.info("starting xml breakdown")
  for channel in root.findall('channel'):
    logging.info("find items")
    for item in channel.findall('item'):
      title = item[0].text
      link = item[1].text
      torrent = title + ".torrent"
      if(regex):
        for x in regex:
          logging.info("starting regex match")
          matched = False
          for x in regex:
            if(matched):
              print('already matched once')
            else:
              matched = re.match(x, title)
              if(matched):
                print(matched.group)
                download(link, torrent)
                matched = True
              # else:
              #   print("no matches")
      else:
        download(link, torrent)

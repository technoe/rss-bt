#!/usr/bin/python3

import requests
import xml.etree.ElementTree as ET 
import logging
import os

def rss(url):
  logmsg = "We're pulling the bookmarks from " + url 
  logging.info(logmsg)

  logging.info("getting url content")
  r = requests.get(url)

  logging.info("setting root var from r.content")
  root = ET.fromstring(r.content)

  logging.info("starting xml breakdown")
  for channel in root.findall('channel'):
    logging.info("find items")
    items = channel.findall('item')
    count = len(items)

    if(count < 1):
        message = "no bookmarks found"
        logging.info(message)
    else:
      for item in items:
        logging.info("set title")
        title = item.find('title').text
        logging.info("set link")
        link = item.find('link').text
        logging.info("set tname")
        tname = title + ".torrent"
        
        message = "Downloading " + title + " to " + tname
        logging.info(message)

        logging.info("requesting uri content")
        r = requests.get(link)

        logging.info("write content to file")
        with open(('/watch/' + tname), 'wb') as f:
          f.write(r.content)

        done = "Torrents should be downloading now!"
        logging.info(done)

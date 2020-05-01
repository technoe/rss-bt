#!/usr/bin/python3

import requests
import xml.etree.ElementTree as ET 
import logging
import os
import re

def tdown(title, tname, link):
  message = "Downloading " + title + " to " + tname
  logging.info(message)

  logging.info("requesting uri content")
  r = requests.get(link)

  logging.info("write content to file")
  with open(('/watch/' + tname), 'wb') as f:
    f.write(r.content)

  done = "Torrents should be downloading now!"
  logging.info(done)

def rss(url, matches):
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
    if count < 10:
      print(items)

    if count < 1:
        message = "no bookmarks found"
        logging.info(message)
    else:
      for item in items:
        title = item.find('title').text
        logging.info("set title: " + title)
        link = item.find('link').text
        logging.info("set link: " + link)
        tname = title + ".torrent"
        logging.info("set tname: " + tname)
        
        if matches:
          for match in matches:
            for i in match:
              pattern = re.compile(i)
              if pattern.search(title):
                print("match found")
                print("match title is: " + title)
                tdown(title, tname, link)
        elif not matches:
          print(title, tname, link)
          tdown(title, tname, link)

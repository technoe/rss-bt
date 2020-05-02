#!/usr/bin/python3

import requests
import xml.etree.ElementTree as ET 
import logging
import os
import re

def get_torrent_title(item):
  title = item.find('title').text
  logging.info("set title: " + title)
  return title

def get_torrent_link(item):
  link = item.find('link').text
  logging.info("set link: " + link)
  return link

def set_filename(item):
  text = item.find('title').text
  name = text + ".torrent"
  logging.info("set filename: " + name)
  return name

def tdown(title, filename, link):
  message = "Downloading " + title + " to " + filename
  logging.info(message)

  logging.info("requesting uri content")
  r = requests.get(link)

  logging.info("write content to file")
  with open(('/watch/' + filename), 'wb') as f:
    f.write(r.content)

  done = title + " is downloading now to " + filename + ".torrent"
  logging.info(done)
  return done

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
        if matches:
          for match in matches:
            for i in match:
              pattern = re.compile(i)
              title = get_torrent_title(item)
              if pattern.search(title):
                print("match found")
                print("match title is: " + title)
                filename = set_filename(item)
                link = get_torrent_link(item)
                tdown(title, filename, link)
        elif not matches:
          title = get_torrent_title(item)
          filename = set_filename(item)
          link = get_torrent_link(item)
          print(title, filename, link)
          tdown(title, filename, link)

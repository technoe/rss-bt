#!/usr/bin/python3

import requests
import xml.etree.ElementTree as ET 
import logging
import os
import re

def logger(linenumber, message):
  header = 50*"="
  mout = "\n{}\n{}\n{}\n{}\n"
  logging.info(mout.format(header,linenumber,message,header))

def get_torrent_title(item):
  title = item.find('title').text
  logger("17", ("set title: " + title))
  return title

def get_torrent_link(item):
  link = item.find('link').text
  logger("22", "set link: " + link)
  return link

def set_filename(item):
  text = item.find('title').text
  name = text + ".torrent"
  logger("28", "set filename: " + name)
  return name

def tdown(title, filename, link):
  message = "Downloading {} to {}"
  logger("35", message.format(title, filename))

  logger("37", "requesting uri content")
  r = requests.get(link)

  logger("40", "write content to file")
  with open(('/watch/' + filename), 'wb') as f:
    f.write(r.content)

  done = "{} is downloading now to {}.torrent"
  logger("42", done.format(title, filename))
  return done

def check_for_bookmarks(url):
  logmsg = "We're pulling the bookmarks from {}" 
  logger("47", logmsg.format(url))

  r = requests.get(url)

  logger("51", "setting root var from r.content")
  root = ET.fromstring(r.content)

  logger("54", "starting xml breakdown")
  for channel in root.findall('channel'):
    logger("56", "find items")
    
    items = channel.findall('item')
    count = len(items)

  if count < 1:
    logger("66", "no bookmarks found")
    return False
  else:
    return items

def rss(url, matches):
  items = check_for_bookmarks(url)
  for item in items:
    for match in matches:
      pattern = re.compile(match)
      title = get_torrent_title(item)
      if pattern.search(title):
        m = "Match found on title {}"
        logger("74", m.format(title))
        filename = set_filename(item)
        link = get_torrent_link(item)
        tdown(title, filename, link)

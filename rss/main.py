#!/usr/bin/python3

import torrents
import logging
from ruamel.yaml import YAML

logger = "service starting"
logging.basicConfig(level=logging.INFO)
logging.info(logger)

config_file = open("/rss/config.yml", 'r')
logging.info("pull config file")
yaml = YAML(typ='safe')
logging.info("set yaml type safe")
data = yaml.load(config_file)
logging.info("data created with yaml config")
regex = []
logging.info("set empty regex list")

for i in data['feeds']:
  logging.info("start loop")

  url = i['feed']['url']
  logging.info("url: " + url)
  
  if "matches" in i['feed']:
    regex.append(i['feed']['matches'])

  torrents.rss(url,regex)

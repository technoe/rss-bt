#!/usr/bin/python3

import torrents
import logging
from ruamel.yaml import YAML

logger = "service starting..."
logging.basicConfig(level=logging.INFO)
logging.info(logger)

config_file = open("/rss/config.yml", 'r')
yaml = YAML(typ='safe')
data = yaml.load(config_file)

for i in data['feeds']:
  url = i['feed']['url']
  torrents.rss(url)

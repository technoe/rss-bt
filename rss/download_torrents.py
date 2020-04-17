#!/usr/bin/python3
import subprocess
import glob
import os 

def watch():
  torrents = glob.glob('./*.torrent')
  for i in torrents:
      subprocess.run(["scp",i,"rancher@192.168.0.108:/mnt/b/transmission/watch/"])
      os.remove(i)

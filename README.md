rss-bt
===

This is a super simple image with a super simple python script designed to automatically
pull my bookmarked rss feeds. I currently have it running on a 5m schedule.

I mount the *watch* dir from my transmissionbt service to the *watch* directory here. Now I can simply download the links locally and let the auto-watch feature do its job.

This runs as a one time use service

Now with a more flexible config file start! See example below

Usage
---

```code
docker run -d -v $PWD/watch:/watch/ -v $PWD/rss-config.yml:/rss/config.yml minoe:rss-bt
```

```yaml
version: "2"
services:
  rss:
    image: minoe/rss:latest
    volumes:
    - /path/to/watch/dir/:/watch/
    - /path/to/config.yml:/rss/config.yml
    lables:
      io.rancher.container.start_once: 'true'
      cron.schedule: '@every 5m'

```

Config File Example
---

```yaml
feeds:
  - feed:
      url: https://favorite-torrent-rss-feed
      matches:
        - "(Bill.And.Teds.Excellent.Adventure.1989)"
  
  - feed:
      url: https://some-other-rss-feed
      matches:
        - ".+" # everything!
```

Details
---

Starting with the Ubuntu 20.04 image, I add python3 and pip3.

Then we install ruamel.yaml. <https://pypi.org/project/ruamel.yaml/> 
This is a python yaml module that is more updated the PyYaml.

From there it's pretty basic python.
Send a request for the bookmarks xml, parse xml for links and regex, then download the torrent files. 

Next up is IMDB lookups!

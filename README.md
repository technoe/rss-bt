rss
===

This is a super simple image with a super simple python script designed to automatically
pull my bookmarked rss feeds. I currently have it running on a 5m schedule.

I mount the *watch* dir from my transmissionbt service to the *watch* directory here. Now I can simply download the links locally and let the auto-watch feature do its job.

This run as a one time use service

Now with a more flexible config file start! See example below

Usage
===

```code
docker run -d -v $PWD/watch:/watch/ minoe:rss
```

```yaml
version: "3.7"
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

```yaml
feeds:
  - feed:
      url: https://...com
      # regex: coming soon
  - feed:
      url:
```

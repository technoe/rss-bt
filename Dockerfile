FROM ubuntu:20.04

RUN apt-get update; apt-get upgrade -y; \
    apt-get install -y python3 python3-pip

RUN pip3 install requests ruamel.yaml --upgrade

RUN mkdir /rss

COPY rss/ /rss

ENTRYPOINT [ "/rss/main.py" ]

VOLUME [ "/watch" ]

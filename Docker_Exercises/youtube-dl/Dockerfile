FROM ubuntu:16.04

WORKDIR /videos

ENV LC_ALL=C.UTF-8

RUN apt-get update
RUN apt-get install -y curl python ca-certificates
RUN curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl && chmod a+x /usr/local/bin/youtube-dl
RUN apt-get purge -y --auto-remove curl && rm -rf /var/lib/apt/lists/* && useradd -m downloader

USER downloader

ENTRYPOINT ["/usr/local/bin/youtube-dl"]
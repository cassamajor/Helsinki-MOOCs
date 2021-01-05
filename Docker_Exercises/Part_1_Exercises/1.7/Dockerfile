FROM ubuntu:16.04

WORKDIR app

RUN apt-get update && apt-get install curl -y

COPY script.sh .

ENTRYPOINT ["bash"]
CMD ["script.sh"]

# docker build -t curler . && docker run -t -i curler
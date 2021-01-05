FROM node:10

EXPOSE 5000

WORKDIR app

RUN git clone https://github.com/docker-hy/frontend-example-docker && \
    npm install frontend-example-docker && \
    rm -rf frontend-example-docker

CMD ["npm", "start"]

# docker image build -t frontend-exercise:3.1 . && docker container run -p 5000:5000 --name frontend-example -d --rm frontend-exercise:3.1
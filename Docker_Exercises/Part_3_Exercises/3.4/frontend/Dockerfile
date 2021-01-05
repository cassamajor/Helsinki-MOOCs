FROM node:10

EXPOSE 5000

WORKDIR frontend

RUN git clone https://github.com/docker-hy/frontend-example-docker && \
    npm install frontend-example-docker && \
    rm -rf frontend-example-docker && \
    useradd -m frontend && chown -R .

USER frontend

CMD ["npm", "start"]

# docker image build -t frontend-exercise:3.4 . && docker container run -p 5000:5000 --name frontend-example -d --rm frontend-exercise:3.4
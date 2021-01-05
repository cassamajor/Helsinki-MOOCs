FROM node:10

EXPOSE 5000

RUN git clone https://github.com/docker-hy/frontend-example-docker
WORKDIR frontend-example-docker
RUN npm install

CMD ["npm", "start"]

# docker image build -t frontend-exercise:1.10 . && docker container run -p 5000:5000 --name frontend-example -d --rm frontend-exercise:1.10
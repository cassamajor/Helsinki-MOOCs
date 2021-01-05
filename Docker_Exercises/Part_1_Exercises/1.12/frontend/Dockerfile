FROM node:10

EXPOSE 5000

RUN git clone https://github.com/docker-hy/frontend-example-docker
WORKDIR frontend-example-docker
RUN npm install

ENV API_URL=http://localhost:8000

CMD ["npm", "start"]

# docker image build -t backend-exercise:12 . && docker container run -p 5000:5000 --name frontend-example -d --rm backend-exercise:12
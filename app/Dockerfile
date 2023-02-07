# Common node machine
FROM node:lts as node-base

RUN apt-get update && \
    apt-get install -y ghostscript graphicsmagick wget unoconv libxml2-dev ffmpeg python-is-python3


WORKDIR /usr/src/app
COPY /package*.json ./

# Test Stage
FROM node-base as test

RUN npm install
COPY . .

CMD [ "npm", "run", "serve" ]

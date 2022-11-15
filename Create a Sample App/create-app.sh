#!/bin/bash

mkdir app

cat << EOT >> app/Dockerfile
RUN pip install flask
COPY  ./static /home/ubuntu/static/
COPY  ./templates /home/ubuntu/templates/
COPY  sample-app.py /home/ubuntu/
EXPOSE 8080
CMD python /home/ubuntu/sample-app.py
EOT

cd app
docker build -t sampleapp .
docker stop samplerunning
docker rm samplerunning
docker run -t -d -p 8000:8080 --name samplerunning sampleapp
docker ps -a
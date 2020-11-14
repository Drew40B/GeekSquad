#!/bin/bash
app="docker.test"
docker rm -f ${app}
docker build -t ${app} --network host .

docker run -d -p 56733:80 \
  --name=${app} \
  --network="br0" \
  -v $PWD:/app  \
  ${app}

sleep 10s
curl http://localhost:56733
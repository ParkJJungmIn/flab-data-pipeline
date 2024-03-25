#!/bin/bash

mkdir -p "$(pwd)/data"
mkdir -p "$(pwd)/examples"

# 도커 파일 빌드 후 
docker run -it \
  -v "$(pwd)/data:/opt/eventsim/data" \
  -v "$(pwd)/examples:/opt/eventsim/examples" \
  eventsim \
    -c "/opt/eventsim/examples/example-config.json" --from 365 --nusers 30000 --growth-rate 0.30 /opt/eventsim/data/fake.json

#!/bin/bash

docker rm ec3-cloud-users; \
docker run --privileged --rm -ti \
-h isabella \
-e ZDOTDIR="/mnt" \
--log-driver json-file --log-opt max-size=10m \
-v /dev/log:/dev/log \
-v /etc/localtime:/etc/localtime:ro \
-v $HOME:/mnt \
-v /home/daniel/my_work/srce/git.isabella-users/isabella-users/:/root/isabella-users \
--name ec3-cloud-users \
ipanema:5000/ec3-cloud-users /bin/zsh

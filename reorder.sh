#!/bin/bash
sudo docker rm -f reorder
echo Inter-Docker user: $USER
sudo docker run -v $HOME/apps/reorder/hostfiles/:/hostfiles -p 3000:3000/udp -p 3005:3005/tcp --name="reorder" --network="split" --ip="10.0.10.4" --privileged -i -t  pmw1/reorder

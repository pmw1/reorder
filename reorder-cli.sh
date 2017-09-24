!/bin/bash
sudo docker rm -f reorder-cli
echo Inter-Docker user: $USER
sudo docker run -v $HOME/apps/reorder/hostfiles/:/hostfiles -p3000:3000/udp -p3005:3005 --name="reorder-cli" --network="split" --ip="10.0.10.4" --entrypoint="/bin/bash" --privileged -i -t  pmw1/reorder

#!/usr/bin/python3

import sys
import random
import os

####### Parse input arguments into variables  ##############

if __name__ == "__main__":
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('--force',   '-f', help="Force existing docker to close and run again")
	parser.add_argument('--destroy', '-d', help="Destroy the direct-send container")
	parser.add_argument('--port', '-p', help="Define port number")
	## Replicate above line to add more optional input arguments
	
	args = parser.parse_args()
	print()



	##### CHECK FORCE AND DESTROY
	if(args.force=='1'):
		bashCommand="sudo docker rm -f comms-server"
		os.system(bashCommand)
		print('Force kill container and re-run')

	if(args.destroy=='1'):
		print("Destroying container: comms-server")
		bashCommand="sudo docker rm -f comms-server"
		os.system(bashCommand)
		quit()

	if(args.port is not None):
		port=args.port
		print('Port override. Mapping {}'.format(port))
	else:
		port="64738"
		print('Using default port: {}'.format(port))








######## END Processing input args into variables ############




def initiateObeDockerTemp():

	print('Initiating Comms Server Docker')

	from subprocess import call
	import stat

	comms_server_start_docker = open("hostfiles/start-docker.sh", "wb")

	comms_server_start_docker.write(bytes("#!/bin/bash\n", 'UTF-8'))
	comms_server_start_docker.write(bytes("docker run ", 'UTF-8'))
	comms_server_start_docker.write(bytes("--name=\"comms-server\" ", 'UTF-8'))
	comms_server_start_docker.write(bytes("-v /home/kevin/py-apps/comms-server/hostfiles:/home/default/hostfiles ", 'UTF-8'))
	comms_server_start_docker.write(bytes("-v /home/kevin/recorded-video:/home/default/recorded-video ", 'UTF-8'))
	comms_server_start_docker.write(bytes("--privileged -i -t -d ", 'UTF-8'))
	comms_server_start_docker.write(bytes("-p {}:{}/udp ".format(port, port), 'UTF-8'))
	comms_server_start_docker.write(bytes("-p {}:{} ".format(port, port), 'UTF-8'))
	##comms_server_start_docker.write(bytes("--entrypoint=\"/bin/bash\" ", 'UTF-8'))
	comms_server_start_docker.write(bytes("--device /dev/blackmagic/io0 ", 'UTF-8'))
	comms_server_start_docker.write(bytes("pmw1/comms-server ", 'UTF-8'))

	comms_server_start_docker.close()

	##os.chmod('hostfiles/start-docker.sh', stat.S_IXOTH)

	call(['bash', 'hostfiles/start-docker.sh'])










initiateObeDockerTemp()






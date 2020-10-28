import socket
import time
import threading
import argparse
startTime = time.time()

parser = argparse.ArgumentParser("Usage: port_scanner.py -t TARGET -sp [START_PORT] -ep [END_PORT]")
parser.add_argument("-t","--target",required = True)
parser.add_argument("-sp","--start-port")
parser.add_argument("-ep","--end-port")
args = parser.parse_args()
target = args.target
start_port = int(args.start_port)
end_port = int(args.end_port)

#t_IP = socket.gethostbyname(target)
print ('Starting scan on host: ', target)

def scan_port(port):

		#print ('Scanning Port:', port)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		s.settimeout(5)
		conn = s.connect_ex((target, port))
		if(conn == 0) :
			print('Port %d: OPEN' %port)
		s.close()


for i in range(start_port, end_port+1):
	
	thread = threading.Thread(target = scan_port, args = (i,))
	thread.daemon = True
	thread.start()

print('Time taken:', time.time() - startTime)
exit()

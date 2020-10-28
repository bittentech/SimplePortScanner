import socket
import time
import threading

startTime = time.time()


start_port = 10
end_port = 1000

#t_IP = socket.gethostbyname(target)
target = input("Enter your target IP/Hostname")
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
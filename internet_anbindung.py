import socket
import json
import time

IP = "192.168.2.46"
PORT = 50005

def send_data(data):

	print(type(data))
	print(data)

	jmes = json.dumps(data, indent=4)

	print(type(jmes))
	print(jmes)

	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((IP, PORT))
		# HIER AENDERN!!!
		sock.send(jmes.encode('utf-8'))
		time.sleep(0.1)
		#wait for received data
		jrdata = sock.recv(1024)
		print("received: ", jrdata)
		data = json.loads(jrdata)
		print("converted: ", data)
		sock.close()
	except Exception as error:
		print("Opps, something is wrong: ", error)
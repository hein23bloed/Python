#!/usr/bin/python3

import socket, sys, time

HOST = ""
PORT = 23532

def sstart():
	reply = "Pong"
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Socket created!")

	try:
		sock.bind((HOST, PORT))		
	except socket.error as msg:
		print("Bind failed. Error Code: " + str(msg))
	print("Socket bind complete!")

	sock.listen(10)
	print("Listing...")

	while 1:
		(conn, addr) = sock.accept()
		print(time.strftime("%d.%m.%y %H:%M:%S ") + "Connection from: " + addr[0] + ":" + str(addr[1]))
		try:
			data = conn.recv(1024).decode("iso-8859-1")
		except socket.error as msg:
			print("Error getting data")
			continue
		if data == "Ping":
			print(time.strftime("%d.%m.%y %H:%M:%S ") + "Getting: " + data)
			if not data:
				print("Connection lost!")
				
				socket.close()
			print(time.strftime("%d.%m.%y %H:%M:%S ") + "Sending: " + reply)
			conn.send(reply.encode("iso-8859-1"))
		else:
			print("missing ping")
			continue
		data = conn.recv(1024).decode("iso-8859-1")
		if data == "Ok":
			print(time.strftime("%d.%m.%y %H:%M:%S ") + "Connected: " + addr[0] + ":" + str(addr[1]))
			read_comming(conn)
		else:	
			print("missing ok")
			return 0
	return (1, sock, conn)

def read_comming(conn):
	while 1:
		try:
			data = conn.recv(1024).decode("iso-8859-1")
			print(data)
		except socket.error as msg:
			print("read error")
		
	
def main(argv):
	r, s = sstart()
	s.close()
if __name__ == "__main__":
	main(sys.argv)

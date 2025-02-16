import socket 
import threading

class Server():
	def __init__(self):
		self.HEADER = 64
		self.FORMAT = "utf-8"
		self.all_clients = []	
		self.s = self.crate_socket_connection()
		self.socket_listen_connection(self.s)

	def header_space(self,msg):
		header = 64
		msg_length = len(msg)
		used_header_space = len(str(msg_length))

		print(f"{msg_length}{'-'* (header - used_header_space)}")
		header_with_tie_dash = f"{msg_length}{'-'* (header - used_header_space)}"
		
		return header_with_tie_dash

	def handle_client_send(self, client, addr):
		while True:
			msg = input()
			msg_length = len(msg)
			msg_length_info = self.HEADER - len(str(msg_length))

			client.send(f"{msg_length}{'-' * msg_length_info}".encode(self.FORMAT))
			client.send(msg.encode(self.FORMAT))

	def handle_client(self,client, addr):
		while True:
			
			msg_length = client.recv(self.HEADER).decode(self.FORMAT)
			msg_length = msg_length.replace("-", "")

			if not msg_length:
				client.close()
				break
			else:
				msg_length = int(msg_length)
				mld = client.recv(msg_length).decode(self.FORMAT)
				print(mld)

				
		print("lost conection")


	

	def socket_listen_connection(self, s):
		s.listen()
		print()

		while True:
			client, addr = s.accept()
			print(f"kobling {addr[0]}")


			TH = threading.Thread(target= self.handle_client, args=(client, addr))
			TH_send = threading.Thread(target= self.handle_client_send, args=(client, addr))
			TH.start()
			TH_send.start()
			print(f"active threades, {threading.active_count() - 1}")#teller antall koblinger 
		

	def crate_socket_connection(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print("[generet socket]")
		port = 12346
		host = ""  
		
		s.bind((host, port))
		print("[kobinert socket med host og ip]")

		return s



Server()
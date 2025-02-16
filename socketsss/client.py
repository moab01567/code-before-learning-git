import socket
import threading


class Start_kobling():
	
	def __init__(self):
		self.header = 64
		self.format = "utf-8"
		self.s = self.kobling()
		
		#lager to threads en for å sende og en for å motta
		TH_send = threading.Thread(target= self.send_til_server, args=(self.s,))

		TH_motta = threading.Thread(target= self.motta_fra_server, args=(self.s,)) 
		TH_send.start()
		print("sendings thread OK!")
		TH_motta.start()
		print("mottaker thread OK!")



	def kobling(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(("ip", 12346))
		return s

	def header_space(self,msg):
		header = 64
		msg_length = len(msg)
		used_header_space = len(str(msg_length))

		print(f"{msg_length}{'-'* (header - used_header_space)}")
		header_with_tie_dash = f"{msg_length}{'-'* (header - used_header_space)}"
		
		return header_with_tie_dash
	
	def send_til_server(self, s):
		while True:
			mld = input(">")
			
			if not mld:
				break
				s.close()
			else:
				
				used_header = self.header_space(mld)
				s.send(used_header.encode(self.format))

				s.send(mld.encode(self.format))

	def motta_fra_server(self, s):
		while True:
			meld_length = s.recv(self.header).decode(self.format)
			meld_length = int(meld_length.replace("-", ""))

			mld = s.recv(meld_length).decode(self.format)
			print(mld)

			


				


server = Start_kobling()


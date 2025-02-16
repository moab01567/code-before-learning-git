import socket
import pickle
import threading
import datetime
import mysql.connector

class Start_server():
	def __init__(self):
		self.header = 64
		self.port = 12347
		self.host = "" 
		s = self.kobling()
		self.set_server_listen_mode(s)


	def kobling(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print("lager kommunikasjonskanal til serveren")
		s.bind((self.host, self.port))
		print("Serveren er koblet til kanalen")
		
		return s

	def set_server_listen_mode(self, s):
		s.listen()
		print("satt på høre modus")

		print("venter på koblinger")
		self.HC = Handle_clients(self.header)


		while True:
			client, addr = s.accept()
			
			TH = threading.Thread(target= self.HC.main, args=(client, addr))
			TH.start()
			continue


			msg_length = client.recv(self.header).decode("utf-8")
			msg_length = self.remove_tie_dash(msg_length)
			msg = client.recv(int(msg_length)).decode("utf-8")
			print(msg)

			msg_length = client.recv(self.header).decode("utf-8")
			msg_length = self.remove_tie_dash(msg_length)
			msg = client.recv(int(msg_length))
			
			info = pickle.loads(msg)
			print(info)
			print(info["first_name"])

class Database_operation():
	def __init__(self):
		self.mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		password="Rehman5724",
		database="meldinger")
		print(self.mydb)


	def add_user_to_database(self, user_info):
		now = datetime.datetime.now()
		now = str(now)[0:10]
		mycursor = self.mydb.cursor()
		sql = f"INSERT INTO users(first_name, last_name, user_name, tlf, account_made) VALUES (%s, %s, %s, %s, %s)"
		val = (f"{user_info['first_name']}", f"{user_info['last_name']}",f"{user_info['user_name']}",f"{user_info['tlf']}",f"{now}")
		mycursor.execute(sql, val)

		self.mydb.commit()

		print(mycursor.rowcount, "record inserted.")

	def check_user_in_database(self, msg):
		mycursor = self.mydb.cursor()
		msg = int(msg)
		sql = f"SELECT * FROM users WHERE user_id = {msg}"

		mycursor.execute(sql)

		myresult = mycursor.fetchall()
		print(myresult)
		return myresult


class Handle_clients():
	def __init__(self, header):
		self.header = header
		self.data_opera = Database_operation()
		

	def header_space(self, msg):
		msg_length = len(msg)
		used_header_space = len(str(msg_length))

		print(f"{msg_length}{'-'* (self.header - used_header_space)}")
		header_with_tie_dash = f"{msg_length}{'-'* (self.header - used_header_space)}"
		
		return header_with_tie_dash
	

	def remove_tie_dash(self, msg_length):
		print(msg_length)
		removed_tiedash_msg_length = msg_length.replace("-", "")
		print(removed_tiedash_msg_length)

		return removed_tiedash_msg_length
	
	def meny(self,  client):
		self.where = "DU befinner deg på nå hoved menyen\n trykk '1' for å se dine chatter "
		self.where = pickle.dumps(self.where)

		client.send(self.header_space(self.where).encode("utf-8"))
		client.send(self.where)
		
		while True:
			msg_length = client.recv(self.header).decode("utf-8")
			msg_length = self.remove_tie_dash(msg)
			msg = client.recv(msg_length)
			msg = pickle.loads(msg)
			
			if msg == "1":
				pass
			elif msg == "hvor":
				client.send(self.header_space(self.where).encode("utf-8"))
				client.send(self.where)
			else:
				continue




	
	def main(self, client, addr):
		msg_length = client.recv(self.header).decode("utf-8") 
		msg_length = self.remove_tie_dash(msg_length)
		msg = client.recv(int(msg_length))
		msg = pickle.loads(msg)

		info_list = self.data_opera.check_user_in_database(msg)
		
		if msg == "100":
			msg_length = client.recv(self.header).decode("utf-8") 
			msg_length = self.remove_tie_dash(msg_length)
			msg = client.recv(int(msg_length))
			msg = pickle.loads(msg)
			
			self.data_opera.add_user_to_database(msg)
		
		elif info_list:
			self.meny(client)
		else:
			print("")
			client.close()

		client.close()




Start_server()








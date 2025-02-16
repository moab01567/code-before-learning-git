import tkinter as tk
from tkinter import filedialog
import socket
class server:
	def __init__(self):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	
		self.s.connect((socket.gethostbyname('localhost'), 1234))

	def send_info(self, path):
		self.path = open(path, "wb")
		self.s.send(self.path.read())

		while True:
			msg = self.s.recv(4)
			msg = msg.decode("utf-8")
			if len(msg) <= 0:
				break
			print(msg)
			

class vindu:
	def __init__(self, master):
		master.geometry("400x450")
		master.maxsize(400,450)
		master.minsize(400,450)

		self.bekreft = tk.Button(master, text = "Bekreft", width=30, 
								command= self.start).pack(side="top",pady = 20)



	def start(self):
		self.path = tk.filedialog.askopenfile().name
		info = server()
		info.send_info(self.path)




if __name__ == "__main__":
	root = tk.Tk()
	frame = vindu(root)
	root.mainloop()
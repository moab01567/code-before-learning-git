import tkinter as tk
from tkinter import filedialog
from tkinter import Scrollbar



class Vindu:

	def __init__(self, master):
		master.geometry("400x450")
		master.maxsize(400,450)
		master.minsize(400,450)
		master.title("booking")
		self.master = master

		self.overskrift = tk.Label(master, text= "booking",
			font=("Times New Roman",30)).pack()


		self.tekst_mAned = tk.Label(master,text="Måned: ",
                 font=("Times New Roman",20)).place(x = 3, y = 39)

		self.skriv_mAned = tk.Entry()
		self.skriv_mAned.pack(side="top", pady=1)


		self.tekst_Ar = tk.Label(master, text= "År:", 
			font= ("Times New Roman", 20)).place(x = 3, y = 63)

		self.skriv_Ar = tk.Entry()
		self.skriv_Ar.pack(side="top", pady= 1)
		
		scrollbar = Scrollbar(root)
		scrollbar.pack()
	


if __name__ == "__main__":
	root = tk.Tk()
	frame = Vindu(root)
	root.mainloop()

class Computer():
	def __init__(self, type_computer ):
		self.type_computer = type_computer

	def config(self):
		print("i5, 16gb, 1TB")
		print(self.type_computer)

com1 = Computer("mac")
com2 = Computer("IOS") 

com1.config()
com2.config()







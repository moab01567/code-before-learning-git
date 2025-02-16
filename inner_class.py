

class Student:
	def __init__(self,name,nr):
		self.name = name
		self.nr = nr
		self.lap = self.Laptop()

	def show(self):
		print(self.name, self.nr)


	class Laptop():
		def __init__(self):
			self.brand = "HP"
			self.cpu = "i5"
			self.ram = 8

		def show(self):
			print(self.brand, self.cpu, self.ram)


s1 = Student("mohemmed", 1)
s1.show()
s1.lap.show()


lap1 = Student.Laptop()


print(id(s1))
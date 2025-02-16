
registrert_brukere = {}
kontoer = {}


class Vindu:

	def innlogget_vindu(self, bruker):
		print(f"Hei, {bruker.fornavn}")
		
		funksjon = {
    		"1": saldo,
   			"2": bankoverføring,
   			"3": innskudd,
   			"4": uttak,
   			"5": endre_password,
   			"6": loggut
   			}
		
		while True:
			print("\ttast 1 for saldo")
			print("\ttast 2 for bankoverføring")
			print("\ttast 3 for innskudd")
			print("\ttast 4 for uttak")
			print("\ttast 5 for endre password")
			print("\ttast 6 for loggut")
			tast = input("tast: ")
			
			if tast == "6":
				break
			
			try:
				utfør_tast = funksjon[tast]()
			except KeyError:
				continue


	
	def main_vindu(self):
		bruker = Person("Mohemmed","Abdulriza","0820384302", "m") 
		registrert_brukere["08020384302"] = bruker
		while True:
			personnummer = input("Personnummer: ")
			try:
				bruker = registrert_brukere[personnummer]
				perssord = input("Passord: ")
			except KeyError:
				continue


			if bruker.passord == perssord:
				self.innlogget_vindu(bruker)

			else:
				continue




class Person:
	def __init__(self, fornavn, etternavn, personNR, passord):
		self.fornavn = fornavn
		self.etternavn = etternavn
		self.personNR = personNR
		self.passord = passord
		self.list_kontoNR = []


class KontoNR(Person):
	def __init__(self):
		super().__init__(fornavn, etternavn, personNR)





start = Vindu()
start.main_vindu()





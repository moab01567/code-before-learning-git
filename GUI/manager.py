from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
import threading
import time
brukere = {"mo":"mo"}



class LoginWindow(Screen):
	brukernavn = ObjectProperty(None)
	passord = ObjectProperty(None)

	def login_btn(self):
		print(self.brukernavn.text)
		print(self.passord.text)
		
		if self.brukernavn.text in brukere.keys():
			if self.passord.text == brukere[self.brukernavn.text]:
				MainWindow.bruker = self.brukernavn.text
				sm.current = "Main"
				self.brukernavn.text = ""
				self.passord.text = ""
			
			else:
				self.brukernavn.text = ""
				self.passord.text = ""
		else:
			self.brukernavn.text = ""
			self.passord.text = ""



	def create_btn(self):
		sm.current = "Create"
	

class MainWindow(Screen):
	brukernavn = ObjectProperty(None)
	grids = ObjectProperty(None)
	bruker = ""
	side = 1
	info = []
	info_dict = {}

	def on_enter(self, *args):
		self.legg_side_tall()
		self.brukernavn.text = "du er nå logget in som " + self.bruker


	def logut(self):
		sm.current = "Login"
	

	def legg_side_tall(self): 

		for i in range(1, 100): 
			lab = Label(text=str(i),color= (0,0,0,1))
			self.info.append(lab)

		print(self.info)
		print()
		lille_liste = []
		antall = 1
		for i in self.info:
			lille_liste.append(i)
			
			if len(lille_liste) == 10:
				self.info_dict[antall] = lille_liste
				lille_liste = []
				antall += 1
			
			else:
				continue

		self.info_dict[antall] = lille_liste
		print(self.info_dict)

	def utfore_vis_liste(self, bruker):
		
		for i in self.info_dict[self.side]:
			self.grids.add_widget(i)

	
	def sett_noverende_liste(self, bruker):

		for i in self.info_dict[self.side]:
			self.grids.remove_widget(i)
		
	
	def vis_liste(self):
		TH = threading.Thread(target= self.utfore_vis_liste, args=(self.bruker,))
		TH.start()

	def slett_vis_liste(self):
		TH = threading.Thread(target= self.sett_noverende_liste, args=(self.bruker,))
		TH.start()


	def tilbake_liste(self):
		if self.side <= 1:
			self.slett_vis_liste()
			self.side = 1
			self.vis_liste()
		
		else:
			self.slett_vis_liste()
			self.side -= 1
			self.vis_liste()

	def fram_liste(self):
		
		if self.side >= len(self.info_dict.keys()):
			self.slett_vis_liste()
			self.side = len(self.info_dict.keys())
			self.vis_liste()

		else:
			self.slett_vis_liste()
			self.side += 1
			self.vis_liste()
		




class CreateWindow(Screen):
	brukernavn = ObjectProperty(None)
	passord = ObjectProperty(None)


	def create_user_btn(self):
		print(self.brukernavn.text)
		print(self.passord.text)
		brukere[self.brukernavn.text] = self.passord.text
		self.brukernavn.text = ""
		self.passord.text = ""
		print(brukere)




class WindowManager(ScreenManager):
	pass

kv = Builder.load_file("manag_style.kv")

sm = WindowManager()

screens = [LoginWindow(name="Login"), CreateWindow(name="Create"), MainWindow(name="Main")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "Login"


class testApp(App):
	def build(self):
		return sm


if __name__ == "__main__":
	testApp().run()
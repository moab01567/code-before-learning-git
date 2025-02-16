from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen


#import inspect
#src = inspect.getsource(module)



			
class Login_window(Widget):
	brukernavn = ObjectProperty(None)
	passord = ObjectProperty(None)

	def btn(self):
		print(self.brukernavn.text)
		print(self.passord.text)
		self.brukernavn.text = ""
		self.passord.text = ""



class second_window(Widget):
	brukernavn = ObjectProperty(None)
	passord = ObjectProperty(None)

	def btn(self):
		print(self.brukernavn.text)
		print(self.passord.text)
		self.brukernavn.text = ""
		self.passord.text = ""




class GUI_learnApp(App):
	def build(self):
		return Login_window()
		




if __name__ == "__main__":
	GUI_learnApp().run()



	
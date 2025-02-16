from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        # Create a label
        self.label = Label(text="Hello, World!")

        # Create a button
        button = Button(text="Update label")

        # Bind the update_label function to the button press event
        button.bind(on_press=self.update_label)

        # Return the label and button
        return self.label, button

    def update_label(self, instance):
        # Update the label text
        self.label.text = "Hello, Kivy!"

if __name__ == "__main__":
    MyApp().run()
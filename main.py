import kivy
kivy.require("2.2.1")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from webview import WebView


class MyApp(App):
    def build(self):
        self.browser = None
        self.label = Label(text="")
        button1 = Button(text="Go to Google", on_press=self.view_google)
        box = BoxLayout(orientation="vertical")
        box.add_widget(button1)
        box.add_widget(self.label)
        return box

    def view_google(self, button):
        self.browser = WebView("https://www.google.com")


if __name__ == "__main__":
    MyApp().run()

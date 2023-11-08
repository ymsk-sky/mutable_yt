import webbrowser

import kivy
kivy.require("2.2.1")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget


class MyApp(App):
    def build(self):
        # UIレイアウト定義
        layout = BoxLayout(orientation="vertical")
        # webページのURL入力用テキストフィールド
        url_input = TextInput(hint_text="Enter URL", multiline=False)
        # URL開くボタン
        open_button = Button(text="GO", on_press=self.open_url)
        # WebView表示用のウィジェット
        webview = Label(text="web content here", markup=True)

        layout.add_widget(url_input)
        layout.add_widget(open_button)
        layout.add_widget(webview)

        return layout

    def open_url(self, instance):
        url_input = self.root.children[-1]  # TextInput
        webview = self.root.children[0]  # WebView

        url = url_input.text
        if url:
            webview.text = f"[ref={url}]{url}[/ref]"
            webbrowser.open(url)


if __name__ == "__main__":
    MyApp().run()

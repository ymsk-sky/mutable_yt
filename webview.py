from kivy.uix.modalview import ModalView


class WebView(ModalView):
    def __init__(self, url, **kwargs):
        super().__init__(**kwargs)
        self.url = url
        self.webview = None
        self.open(url)

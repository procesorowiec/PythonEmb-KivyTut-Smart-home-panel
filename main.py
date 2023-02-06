
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class MainScreen(BoxLayout):
    pass


class KivyApp(App):
    def build(self):
        return MainScreen()


kv_app = KivyApp()
kv_app.run()

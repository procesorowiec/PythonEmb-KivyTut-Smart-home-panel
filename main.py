
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class MainScreen(BoxLayout):
    pass


class TMonitorApp(App):
    def build(self):
        return MainScreen()


kv_app = TMonitorApp()
kv_app.run()

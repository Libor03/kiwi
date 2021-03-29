from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder

class Menu(Screen):
    pass

class Auth(Screen):
    pass


class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")

class MyApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    MyApp().run()


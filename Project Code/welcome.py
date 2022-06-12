from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput


# This is the welcome screen, which user will see when opening the app

KV = '''
#: import Window kivy.core.window.Window

<Welcome>:
    GridLayout:
        cols: 1
        size: Window.size
        padding: (0,0,0,0)

        canvas:
            Color:
                rgba: 0.85,0.85,0.85, 1
            Rectangle:
                pos: self.pos
                size: self.size

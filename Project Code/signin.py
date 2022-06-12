from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput


# This is the profile creation screen, which user will see after opening the app

KV = '''
#: import Window kivy.core.window.Window

<Create_prof>:
    GridLayout:
        cols: 1
        size: Window.size
        padding: (0,0,0,0)
        spacing: 1

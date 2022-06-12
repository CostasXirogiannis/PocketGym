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
        Label:
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            text: 'PocketGym'
            color: 0.15,0.12,0.54, 2
            halign: 'center'
            font_size: '34sp'
            size_hint: 1, 0.1
        
        BoxLayout:
            orientation: 'vertical'
            size_hint: 1, 0.9
            padding: (5,5,5,5)

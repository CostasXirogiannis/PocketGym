from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


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

        PGScreenSelector:
'''

Builder.load_string(KV)


# Methods that are being used by the welcome screen

class Welcome(Screen):

    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app


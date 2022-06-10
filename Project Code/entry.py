from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

KV = '''
#: import Window kivy.core.window.Window

<Entry>:
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
            color: 0.15,0.12,0.54, 1
            halign: 'center'
            font_size: '34sp'
            size_hint: 1, 0.1

       
        PGScreenSelector:
'''

Builder.load_string(KV)


class Entry(Screen):

    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app

    def on_profile(self):
        print('You hit profile')

    def on_history(self):
        print('You hit history')
        self.app.manager.current = 'history'

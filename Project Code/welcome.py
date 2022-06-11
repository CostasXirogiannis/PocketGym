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
            color: 0.15,0.12,0.54, 1
            halign: 'center'
            font_size: '34sp'
            size_hint: 1, 0.1
        
        BoxLayout:
            orientation: 'vertical'
            size_hint: 1, 0.9
            padding: (5,5,5,5)

            canvas:
                Color:
                    rgba: 0.95,0.95,0.95, 0.5
                Rectangle:
                    pos: self.pos
                    size: self.size
            Label:
                pos_hint: {'center_x': 0.5, 'center_y': 0.2}
                text: 'Welcome!'
                color: 0.15,0.12,0.54, 1
                halign: 'center'
                text_size: self.size
                font_size: '20sp'
                size_hint: 1, 0.1

            GridLayout:
                cols: 2
                size_hint: 1, 0.3
                padding: (0,0,0,0)
                
                canvas:
                    Color:
                        rgba: 0.85,0.85,0.85, 1
                    Line:
                        points: self.x, self.y, self.x+self.width,self.y

                Label:
                    pos_hint: {'center_x': 0.1, 'center_y': 0.3}
                    text: 'Εισάγετε Όνομα:'
                    color: 0,0,0, 0.7
                    halign: 'left'
                    text_size: self.size
                    font_size: '15sp'
                    size_hint: 1, 0.1

                TextInput:
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    size_hint: (.2, None)
                    height: 30
                    halign: 'left'
                    multiline: False

                Label:
                    pos_hint: {'center_x': 0.1, 'center_y': 0.4}
                    text: 'Εισάγετε Κωδικό:'
                    color: 0,0,0, 0.7
                    halign: 'left'
                    text_size: self.size
                    font_size: '15sp'
                    size_hint: 1, 0.1

                TextInput:
                    pos_hint: {'center_x': 0.5, 'center_y': 0.4}
                    size_hint: (.2, None)
                    height: 30
                    multiline: False

        PGScreenSelector:
'''

Builder.load_string(KV)


# Methods that are being used by the welcome screen

class Welcome(Screen):

    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app


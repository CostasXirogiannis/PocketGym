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
        spacing: 10

        canvas:
            Color:
                rgba: 0.85,0.85,0.85, 1
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            text: 'Δημιουργία Προφίλ'
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

            GridLayout:
                cols: 2
                padding: (0,20,100,0)
                size_hint: 1, 0.3
                spacing: dp(40)

                canvas:
                    Color:
                        rgba: 0.85,0.85,0.85, 1
                Label:
                    pos_hint: {'center_x': 0.1, 'center_y': 0.2}
                    text: 'Avatar:'
                    color: 0,0,0, 0.7
                    halign: 'right'
                    valign: 'center'
                    text_size: self.size
                    font_size: '15sp'
                    size_hint: 0.3, 1

                MDIconButton:
                    canvas:
                        Color:
                            rgba: 0.95,0,0, 0.5

                    icon: 'camera-plus-outline'
                    user_font_size: '60sp'
                    valign: 'center'
                    halign: 'center'

                Label:
                    pos_hint: {'center_x': 0.1, 'center_y': 0.3}
                    text: 'Ονομα:'
                    color: 0,0,0, 0.7
                    halign: 'right'
                    text_size: self.size
                    font_size: '15sp'
                    size_hint: 0.3, 1

                MDTextFieldRound:
                    id: name
                    normal_color: .8, .8, .8, .8

                Label:
                    pos_hint: {'center_x': 0.1, 'center_y': 0.4}
                    text: 'Επίθετο:'
                    color: 0,0,0, 0.7
                    halign: 'right'
                    text_size: self.size
                    font_size: '15sp'
                    size_hint: 0.3, 1

                MDTextFieldRound:
                    id: surname
                    normal_color: .8, .8, .8, .8

                Label:
                    pos_hint: {'center_x': 0.1, 'center_y': 0.3}
                    text: 'Ηλικία:'
                    color: 0,0,0, 0.7
                    halign: 'right'
                    text_size: self.size
                    font_size: '15sp'
                    size_hint: 0.3, 1

                MDTextFieldRound:
                    id: name
                    normal_color: .8, .8, .8, .8

                Label:
                    pos_hint: {'center_x': 0.1, 'center_y': 0.4}
                    text: 'Φύλο:'
                    color: 0,0,0, 0.7
                    halign: 'right'
                    text_size: self.size
                    font_size: '15sp'
                    size_hint: 0.3, 1

                MDTextFieldRound:
                    id: surname
                    normal_color: .8, .8, .8, .8

                Label:
                    pos_hint: {'center_x': 0.1, 'center_y': 0.3}
                    text: 'Ύψος:'
                    color: 0,0,0, 0.7
                    halign: 'right'
                    text_size: self.size
                    font_size: '15sp'
                    size_hint: 0.3, 1

                MDTextFieldRound:
                    id: name
                    normal_color: .8, .8, .8, .8

                Label:
                    pos_hint: {'center_x': 0.1, 'center_y': 0.4}
                    text: 'Βάρος:'
                    color: 0,0,0, 0.7
                    halign: 'right'
                    text_size: self.size
                    font_size: '15sp'
                    size_hint: 0.3, 1

                MDTextFieldRound:
                    id: surname
                    normal_color: .8, .8, .8, .8

        PGScreenSelector:
'''

Builder.load_string(KV)


# Methods that are being used by the create_prof screen

class Create_prof(Screen):

    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app

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
                pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                text: 'Welcome!'
                color: 0.15,0.12,0.54, 1
                halign: 'center'
                text_size: self.size
                font_size: '20sp'
                size_hint: 1, 0.2

            GridLayout:
                cols: 2
                padding: (0,0,100,0)
                size_hint: 1, 0.3
                spacing: dp(40)
                
                canvas:
                    Color:
                        rgba: 0.85,0.85,0.85, 1

                Label:
                    pos_hint: {'center_x': 0.1, 'center_y': 0.3}
                    text: 'Εισάγετε Όνομα:'
                    color: 0,0,0, 0.7
                    halign: 'right'
                    text_size: self.size
                    font_size: '15sp'
                    size_hint: 0.3, 1

                MDTextFieldRound:
                    id: name
                    normal_color: .8, .8, .8, .8

                #TextInput:
                    #pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    #size_hint: (0.7, None)
                    #height: 30
                    #halign: 'left'
                    #multiline: False

                Label:
                    pos_hint: {'center_x': 0.1, 'center_y': 0.4}
                    text: 'Εισάγετε Κωδικό:'
                    color: 0,0,0, 0.7
                    halign: 'right'
                    text_size: self.size
                    font_size: '15sp'
                    size_hint: 0.3, 1

                MDTextFieldRound:
                    id: password
                    icon_right: "key"
                    helper_text: "Password"
                    password: True
                    normal_color: .8, .8, .8, .8

                #TextInput:
                    #pos_hint: {'center_x': 0.5, 'center_y': 0.4}
                    #size_hint: (.7, None)
                    #height: 30
                    #halign: 'left'
                    #multiline: False
                    
            BoxLayout:
                spacing: 10
                size_hint: 1, 0.5
                
                canvas:
                    Color:
                        rgba: 0.85,0.85,0.85, 1

                MDIconButton:
                    canvas:
                        Color:
                            rgba: 0.95,0,0, 0.5

                    icon: 'information-outline'
                    user_font_size: '30sp'
                    valign: 'center'

                #Label:
                    #canvas:
                        #Color:
                            #rgba: 0,0.95,0, 0.5

                    #text: 'About'
                    #color: 0,0,0, 0.7
                    #halign: 'center'
                    #font_size: '20sp'
                    #size_hint: 0.7, 1
                    #pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        PGScreenSelector:
'''

Builder.load_string(KV)


# Methods that are being used by the welcome screen

class Welcome(Screen):

    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app


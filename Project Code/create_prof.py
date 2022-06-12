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

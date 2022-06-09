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
            color: 0.8,0.3,0.9, 1
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

            BoxLayout:
                spacing: 10

                canvas.before:
                    Color:
                        rgba: 0.85,0.85,0.85, 1
                    Line:
                        points: self.x, self.y, self.x+self.width,self.y

                orientation: 'horizontal'
                MDIconButton:
                    icon: 'account-outline'
                    md_bg_color: (0,0,0,0.1)
                    user_font_size: '20sp'
                    pos_hint: {'center_x': 0.05, 'center_y': 0.5}

                Label:
                    text: '[ref=koko]Προφίλ[/ref]'
                    markup: True
                    color: 0,0,0, 0.7
                    text_size: self.size
                    size_hint: (1, 1)
                    halign: "left"
                    valign: "middle"
                    on_ref_press: root.on_profile()

            BoxLayout:
                spacing: 10

                canvas.before:
                    Color:
                        rgba: 0.85,0.85,0.85, 1
                    Line:
                        points: self.x, self.y, self.x+self.width,self.y

                orientation: 'horizontal'
                MDIconButton:
                    icon: 'plus-thick'
                    md_bg_color: (0,0,0,0.1)
                    user_font_size: '20sp'
                    pos_hint: {'center_x': 0.05, 'center_y': 0.5}

                Label:
                    text: 'Νέα δραστηριότητα'
                    color: 0,0,0, 0.7
                    text_size: self.size
                    size_hint: (1, 1)
                    halign: "left"
                    valign: "middle"

            BoxLayout:
                spacing: 10

                canvas.before:
                    Color:
                        rgba: 0.85,0.85,0.85, 1
                    Line:
                        points: self.x, self.y, self.x+self.width,self.y


                orientation: 'horizontal'
                MDIconButton:
                    icon: 'history'
                    md_bg_color: (0,0,0,0.1)
                    user_font_size: '20sp'
                    pos_hint: {'center_x': 0.05, 'center_y': 0.5}

                Label:
                    text: '[ref=history]Ιστορικό[/ref]'
                    markup: True
                    color: 0,0,0, 0.7
                    text_size: self.size
                    size_hint: (1, 1)
                    halign: "left"
                    valign: "middle"
                    on_ref_press: root.on_history()

            BoxLayout:
                spacing: 10

                canvas.before:
                    Color:
                        rgba: 0.85,0.85,0.85, 1
                    Line:
                        points: self.x, self.y, self.x+self.width,self.y


                orientation: 'horizontal'
                MDIconButton:
                    icon: 'star'
                    md_bg_color: (0,0,0,0.1)
                    user_font_size: '20sp'
                    pos_hint: {'center_x': 0.05, 'center_y': 0.5}

                Label:
                    text: 'Premium'
                    color: 0,0,0, 0.7
                    text_size: self.size
                    size_hint: (1, 1)
                    halign: "left"
                    valign: "middle"

            BoxLayout:
                spacing: 10

                canvas.before:
                    Color:
                        rgba: 0.85,0.85,0.85, 1
                    Line:
                        points: self.x, self.y, self.x+self.width,self.y

                orientation: 'horizontal'
                MDIconButton:
                    icon: 'cog-outline'
                    md_bg_color: (0,0,0,0.1)
                    user_font_size: '20sp'
                    pos_hint: {'center_x': 0.05, 'center_y': 0.5}

                Label:
                    text: 'Ρυθμίσεις'
                    markup: True
                    color: 0,0,0, 0.7
                    text_size: self.size
                    size_hint: (1, 1)
                    halign: "left"
                    valign: "middle"

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

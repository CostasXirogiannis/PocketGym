from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

KV = '''
#: import Window kivy.core.window.Window

<History>:
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

        BoxLayout:
            size_hint: 1, 0.1
            orientation: 'horizontal'
            padding: [10,0,10,0]

            canvas.before:
                Color:
                    rgba: 0.85,0.85,0.85, 1
                Line:
                    points: self.x, self.y, self.x+self.width,self.y

            Label:
                text: 'Ιστορικό'
                color: 0.15,0.12,0.54, 1
                font_size: '34sp'
                text_size: self.size
                size_hint: (1, 1)
                halign: "center"
                valign: "middle"

            MDIconButton:
                icon: 'arrow-left'
                #md_bg_color: (0,0,0,0.1)
                user_font_size: '20sp'
                pos_hint: {'center_x': 0.05, 'center_y': 0.5}
                on_press: root.on_back()

        BoxLayout:
            orientation: 'vertical'
            size_hint: 1, 0.9

            BoxLayout:
                orientation: 'horizontal'
                size_hint: 1, 0.2
                padding: (5,5,5,5)

                canvas:
                    Color:
                        rgba: 0.95,0.95,0.95, 0.5
                    Rectangle:
                        pos: self.pos
                        size: self.size

                    Color:
                        rgba: 0.85,0.85,0.85, 1
                    Line:
                        points: self.x, self.y, self.x+self.width,self.y

                MDIconButton:
                    icon: 'run-fast'
                    #md_bg_color: (0,0,0,0.1)
                    user_font_size: '60sp'
                    pos_hint: {'center_x': 0.05, 'center_y': 0.5}
    
                BoxLayout:
                    spacing: 5
                    orientation: 'vertical'
                    
                    Label:
                        text: '[b]Ημερομηνία:[/b] 08/06/2022'
                        markup: True
                        color: 0,0,0, 0.6
                        text_size: self.size
                        font_size: '16sp'
                        halign: "right"
                        valign: "middle"
                    Label:
                        text: '[b]Διάρκεια:[/b] 1:22:48'
                        markup: True
                        color: 0,0,0, 0.6
                        text_size: self.size
                        font_size: '16sp'
                        halign: "right"
                        valign: "middle"
                    Label:
                        text: '[b]Καύση:[/b] 526 cal'
                        markup: True
                        color: 0,0,0, 0.6
                        text_size: self.size
                        font_size: '16sp'
                        halign: "right"
                        valign: "middle"
            BoxLayout:
                orientation: 'horizontal'
                size_hint: 1, 0.2
                padding: (5,5,5,5)

                canvas:
                    Color:
                        rgba: 0.95,0.95,0.95, 0.5
                    Rectangle:
                        pos: self.pos
                        size: self.size

                    Color:
                        rgba: 0.85,0.85,0.85, 1
                    Line:
                        points: self.x, self.y, self.x+self.width,self.y

                MDIconButton:
                    icon: 'swim'
                    #md_bg_color: (0,0,0,0.1)
                    user_font_size: '60sp'
                    pos_hint: {'center_x': 0.05, 'center_y': 0.5}
                    
                BoxLayout:
                    spacing: 5
                    orientation: 'vertical'
    
                    Label:
                        text: '[b]Ημερομηνία:[/b] 07/06/2022'
                        markup: True
                        color: 0,0,0, 0.6
                        text_size: self.size
                        font_size: '16sp'
                        halign: "right"
                        valign: "middle"
                    Label:
                        text: '[b]Διάρκεια:[/b] 1:02:29'
                        markup: True
                        color: 0,0,0, 0.6
                        text_size: self.size
                        font_size: '16sp'
                        halign: "right"
                        valign: "middle"
                    Label:
                        text: '[b]Καύση:[/b] 267 cal'
                        markup: True
                        color: 0,0,0, 0.6
                        text_size: self.size
                        font_size: '16sp'
                        halign: "right"
                        valign: "middle"
            BoxLayout:
                orientation: 'horizontal'
                size_hint: 1, 0.2
                padding: (5,5,5,5)

                canvas:
                    Color:
                        rgba: 0.95,0.95,0.95, 0.5
                    Rectangle:
                        pos: self.pos
                        size: self.size

                    Color:
                        rgba: 0.85,0.85,0.85, 1
                    Line:
                        points: self.x, self.y, self.x+self.width,self.y

                MDIconButton:
                    icon: 'weight-lifter'
                    #md_bg_color: (0,0,0,0.1)
                    user_font_size: '60sp'
                    pos_hint: {'center_x': 0.05, 'center_y': 0.5}
    
                BoxLayout:
                    spacing: 5
                    orientation: 'vertical'
    
                    Label:
                        text: '[b]Ημερομηνία:[/b] 04/06/2022'
                        markup: True
                        color: 0,0,0, 0.6
                        text_size: self.size
                        font_size: '16sp'
                        halign: "right"
                        valign: "middle"
                    Label:
                        text: '[b]Διάρκεια:[/b] 00:56:17'
                        markup: True
                        color: 0,0,0, 0.6
                        text_size: self.size
                        font_size: '16sp'
                        halign: "right"
                        valign: "middle"
                    Label:
                        text: '[b]Καύση:[/b] 349 cal'
                        markup: True
                        color: 0,0,0, 0.6
                        text_size: self.size
                        font_size: '16sp'
                        halign: "right"
                        valign: "middle"
            BoxLayout:
                orientation: 'horizontal'
                size_hint: 1, 0.2
                padding: (5,5,5,5)
       
                canvas:
                    Color:
                        rgba: 0.95,0.95,0.95, 0.5
                    Rectangle:
                        pos: self.pos
                        size: self.size

                    Color:
                        rgba: 0.85,0.85,0.85, 1
                    Line:
                        points: self.x, self.y, self.x+self.width,self.y

                MDIconButton:
                    icon: 'walk'
                    #md_bg_color: (0,0,0,0.1)
                    user_font_size: '60sp'
                    pos_hint: {'center_x': 0.05, 'center_y': 0.5}
    
                BoxLayout:
                    spacing: 5
                    orientation: 'vertical'
    
                    Label:
                        text: '[b]Ημερομηνία:[/b] 03/06/2022'
                        markup: True
                        color: 0,0,0, 0.6
                        text_size: self.size
                        font_size: '16sp'
                        halign: "right"
                        valign: "middle"
                    Label:
                        text: '[b]Διάρκεια:[/b] 02:03:34'
                        markup: True
                        color: 0,0,0, 0.6
                        text_size: self.size
                        font_size: '16sp'
                        halign: "right"
                        valign: "middle"
                    Label:
                        text: '[b]Καύση:[/b] 233 cal'
                        markup: True
                        color: 0,0,0, 0.6
                        text_size: self.size
                        font_size: '16sp'
                        halign: "right"
                        valign: "middle"
            BoxLayout:
                orientation: 'horizontal'
                size_hint: 1, 0.2
                padding: (5,5,5,5)

                canvas:
                    Color:
                        rgba: 0.95,0.95,0.95, 0.5
                    Rectangle:
                        pos: self.pos
                        size: self.size

                    Color:
                        rgba: 0.85,0.85,0.85, 1
                    Line:
                        points: self.x, self.y, self.x+self.width,self.y

                MDIconButton:
                    icon: 'tennis'
                    #md_bg_color: (0,0,0,0.1)
                    user_font_size: '60sp'
                    pos_hint: {'center_x': 0.05, 'center_y': 0.5}
    
                BoxLayout:
                    spacing: 0
                    orientation: 'vertical'
    
                    Label:
                        text: '[b]Ημερομηνία:[/b] 29/05/2022'
                        markup: True
                        color: 0,0,0, 0.6
                        text_size: self.size
                        halign: "right"
                        valign: "middle"
                    Label:
                        text: '[b]Διάρκεια:[/b] 01:10:45'
                        markup: True
                        color: 0,0,0, 0.6
                        text_size: self.size
                        halign: "right"
                        valign: "middle"
                    Label:
                        text: '[b]Καύση:[/b] 352 cal'
                        markup: True
                        color: 0,0,0, 0.6
                        text_size: self.size
                        halign: "right"
                        valign: "middle"

        PGScreenSelector:
'''

Builder.load_string(KV)


class History(Screen):

    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app

    def on_back(self):
        print('You hit history')
        self.app.manager.current = 'entry'

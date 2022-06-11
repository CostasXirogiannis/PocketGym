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

               
    def on_back(self):
        print('You hit history')
        self.app.manager.current = 'entry'

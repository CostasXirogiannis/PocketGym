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

           

       

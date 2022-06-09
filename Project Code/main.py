import os

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager, SwapTransition
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
Clock.max_iteration = 20

import entry
import history


__version__ = 'v0.2'

SCR_SELECTOR='''
<PGScreenSelector>:
    cols: 5
    size_hint: (1, 0.05)
    canvas.before:
        Color:
            rgba: 0.3,0.3,0.3, 1
        Rectangle:
            pos: self.pos
            size: self.size

    Label:
        text: "[ref=entry]Entry[/ref]"
        markup: True
        #theme_text_color: 'Custom'
        text_color: 1,1,0, 1
        on_ref_press: app.manager.current = 'entry'
    Label:
        text: 'Scr2'
        #theme_text_color: 'Custom'
        text_color: 1,1,0, 1
        #on_release: app.manager.current = 'entry'
    Label:
        text: "[ref=history]History[/ref]"
        markup: True
        #theme_text_color: 'Custom'
        text_color: 1,1,0, 1
        on_ref_press: app.manager.current = 'history'
    Label:
        text: 'Scr4'
        #theme_text_color: 'Custom'
        text_color: 1,1,0, 1
        #on_release: app.manager.current = 'entry'
    Label:
        text: 'Scr5'
        #theme_text_color: 'Custom'
        text_color: 1,1,0, 1
        #on_release: app.manager.current = 'entry'
'''

Builder.load_string(SCR_SELECTOR)


class PGScreenSelector(GridLayout):
    pass

class PGAppKV(MDApp):

    version = StringProperty(__version__)
    manager = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.title = None
        self.manager = None
        self.entry_scr = None
        self.history_scr = None

    def build(self):

        self.manager = ScreenManager(transition=SwapTransition())

        self.entry = entry.Entry(app=self, name='entry')
        self.manager.add_widget(self.entry)
        self.history = history.History(app=self, name='history')
        self.manager.add_widget(self.history)

        return self.manager

if __name__ == "__main__":
    myapp = PGAppKV()

    myapp.run()

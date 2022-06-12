from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


# This is the entry screen, which user will see when opening the app

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

            #BoxLayout:
                #spacing: 10

                #canvas.before:
                    #Color:
                        #rgba: 0.85,0.85,0.85, 1
                    #Line:
                        #points: self.x, self.y, self.x+self.width,self.y

                #orientation: 'horizontal'
                #MDIconButton:
                    #icon: 'plus-thick'
                    #md_bg_color: (0,0,0,0.1)
                    #user_font_size: '20sp'
                    #pos_hint: {'center_x': 0.05, 'center_y': 0.5}

                #Label:
                    #text: 'extra'
                    #color: 0,0,0, 0.7
                    #text_size: self.size
                    #size_hint: (1, 1)
                    #halign: "left"
                    #valign: "middle"

            #BoxLayout:
                #spacing: 10

                #canvas.before:
                    #Color:
                        #rgba: 0.85,0.85,0.85, 1
                    #Line:
                        #points: self.x, self.y, self.x+self.width,self.y

                #orientation: 'horizontal'
                #MDIconButton:
                    #icon: 'plus-thick'
                    #md_bg_color: (0,0,0,0.1)
                    #user_font_size: '20sp'
                    #pos_hint: {'center_x': 0.05, 'center_y': 0.5}

                #Label:
                    #text: 'extra2'
                    #color: 0,0,0, 0.7
                    #text_size: self.size
                    #size_hint: (1, 1)
                    #halign: "left"
                    #valign: "middle"
       
        PGScreenSelector:
'''

Builder.load_string(KV)


# Methods that are being used by the entry screen

class Entry(Screen):

    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app
    
# Method that will be used when pressing Profile button   
   def on_profile(self):
        print('You hit profile')


# Method that will be used when pressing New Activity button   
    def on_new_activity(self):
        print('You hit new activity')


# Method that will be used when pressing History button   
    def on_history(self):
        print('You hit history')
        self.app.manager.current = 'history'
    
    
# Method that will be used when pressing Premium button   
    def on_premium(self):
        print('You hit premium')


# Method that will be used when pressing  Settings button   
    def on_settings(self):
        print('You hit settings')

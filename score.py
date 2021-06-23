from kivy.core import window
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.properties import NumericProperty
import sys
class Score(BoxLayout):
    hei=NumericProperty()
    wid=NumericProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.opacity=0
    def on_touch_down(self, touch):
        if self.opacity==0:
            return False
        return super(BoxLayout,self).on_touch_down(touch)
    def on_size(self,*args):
        self.wid=Window.width
        self.hei=Window.height
    def end_game(self):
        sys.exit()
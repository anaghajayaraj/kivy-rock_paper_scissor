from ast import Str
from kivy.config import Config
from kivy.core.window import Window
Config.set("graphics","width","900")
Config.set("graphics","height","600")
from kivy.app import App 
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivy.properties import StringProperty,ObjectProperty,NumericProperty
import random
Builder.load_file("score.kv")

class OpeningPage(Screen):
    pass

class GamingPage(Screen):
    scoreSheet=ObjectProperty()
    score_op=NumericProperty()
    user_score=0
    comp_score=0
    msg=StringProperty("It's a draw")
    computer=StringProperty(str(comp_score))
    you=StringProperty(str(user_score))
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def scoreCode(self,_):
        comp_in=random.randint(0,2)
        if comp_in==_:
            pass
        if comp_in==0 and _==1:
            self.user_score+=1
        if comp_in==1 and _==0:
            self.comp_score+=1
        if comp_in==0 and _==2:
            self.comp_score+=1
        if comp_in==2 and _==0:
            self.user_score+=1
        if comp_in==2 and _==1:
            self.comp_score+=1
        if comp_in==1 and _==2:
            self.user_score+=1


    def rockSelected(self):
        self.scoreCode(0)
        self.computer=str(self.comp_score)
        self.you=str(self.user_score)
    def paperSelected(self):
        self.scoreCode(1)
        self.computer=str(self.comp_score)
        self.you=str(self.user_score)
    def scissorSelected(self):
        self.scoreCode(2)
        self.computer=str(self.comp_score)
        self.you=str(self.user_score)
    def score_visible(self):
        if self.score_op==1:
            self.scoreSheet.opacity=1
        else:
            self.scoreSheet.opacity=0
    def score(self):
        self.score_op=1
        self.score_visible()
        if self.user_score>self.comp_score:
            self.msg="You win"
            print(self.msg)
        if self.user_score<self.comp_score:
            self.msg="computer win"
            print(self.msg)
        



class WindowManager(ScreenManager):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.add_widget(OpeningPage(name="first"))
        self.add_widget(GamingPage(name="second"))
        #self.add_widget(ScorePage(name="score"))
        

kv=Builder.load_file("my.kv")
class RockPaperScissorApp(App):
    def build(self):
        
        return kv

if __name__=="__main__":

    RockPaperScissorApp().run()

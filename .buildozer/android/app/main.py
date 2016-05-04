__version__='1.0.1'

from kivy.app import App
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.storage.dictstore import DictStore
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from generator import expression
from datetime import datetime
from highscore import HighscoreDict
from os.path import join

class OPIOApp(App):
    def build(self):
        self.title = "Operation IO"           
        sm = ScreenManager()
        high=Highscores()
        menu_scr = Screen(name = 'menu')
        high_scr = Screen(name = 'highscore', on_pre_enter=high.update)
        high_scr.add_widget(high)
        menu_scr.add_widget(Menu())
        sm.add_widget(high_scr)
        sm.add_widget(menu_scr)
        sm.current='menu'
        return sm

class Highscores(Widget):

    no1_Score=NumericProperty(0)
    no2_Score=NumericProperty(0)
    no3_Score=NumericProperty(0)
    no4_Score=NumericProperty(0)
    no5_Score=NumericProperty(0)
    no6_Score=NumericProperty(0)
    no7_Score=NumericProperty(0)
    no8_Score=NumericProperty(0)
    no9_Score=NumericProperty(0)
    no10_Score=NumericProperty(0)
    
    no1_Name=StringProperty(None)
    no2_Name=StringProperty(None)
    no3_Name=StringProperty(None)
    no4_Name=StringProperty(None)
    no5_Name=StringProperty(None)
    no6_Name=StringProperty(None)
    no7_Name=StringProperty(None)
    no8_Name=StringProperty(None)
    no9_Name=StringProperty(None)
    no10_Name=StringProperty(None)
        
    def __init__(self,**kwargs):
        super(Highscores,self).__init__(**kwargs)
        self.ids.menu_button.bind(on_press=self.exit_highscore)
        self.update()


    def update(self, value=None):

        self.no1_Score=data['highscore']['1'][1]
        self.no2_Score=data['highscore']['2'][1]
        self.no3_Score=data['highscore']['3'][1]
        self.no4_Score=data['highscore']['4'][1]
        self.no5_Score=data['highscore']['5'][1]
        self.no6_Score=data['highscore']['6'][1]
        self.no7_Score=data['highscore']['7'][1]
        self.no8_Score=data['highscore']['8'][1]
        self.no9_Score=data['highscore']['9'][1]
        self.no10_Score=data['highscore']['10'][1]
    
        self.no1_Name=data['highscore']['1'][0]
        self.no2_Name=data['highscore']['2'][0]
        self.no3_Name=data['highscore']['3'][0]
        self.no4_Name=data['highscore']['4'][0]
        self.no5_Name=data['highscore']['5'][0]
        self.no6_Name=data['highscore']['6'][0]
        self.no7_Name=data['highscore']['7'][0]
        self.no8_Name=data['highscore']['8'][0]
        self.no9_Name=data['highscore']['9'][0]
        self.no10_Name=data['highscore']['10'][0]
    

    def exit_highscore(self,values):
        self.parent.manager.current='menu'
        
class MenuButton(Button):
    pass

class Texter(TextInput):
    pass

class MenuLabel(Label):
    pass

class MenuLabelXL(Label):
    pass

class Menu(Widget):
    def __init__(self, **kwargs):
        super(Menu,self).__init__(**kwargs)

    def show_highscore(self,value):
        self.parent.manager.current='highscore'
        
    def start_easy(self,value):
        game=Game(lvl=1)   
        game_scr=Screen(name='game')
        game_scr.add_widget(game) 
        Clock.schedule_interval(game.update,1/2)
        Clock.schedule_interval(game.speed_up,1)           
        self.parent.manager.add_widget(game_scr)
        self.parent.manager.current='game'
        
    def start_med(self,value): 
        game=Game(lvl=2)   
        game_scr=Screen(name='game')
        game_scr.add_widget(game) 
        Clock.schedule_interval(game.update,1/2)
        Clock.schedule_interval(game.speed_up,1)           
        self.parent.manager.add_widget(game_scr)      
        self.parent.manager.current='game'
        
    def start_hard(self,value): 
        game=Game(lvl=3)   
        game_scr=Screen(name='game')
        game_scr.add_widget(game) 
        Clock.schedule_interval(game.update,1/2)
        Clock.schedule_interval(game.speed_up,1)           
        self.parent.manager.add_widget(game_scr)            
        self.parent.manager.current='game'



        
class Game(Widget):
    score = NumericProperty(0)
    wrong = NumericProperty(0)
    miss = NumericProperty(0)
    btn = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(Game,self).__init__(**kwargs)              
        self.size=(WIDTH,HEIGHT)
        self.lvl=kwargs['lvl']
        self.speed=1
        self.miss=0
        self.wrong=0
        self.lbl = MenuLabel(font_size='15sp',text='Right: '+str(self.score))
        self.miss_lbl = MenuLabel(font_size='15sp',text='Missed: '+str(self.miss))
        self.wrong_lbl = MenuLabel(font_size='15sp',text='Wrong: '+str(self.wrong))
        self.new_exp()
        self.info=BoxLayout(halign='left',top=HEIGHT*0.8,size=(WIDTH/3,HEIGHT/5),orientation='vertical')
        self.info.add_widget(self.lbl)
        self.info.add_widget(self.miss_lbl)
        self.info.add_widget(self.wrong_lbl)
        self.add_widget(self.info)
        self.txt_input = Texter(width=WIDTH/2,center=(WIDTH/2,HEIGHT/2))
    
    def end(self):
        Clock.unschedule(self.update)
        Clock.unschedule(self.speed_up)
        self.txt_input.bind(on_text_validate=self.exit_game)
        self.txt_input.select_all()
        self.add_widget(self.txt_input)

    def exit_game(self,value):
        total_score=(self.score*100)-(self.miss*5)-(self.wrong*20)
        val=(self.txt_input.text,total_score)
        highscore.put(val)
        data['highscore']=highscore
        self.remove_widget(self.txt_input)
        self.parent.manager.current='menu'
        self.parent.manager.remove_widget(self.parent)
       
    def new_exp(self):
        if self.btn != None:
            self.remove_widget(self.btn)                        
        self.btn = Expression()
        self.btn.set_exp(self.lvl)      
        self.add_widget(self.btn)
        
    def speed_up(self,dt):
        self.speed *= 1.01

    def choose(self,choice):
        if self.btn.correct==choice:
            self.score+=1
            correct_snd.play()
        else:
            self.wrong+=1
            wrong_snd.play()
        self.new_exp()
        
    def update(self,dt):
        if self.wrong + self.miss + self.score>=25:
            self.end()
        self.lbl.text='Right: '+str(self.score)
        self.miss_lbl.text='Missed: '+str(self.miss)
        self.wrong_lbl.text='Wrong: '+str(self.wrong)
        self.btn.center_y += self.speed * HEIGHT/400
        if self.btn.center_y > HEIGHT:
            self.miss+=1
            miss_snd.play()
            self.new_exp()
        if self.btn.center_x < WIDTH * 0.2:
            self.choose(False)            
        elif self.btn.center_x > WIDTH * 0.8:                
            self.choose(True)          


              
class Expression(Label):
    def __init__(self,**kwargs):
        super(Expression,self).__init__(**kwargs)       
        self.width=WIDTH
        self.height=HEIGHT*0.2       
        self.halign='center'
        self.valign='bottom'             
        
        self.center_x=WIDTH/2
        self.center_y = 0 - self.height       
        
    def set_exp(self,lvl):
        exp = expression(lvl)
        self.text = exp[0]
        self.correct= exp[1]
    
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
        else:
            return super(Expression,self).on_touch_down(touch)
    
    def on_touch_move(self, touch):
        if touch.grab_current is self:
            self.center_x = touch.x           
        else:
            return super(Expression,self).on_touch_move(touch)
    
    def on_touch_up(self,touch):
        if touch.grab_current is self:
            a=Animation(center_x=WIDTH/2, transition='out_elastic')
            a.start(self)


if __name__ == '__main__':
    
    HEIGHT=Window.height
    WIDTH=Window.width
    miss_snd = SoundLoader.load('sound/miss.wav')
    correct_snd = SoundLoader.load('sound/correct.wav')
    wrong_snd = SoundLoader.load('sound/wrong.wav')
    
    highscore = HighscoreDict()
    
    
    opio=OPIOApp()
    data=DictStore('store.dat')
    if data.exists('highscore'):
        for k,v in data['highscore'].items():
            highscore[k]=v
    else:
        data['highscore']=highscore
    opio.run()


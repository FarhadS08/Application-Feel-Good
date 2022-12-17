from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json, glob
from datetime import datetime
from pathlib import Path
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
import random


Builder.load_file('design.kv')

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current='sign_up_screen'

    def login(self, uname, pword):
        with open('users.json') as file:
            users = json.load(file)
        if uname in users and users[uname]['password'] == pword:
            self.manager.current = 'login_screen_success'
        else:
            self.ids.login_wrong.text='Wrong username or password!'

    def forgot_screen(self):
        self.manager.current = 'forgot_screen'

class RootWidget(ScreenManager):
    pass

class SignUpScreen(Screen):
    def add_user(self, uname, pword, bday):
        with open('users.json') as file:
            users = json.load(file)

        users[uname] = {'username':uname, 'password':pword,
        'Birthday':bday,'created': datetime.now().strftime('Y%-m%-d% H%-M%-S%')}

        with open('users.json', 'w') as file:
            json.dump(users, file)
        self.manager.current='sign_up_screen_success'


class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.transition.direction='right'
        self.manager.current='login_screen'

class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login_screen'


    def get_quote(self, feel):
        feel = feel.lower()
        available_feelings = glob.glob('quotes/*txt')

        available_feelings = [Path(filename).stem for 
                            filename in available_feelings]

        if feel in available_feelings:
            with open(f'quotes/{feel}.txt') as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quotes.text = 'Try another feeling'

class ForgotPassword(Screen):
        def get_password(self,uname, bday):
             with open('users.json') as file:
                users = json.load(file)
                password = users[uname]['password'] 
             if uname in users and users[uname]['Birthday'] == bday:
                self.ids.passw.text = password
             else:
                 self.ids.passw.text = 'User not found'
                  

class ImageButton(ButtonBehavior,HoverBehavior, Image):
    pass
      



class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    MainApp().run()





    
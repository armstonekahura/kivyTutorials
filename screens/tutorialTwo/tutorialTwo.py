from kivy.uix.screenmanager import Screen
from datetime import datetime
from kivy.properties import StringProperty

class TutorialTwo(Screen):

    currentDate = StringProperty()

    def __init__(self, **kwargs):
        super(TutorialTwo, self).__init__(**kwargs)
        self.currentDate = self.current_date_method_two()
    
    def current_date_method_one(self):
        currentDate = datetime.now()
        formatedDate = currentDate.strftime("%A, %B %d %Y - %H:%M")
        return formatedDate
    
    def current_date_method_two(self):
        currentDate = datetime.now()
        formatedDate = currentDate.strftime("%A, %B %d %Y - %H:%M")
        return formatedDate
from kivy.config import Config

Config.set('graphics', 'width', 375)
Config.set('graphics', 'height', 650)


from kivymd.app import MDApp
from kivy.lang import Builder


from screens.tutorialOne.tutorialOne import TutorialOne
from screens.tutorialTwo.tutorialTwo import TutorialTwo


class MainApp(MDApp):
    def build(self):
        self.title = "Armarx Mobile"
        # Load the main.kv (Kivy automatically loads main.kv if named same as app class minus "App")
        return Builder.load_file("main.kv")

    def on_start(self):
        # Set default screen
        self.root.current = 'tutorial_two'


if __name__ == "__main__":
    MainApp().run()

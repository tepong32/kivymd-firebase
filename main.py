from kivy.lang import Builder
from kivymd.app import MDApp
from screens import MainScreen, PostScreen, MessageScreen
from models import create_post, send_message

class MainApp(MDApp):
    def build(self):
        self.title = "Social Media App"
        sm = Builder.load_string('''
MDScreenManager:
        MainScreen:
        PostScreen:
        MessageScreen:
        ''')
        return sm

    def go_to_main(self):
        self.root.current = 'main'

    def create_post(self):
        content = self.root.get_screen('post').ids.text_field.text
        create_post(content)
        self.root.current = 'main'

    def send_message(self):
        message = self.root.get_screen('message').ids.message_input.text
        send_message(message)
        self.root.get_screen('message').ids.message_input.text = ""

if __name__ == "__main__":

    MainApp().run()
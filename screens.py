from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

Builder.load_string('''

<MainScreen>:
    name: 'main'
    MDBoxLayout:
        orientation: 'vertical'
        MDNavigationBar:
            title: "Home"
            left_action_items: [['menu', lambda x: app.navigation_draw()]]
        MDLabel:
            text: "Welcome to the Social Media App"
            halign: "center"
        MDRaisedButton:
            text: "Create Post"
            on_release: app.root.current = 'post'

<PostScreen>:
    name: 'post'
    MDBoxLayout:
        orientation: 'vertical'
        MDNavigationBar:
            title: "Create Post"
            left_action_items: [['arrow-left', lambda x: app.go_to_main()]]
        MDTextField:
            id: text_field
            hint_text: "What's on your mind?"
        MDRaisedButton:
            text: "Post"
            on_release: app.create_post()

<MessageScreen>:
    name: 'message'
    MDBoxLayout:
        orientation: 'vertical'
        MDNavigationBar:
            title: "Messages"
            left_action_items: [['arrow-left', lambda x: app.go_to_main()]]
        MDList:
            id: message_list
        MDTextField:
            id: message_input
            hint_text: "Type a message"
        MDRaisedButton:
            text: "Send"
            on_release: app.send_message()
''')


class MainScreen(MDScreen):
    pass


class PostScreen(MDScreen):
    pass


class MessageScreen(MDScreen):

    pass
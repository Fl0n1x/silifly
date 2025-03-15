# Шторка не працює чомусь?????
# Питання ще по налаштуваннях





from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from main_screen import DesighMainScreen
from Sidepanel import SlidingPanel


# Ось ми визначаємо LoginScreen
class LoginScreen(FloatLayout):
    pass  # Тут можна додавати додаткову логіку, якщо потрібно

class SilifyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Builder.load_file("main_screen.kv")  # Завантаження kv файлу

    def build(self):
        Window.size = (350, 1980*350/1080)  # Розмір вікна для телефону
        return LoginScreen()  # Повертаємо екран логіну

    def on_login(self, username):
        self.username = username
        self.root.clear_widgets()  # Очищаємо екран
        main_screen = DesighMainScreen()  # Екран після входу
        self.root.add_widget(main_screen)


if __name__ == "__main__":
    SilifyApp().run()

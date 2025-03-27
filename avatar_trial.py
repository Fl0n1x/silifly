from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.animation import Animation

class ProfileApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        avatar = Image(source="avatar.png", size=(100, 100))
        change_button = Button(text="Change Avatar", size_hint=(None, None), size=(200, 50))

        # Функція для відкриття діалогу вибору файлу
        def change_avatar(instance):
            filechooser = FileChooserIconView()
            filechooser.bind(on_selection=lambda filechooser, value: self.update_avatar(value, avatar))
            popup = Popup(title="Choose Avatar", content=filechooser, size_hint=(0.9, 0.9))
            popup.open()

        change_button.bind(on_press=change_avatar)
        layout.add_widget(avatar)
        layout.add_widget(change_button)
        return layout

    def update_avatar(self, selection, avatar):
        if selection:
            avatar.source = selection[0]  # Обираємо перший файл із списку
            animation = Animation(size=(150, 150), duration=0.5)  # Анімація зміни розміру
            animation.start(avatar)

if __name__ == "__main__":
    ProfileApp().run()

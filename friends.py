<<<<<<< HEAD
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

class FriendsWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.friends_list = []  # Список друзів

        # Поле пошуку
        friend_search = TextInput(hint_text="Введіть псевдонім друга", multiline=False, size_hint=(0.85, None), height=40)
        self.add_widget(friend_search)

        # Кнопка пошуку
        search_button = Button(text="Відправити запит", size_hint=(None, None), width=142, height=40)

        def search(instance):
            friend_name = friend_search.text.strip()
            if friend_name:
                self.friends_list.append(f"Запит на дружбу {friend_name} відправлено")
                friend_search.text = ""
                self.update_friends_list()

        search_button.bind(on_press=search)
        self.add_widget(search_button)

        # Список друзів
        self.scroll_view = ScrollView(size_hint=(1, 0.7))
        self.friends_container = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.friends_container.bind(minimum_height=self.friends_container.setter('height'))

        self.scroll_view.add_widget(self.friends_container)
        self.add_widget(self.scroll_view)

        self.update_friends_list()

    def update_friends_list(self):
        self.friends_container.clear_widgets()
        self.friends_container.add_widget(Label(text="Список друзів:", size_hint_y=None, height=40))

        if self.friends_list:
            for friend in self.friends_list:
                self.friends_container.add_widget(Label(text=friend, size_hint_y=None, height=40))
        else:
            self.friends_container.add_widget(Label(text="Список друзів пустий", size_hint_y=None, height=300))
=======
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

class FriendsWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.friends_list = []  # Список друзів

        # Поле пошуку
        friend_search = TextInput(hint_text="Введіть псевдонім друга", multiline=False, size_hint=(0.85, None), height=40)
        self.add_widget(friend_search)

        # Кнопка пошуку
        search_button = Button(text="Відправити запит", size_hint=(None, None), width=250, height=40)

        def search(instance):
            friend_name = friend_search.text.strip()
            if friend_name:
                self.friends_list.append(f"Запит на дружбу {friend_name} відправлено")
                friend_search.text = ""
                self.update_friends_list()

        search_button.bind(on_press=search)
        self.add_widget(search_button)

        # Список друзів
        self.scroll_view = ScrollView(size_hint=(1, 0.7))
        self.friends_container = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.friends_container.bind(minimum_height=self.friends_container.setter('height'))

        self.scroll_view.add_widget(self.friends_container)
        self.add_widget(self.scroll_view)

        self.update_friends_list()

    def update_friends_list(self):
        self.friends_container.clear_widgets()
        self.friends_container.add_widget(Label(text="Список друзів:", size_hint_y=None, height=40))

        if self.friends_list:
            for friend in self.friends_list:
                self.friends_container.add_widget(Label(text=friend, size_hint_y=None, height=40))
        else:
            self.friends_container.add_widget(Label(text="Список друзів пустий", size_hint_y=None, height=300))
>>>>>>> e40092f (Перше збереження)

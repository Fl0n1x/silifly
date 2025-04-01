from Demos.win32ts_logoff_disconnected import username
from docutils.nodes import label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy_garden.mapview import MapView, MapMarkerPopup, MapSource
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.animation import Animation
import numpy as np
from friends import FriendsWidget
from Sidepanel import SlidingPanel
from settings import SettingsScreen
from kivy.graphics import Ellipse, Rectangle


class ProgressBarLayout(BoxLayout):
    def __init__(self, progress=50, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.spacing = 10
        self.size_hint = (1, 0.1)
        self.pos_hint = {'top':.2}

        self.label = Label(text=f"Progress: {progress}%", size_hint=(0.3, 1), color=(0, 1, 0, 1), pos_hint = {'y':.3})
        self.label.font_size = 16
        self.add_widget(self.label)

        progress_grid = GridLayout(cols=10, spacing=5, size_hint=(0.7, 1))
        buttons = np.array([Button(size_hint=(None, None), size=(30, 30)) for _ in range(10)])

        for i in range(len(buttons)):
            if i < (progress // 10):
                buttons[i].background_color = (0, 1, 0, 1)
            else:
                buttons[i].background_color = (0.2, 0.2, 0.2, 1)
            progress_grid.add_widget(buttons[i])

        self.add_widget(progress_grid)

class MapboxMapView(MapView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.map_source = MapSource(
            url="https://api.mapbox.com/styles/v1/shufla/cm7w6m8em00o301scf10zdpm9/tiles/{z}/{x}/{y}?access_token=pk.eyJ1Ijoic2h1ZmxhIiwiYSI6ImNtN3ZoNDI1eDBiczIybnNhbm9raHVrNnIifQ.T4bkVKCXu_t09rIOiTurmQ",
            attribution="© Mapbox",
            min_zoom=1,
            max_zoom=20
        )


from kivy.uix.image import Image

class DesighMainScreen(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, 1)
        self.sliding_panel = SlidingPanel()
        self.add_widget(self.sliding_panel)

        self.background = Image(source="back.jpg", size = (400, 1980*400/1080),)
        self.add_widget(self.background)

        self.show_layout(None)

    def clear_widgets_except_panel(self):
        widgets_to_remove = [w for w in self.children if w not in {self.sliding_panel, self.background}]
        for w in widgets_to_remove:
            self.remove_widget(w)


    def friends(self, instance):
        self.clear_widgets_except_panel()  # Очищаємо екран
        friends_widget = FriendsWidget()  # Створюємо віджет із друзями
        self.add_widget(friends_widget)  # Додаємо його на екран
        label = Label(text = '')
        self.add_widget(label)
        grid = MyGridLayout()
        self.add_widget(grid)

    def add_map(self):
        return MapboxMapView(zoom=12, lat=49.8425, lon=24.0322, size_hint=(1, 1))

    def clear_screen(self, instance=None):
        self.clear_widgets_except_panel()

    def profile(self, instance):
        self.clear_widgets_except_panel()

        avatar = Image(source='profile.png', size=(50, 50), size_hint=(None, None))
        avatar.size_hint = (None, None)
        avatar.size = (100, 100)  # Встановлюємо розмір.
        avatar.pos = (self.width / 2 - avatar.width / 2 - 150, self.height - avatar.height - 100)
        with avatar.canvas.before:
            self.ellipse = Ellipse(pos=avatar.pos, size=avatar.size)
        self.add_widget(avatar)

        username = Label(
            font_size=28,
            text="User",
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'center_x': 0.65, 'top': 0.89}
        )
        self.add_widget(username)

        grid = MyGridLayout()
        self.add_widget(grid)

        #       def change_avatar(instance):
  ##         filechooser.bind(on_selection=lambda filechooser, value: self.update_avatar(value, avatar))
    #        popup = Popup(title="Choose Avatar", content=filechooser, size_hint=(0.9, 0.9))
     #       popup.open()


#        achivement_button = Button(text='Achievements', size_hint=(1, 0.2))
 #       profile_layout.add_widget(achivement_button)
#
 #       history_button = Button(text='History of visiting', size_hint=(1, 0.2))
  #      profile_layout.add_widget(history_button)

        progress_bar = ProgressBarLayout(progress=53)
        progress_bar.pos_hint = {'top': 0.2}  # Розміщуємо прогрес-бар нижче аватара
        self.add_widget(progress_bar)


        optionsButton = Button(background_normal='settings.png', size_hint=(None, None), size=(30, 30),
                               pos_hint={'top': 1, 'left': 1})



        optionsButton.bind(on_press = self.open_settings)
        self.add_widget(optionsButton)




    def show_layout(self, instance):
        self.clear_widgets_except_panel()

        # Додаємо карту у контейнер
        map_view = self.add_map()
        self.add_widget(map_view)  # Тепер карта точно додається!

        buttons = [
            ("Profile", self.profile),
            ("Friends", self.coming_soon),
            ("Nearest Locations", self.coming_soon),
            ("Quests", self.coming_soon),
            ("Options", self.open_settings)
        ]

        grid = MyGridLayout()
        self.add_widget(grid)

    def coming_soon(self, instance):
        self.clear_widgets_except_panel()
        label = Label(text="Coming soon!", font_size=32, color=(0, 1, 0, 1))
        self.add_widget(label)

        grid = MyGridLayout()
        self.add_widget(grid)

    def open_settings(self, instance):
        settings = SettingsScreen()
        settings.__init__()
        popup = Popup(title="Settings", content=settings, size_hint=(0.8, 0.8))
        popup.open()

class MyGridLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pos_hint = {'x': 0, 'y': 0}



    def get_main_screen(self):
        # Проходимо по батьківських віджетах, поки не знайдемо DesighMainScreen
        parent = self.parent
        while parent:
            if isinstance(parent, DesighMainScreen):
                return parent
            parent = parent.parent
        return None  # Якщо не знайшли

    def profile(self, instance):
        main_screen = self.get_main_screen()
        if main_screen:
            main_screen.profile(instance)

    def coming_soon(self, instance):
        main_screen = self.get_main_screen()
        if main_screen:
            main_screen.coming_soon(instance)

    def options(self, instance):
        main_screen = self.get_main_screen()
        if main_screen:
            main_screen.options(instance)



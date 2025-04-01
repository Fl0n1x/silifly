from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.core.window import Window

class SlidingPanel(RelativeLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.panel_width = Window.width * 0.7
        self.size_hint = (None, None)
        self.size = (self.panel_width, Window.height)
        self.pos = (-self.panel_width, 0)  # Початково схована зліва
        self.is_open = False

        self.panel_box = BoxLayout(orientation='vertical', spacing=10, padding=10)
        self.panel_box.add_widget(Label(text="Settings", font_size=32))
        self.panel_box.add_widget(Button(text="Profile settings"))
        self.panel_box.add_widget(Button(text="Privacy settings"))
        self.panel_box.add_widget(Button(text="Log out", on_press=self.logout))

        self.add_widget(self.panel_box)

    def toggle_panel(self, instance):
        parent = self.parent
        if parent:
            parent.remove_widget(self)
            parent.add_widget(self)

        if self.is_open:
            anim = Animation(x=Window.width, y=Window.height * 0.2, duration=0.3)
            anim.start(self)
            self.is_open = False
        else:
            anim = Animation(x=Window.width - self.panel_width, y=Window.height * 0.1, duration=0.3)
            anim.start(self)
            self.is_open = True

    def logout(self, instance):
        print("Log out clicked")

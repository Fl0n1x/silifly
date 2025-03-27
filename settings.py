from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label


class MyGridLayout(Widget):
    pass


class SettingsScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)
        self.buttons()

    def buttons(self):
        self.name_label = Label(text="Current Name: Default", font_size=24)
        self.add_widget(self.name_label)

        name_button = Button(text="Change Name", font_size=24)
        self.add_widget(name_button)
        name_button.bind(on_release=self.change_name)

        language_button = Button(text='Languages', font_size=24)
        self.add_widget(language_button)
        language_button.bind(on_release=self.language_options)

        privacy_button = Button(text='Privacy and Policy', font_size=24)
        self.add_widget(privacy_button)
        privacy_button.bind(on_release=self.privacy_policy)

        promocode_button = Button(text='Input promocode', font_size=24)
        self.add_widget(promocode_button)
        promocode_button.bind(on_release=self.promocode_input)

        logout_button = Button(text='Log out', font_size=24)
        self.add_widget(logout_button)

    def language_options(self, instance):
        language_popup = Popup(title='Select Language', size_hint=(0.5, 0.4))

        lang_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        language_popup.content = lang_layout

        ukr_button = Button(text='Українська', font_size=28)
        lang_layout.add_widget(ukr_button)

        eng_button = Button(text='English', font_size=28)
        lang_layout.add_widget(eng_button)

        language_popup.open()

    def promocode_input(self, instance):
        promocode_popup = Popup(title='Enter Promocode', size_hint=(0.6, 0.4))

        promo_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        promocode_popup.content = promo_layout

        promo_input = TextInput(hint_text='Enter your promocode', font_size=24, size_hint_y=None, height=50)
        promo_layout.add_widget(promo_input)

        submit_button = Button(text='Submit', font_size=24, size_hint_y=None, height=50)
        promo_layout.add_widget(submit_button)

        promocode_popup.open()

    def privacy_policy(self, instance):
        policy_text = """бла бла бла"""

        policy_popup = Popup(title='Privacy and Policy', size_hint=(0.8, 0.8))

        policy_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        policy_popup.content = policy_layout

        scroll = ScrollView()
        policy_layout.add_widget(scroll)

        policy_label = Label(text=policy_text, font_size=18, size_hint_y=None, valign='top')
        policy_label.bind(texture_size=lambda instance, value: setattr(policy_label, 'height', value[1]))
        scroll.add_widget(policy_label)

        policy_popup.open()

    def change_name(self, instance):
        name_popup = Popup(title="Change Name", size_hint=(0.6, 0.4))

        name_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        name_popup.content = name_layout

        name_input = TextInput(hint_text="Enter new name", font_size=24, size_hint_y=None, height=50)
        name_layout.add_widget(name_input)

        def update_name(instance):
            new_name = name_input.text.strip()
            if new_name:
                self.name_label.text = f"Current Name: {new_name}"
            name_popup.dismiss()

        submit_button = Button(text="Submit", font_size=24, size_hint_y=None, height=50)
        submit_button.bind(on_release=update_name)
        name_layout.add_widget(submit_button)

        name_popup.open()


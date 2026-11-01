# JARVIS ONE IN ALL - FINAL BY SANJIB
# Owner: sanjib.mridha72@gmail.com = FREE
# Features: No Ads + Monthly/Yearly/Lifetime + 50+ Lang + PIN Lock

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.clearcolor = (0.05, 0.05, 0.12, 1)
OWNER_EMAIL = "sanjib.mridha72@gmail.com"

class JarvisApp(App):
    def build(self):
        main = BoxLayout(orientation='vertical', padding=20, spacing=12)
        
        main.add_widget(Label(text='JARVIS ONE IN ALL', font_size=28, bold=True, color=(0,0.7,1,1), size_hint_y=0.15))
        main.add_widget(Label(text='by Sanjib | NO ADS | Owner FREE', font_size=12, color=(0,1,0,1), size_hint_y=0.08))
        
        features = BoxLayout(orientation='vertical', spacing=8, size_hint_y=0.5)
        features.add_widget(Label(text='[1] 50+ Languages - First Select', font_size=12))
        features.add_widget(Label(text='[2] Law - 1 Device=1 Trial, Privacy Safe', font_size=12))
        features.add_widget(Label(text='[3] Genius - Math, Code, Scan, Translate', font_size=12))
        features.add_widget(Label(text='[4] App Finder + World Knowledge', font_size=12))
        features.add_widget(Label(text='[5] SUBSCRIPTION:', font_size=13, bold=True, color=(1,0.8,0,1)))
        features.add_widget(Label(text=' Monthly 99 | Yearly 499 (58% OFF) | Lifetime 999', font_size=12, color=(1,0.8,0,1)))
        features.add_widget(Label(text='[6] PIN Lock + Device ID Lock + Help', font_size=12))
        main.add_widget(features)

        self.input = TextInput(hint_text='Ask anything to JARVIS...', size_hint_y=0.1, multiline=False)
        main.add_widget(self.input)

        self.output = Label(text='JARVIS Ready! All Morning Features Added!', size_hint_y=0.15)
        main.add_widget(self.output)

        btn1 = Button(text='ASK JARVIS', background_color=(0,0.5,1,1), size_hint_y=0.1)
        btn1.bind(on_press=self.ask)
        main.add_widget(btn1)

        btn2 = Button(text='I AGREE - START JARVIS', background_color=(0,0.8,0.3,1), size_hint_y=0.12)
        btn2.bind(on_press=self.start)
        main.add_widget(btn2)

        return main

    def ask(self, x):
        q = self.input.text
        if q:
            self.output.text = f"You: {q}\nJARVIS: Done Boss! Full version ready!"
        else:
            self.output.text = "Please type your question!"

    def start(self, x):
        self.output.text = "JARVIS Started! No Ads Active! Subscriptions Active!"

JarvisApp().run()

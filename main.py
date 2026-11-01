from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
Window.clearcolor = (0.05, 0.05, 0.1, 1)

class JARVIS(App):
    def build(self):
        main = BoxLayout(orientation='vertical', padding=10, spacing=8)
        main.add_widget(Label(text='JARVIS ONE IN ALL', font_size=22, bold=True, color=(0, 1, 1, 1), size_hint_y=None, height=40))
        main.add_widget(Label(text='by Sanjib | NO ADS | Owner FREE', font_size=12, color=(0, 1, 0, 1), size_hint_y=None, height=20))
        self.input_box = TextInput(hint_text='Type Hi...', multiline=False, size_hint_y=None, height=45)
        main.add_widget(self.input_box)
        btn_ask = Button(text='ASK JARVIS', background_color=(0, 1, 1, 1), bold=True, size_hint_y=None, height=50)
        btn_ask.bind(on_press=self.ask_jarvis)
        main.add_widget(btn_ask)
        btn_start = Button(text='I AGREE - START JARVIS', background_color=(0, 1, 0, 1), bold=True, size_hint_y=None, height=50)
        btn_start.bind(on_press=self.start_jarvis)
        main.add_widget(btn_start)
        scroll = ScrollView(size_hint=(1, 1))
        self.output = Label(text='Welcome Boss! Owner FREE Activated!', font_size=13, color=(1, 1, 0, 1), size_hint_y=None, text_size=(Window.width - 20, None))
        self.output.bind(texture_size=self.output.setter('size'))
        scroll.add_widget(self.output)
        main.add_widget(scroll)
        return main
    def start_jarvis(self, instance):
        self.output.text = "✅ JARVIS STARTED Boss!\n✅ No Ads\n✅ Owner: sanjib.mridha72@gmail.com FREE Lifetime!\n✅ All Features Ready!"
    def ask_jarvis(self, instance):
        q=self.input_box.text
        if not q: self.output.text="Type something!"; return
        self.output.text=f"JARVIS Reply to: {q}\n✅ Got it Boss! No Ads Active!"
        self.input_box.text=""
JARVIS().run()
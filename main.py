from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class Portfolio(App):
    def build(self):
        root = BoxLayout(orientation="vertical", padding=30, spacing=20)
        self.label = Label(text="Hi, I'm <Your Name>\nPython Developer",
                           font_size="24sp", halign="center")
        btn = Button(text="About me", size_hint_y=None, height=120)
        btn.bind(on_press=lambda x: setattr(
            self.label, "text", "I build apps with Python."))
        root.add_widget(self.label)
        root.add_widget(btn)
        return root

Portfolio().run()

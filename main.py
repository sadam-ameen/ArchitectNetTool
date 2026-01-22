import socket
import threading
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

class ArchitectNet(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.status = TextInput(
            text="[SYSTEM READY]: Waiting for execution...\n",
            readonly=True,
            multiline=True,
            background_color=(0,0,0,1),
            foreground_color=(0,1,0,1)
        )
        self.btn = Button(
            text="RUN STEALTH INJECTION",
            size_hint_y=0.2,
            background_color=(1,0,0,1)
        )
        self.btn.bind(on_press=self.execute)
        layout.add_widget(self.status)
        layout.add_widget(self.btn)
        return layout
    
    def log(self, msg):
        Clock.schedule_once(lambda dt: self.update_log(msg))
    
    def update_log(self, msg):
        self.status.text += f">> {msg}\n"
    
    def execute(self, instance):
        threading.Thread(target=self.start_server, daemon=True).start()
    
    def start_server(self):
        self.log("Starting server...")
        # كود السيرفر هنا

if __name__ == "__main__":
    ArchitectNet().run()

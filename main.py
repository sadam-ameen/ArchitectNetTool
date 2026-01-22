import socket
import threading
import requests
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class ArchitectNet(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.status = TextInput(text="[SYSTEM READY]: Waiting for execution...\n", readonly=True, background_color=(0,0,0,1), foreground_color=(0,1,0,1))
        self.btn = Button(text="RUN STEALTH INJECTION", size_hint_y=0.2, background_color=(1,0,0,1))
        self.btn.bind(on_press=self.execute)
        self.layout.add_widget(self.status)
        self.layout.add_widget(self.btn)
        return self.layout

    def log(self, msg): self.status.text += f">> {msg}\n"

    def execute(self, instance):
        threading.Thread(target=self.start_engine, daemon=True).start()

    def start_engine(self):
        target = "static.whatsapp.net"
        self.log(f"Targeting: {target}")
        
        # تشغيل البروكسي الداخلي للحقن
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('127.0.0.1', 8989))
        server.listen(50)
        self.log("Stealth Tunnel Active on Port 8989")

        while True:
            client, addr = server.accept()
            threading.Thread(target=self.tunnel, args=(client, target)).start()

    def tunnel(self, client, host):
        try:
            remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            remote.connect((host, 80))
            payload = f"GET / HTTP/1.1\r\nHost: {host}\r\nX-Forwarded-For: 8.8.8.8\r\nConnection: upgrade\r\n\r\n"
            remote.send(payload.encode())
            client.send(b"HTTP/1.1 200 OK\r\n\r\n")
            
            def pipe(src, dst):
                try:
                    while True:
                        d = src.recv(4096)
                        if not d: break
                        dst.send(d)
                except: pass

            threading.Thread(target=pipe, args=(client, remote)).start()
            threading.Thread(target=pipe, args=(remote, client)).start()
            self.log("Traffic Injected Successfully")
        except: pass

if __name__ == "__main__":
    ArchitectNet().run()

import socket
import threading
import requests  # ⚠️ غير مستخدمة - يمكن إزالتها
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class ArchitectNet(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.status = TextInput(
            text="[SYSTEM READY]: Waiting for execution...\n", 
            readonly=True, 
            background_color=(0,0,0,1), 
            foreground_color=(0,1,0,1),
            multiline=True  # ⭐ إضافة هذه الخاصية
        )
        self.btn = Button(
            text="RUN STEALTH INJECTION", 
            size_hint_y=0.2, 
            background_color=(1,0,0,1)
        )
        self.btn.bind(on_press=self.execute)
        self.layout.add_widget(self.status)
        self.layout.add_widget(self.btn)
        return self.layout

    def log(self, msg): 
        # ⭐ استخدم Clock.schedule_once للتحديث الآمن من ثانوي
        from kivy.clock import Clock
        Clock.schedule_once(lambda dt: self.update_log(msg))

    def update_log(self, msg):
        self.status.text += f">> {msg}\n"

    def execute(self, instance):
        threading.Thread(target=self.start_engine, daemon=True).start()

    def start_engine(self):
        try:
            target = "static.whatsapp.net"
            self.log(f"Targeting: {target}")
            
            # ⭐ إضافة handling للأخطاء وإغلاق السوكيت
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server.bind(('127.0.0.1', 8989))
            self.server.listen(5)  # ⭐ قلل عدد الاتصالات
            self.log("Stealth Tunnel Active on Port 8989")
            
            self.running = True
            while self.running:
                try:
                    client, addr = self.server.accept()
                    self.log(f"Connection from {addr}")
                    threading.Thread(target=self.tunnel, args=(client, target)).start()
                except Exception as e:
                    if self.running:
                        self.log(f"Accept error: {e}")
        except Exception as e:
            self.log(f"Server error: {e}")

    def tunnel(self, client, host):
        remote = None
        try:
            remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            remote.connect((host, 80))
            
            # ⭐ إصلاح البايلود - يجب أن يكون بناءً على طلب العميل
            data = client.recv(4096)
            if data:
                # ⭐ تعديل الهيدر ليشمل X-Forwarded-For
                headers = data.decode('utf-8', errors='ignore')
                if 'X-Forwarded-For' not in headers:
                    # إضافة الهيدر إذا لم يكن موجوداً
                    lines = headers.split('\r\n')
                    for i, line in enumerate(lines):
                        if line.lower().startswith('host:'):
                            lines.insert(i+1, 'X-Forwarded-For: 8.8.8.8')
                            break
                    data = '\r\n'.join(lines).encode()
                
                remote.send(data)
                
                def pipe(src, dst, name):
                    try:
                        while True:
                            d = src.recv(4096)
                            if not d: 
                                break
                            dst.send(d)
                    except:
                        pass
                    finally:
                        try:
                            src.close()
                            dst.close()
                        except:
                            pass

                # ⭐ تشغيل الأنابيب في ثوابت منفصلة
                t1 = threading.Thread(target=pipe, args=(client, remote, "client->remote"))
                t2 = threading.Thread(target=pipe, args=(remote, client, "remote->client"))
                t1.start()
                t2.start()
                t1.join()
                t2.join()
                
                self.log("Traffic tunneled successfully")
        except Exception as e:
            self.log(f"Tunnel error: {e}")
        finally:
            # ⭐ تأكد من إغلاق جميع السوكيتات
            try:
                client.close()
            except:
                pass
            try:
                if remote:
                    remote.close()
            except:
                pass

    def on_stop(self):
        # ⭐ تنظيف الموارد عند إغلاق التطبيق
        self.running = False
        try:
            self.server.close()
        except:
            pass

if __name__ == "__main__":
    ArchitectNet().run()

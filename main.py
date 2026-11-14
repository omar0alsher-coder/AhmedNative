import threading
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

class AhmedApp(App):
    def build(self):
        Window.clearcolor = (0.1, 0.1, 0.2, 1)
        self.layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        self.btn = Button(text="ابدأ الحل (بدون متصفح)", size_hint=(1, 0.2), background_color=(0, 0.7, 1, 1), font_size=20)
        self.btn.bind(on_press=self.start_process)
        
        self.log_label = Label(text="جاهز للاتصال بالموقع...", size_hint=(1, 0.8), halign="center", valign="middle")
        self.log_label.bind(size=self.log_label.setter('text_size'))
        
        self.layout.add_widget(self.btn)
        self.layout.add_widget(self.log_label)
        return self.layout

    def start_process(self, instance):
        self.btn.disabled = True
        self.btn.text = "جاري الحل..."
        self.log_label.text = "جاري الاتصال بالسيرفر..."
        threading.Thread(target=self.run_logic).start()

    def run_logic(self):
        try:
            # هنا تضع كود app.py الخاص بك (دالة solve_two_pass و get_session)
            # هذا مثال تجريبي للتأكد من نجاح الاتصال
            response = requests.get("https://me-tp.qureo.education/api/study/students/me", timeout=10)
            if response.status_code in (200, 401, 403):
                self.log_label.text = f"تم الاتصال بنجاح!\nكود الاستجابة: {response.status_code}\n\nيمكنك الآن نقل كود app.py هنا."
            else:
                self.log_label.text = f"استجابة غير متوقعة: {response.status_code}"
        except Exception as e:
            self.log_label.text = f"خطأ في الاتصال:\n{str(e)}"
        
        self.btn.disabled = False
        self.btn.text = "ابدأ الحل مجدداً"

if __name__ == '__main__':
    AhmedApp().run()

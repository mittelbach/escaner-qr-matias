import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2
from pyzbar import pyzbar
import webbrowser

class BarcodeScanner(App):
    def build(self):
        # La interfaz: una caja que contiene la imagen de la cámara
        self.img1 = Image()
        layout = BoxLayout()
        layout.add_widget(self.img1)
        
        # Conectar con la cámara (0 es la integrada, 1 si tenés una externa)
        self.capture = cv2.VideoCapture(0)
        
        # Programar la actualización de la imagen (30 veces por segundo)
        Clock.schedule_interval(self.update, 1.0/30.0)
        
        return layout

    def update(self, dt):
        # Leer un cuadro de la cámara
        ret, frame = self.capture.read()
        
        if ret:
            # 1. PASAR EL ESCÁNER: Buscamos códigos en este cuadro
            barcodes = pyzbar.decode(frame)
            
            for barcode in barcodes:
                # Decodificar el número del código
                barcode_data = barcode.data.decode('utf-8')
                print(f"✅ Código detectado: {barcode_data}")
                
                # 2. ACCIÓN: Abrir Mercado Libre con ese código
                url = f"https://www.mercadolibre.com.ar/jm/search?as_word={barcode_data}"
                webbrowser.open(url)
                
                # 3. HOMEOSTASIS: Cerramos la app para evitar abrir 100 pestañas
                self.on_stop()
                App.get_running_app().stop()
                return

            # 4. FEEDBACK VISUAL: Mostrar lo que ve la cámara en la ventana de Kivy
            # Volteamos la imagen para que no se vea como espejo (opcional)
            buf1 = cv2.flip(frame, 0)
            buf = buf1.tobytes()
            image_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            self.img1.texture = image_texture

    def on_stop(self):
        # Liberar la cámara al cerrar para que no quede "tomada" por el sistema
        if self.capture.isOpened():
            self.capture.release()

if __name__ == '__main__':
    BarcodeScanner().run()

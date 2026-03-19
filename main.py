import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2
from pyzbar import pyzbar

class BarcodeScanner(App):
    def build(self):
        self.img1 = Image()
        layout = BoxLayout()
        layout.add_widget(self.img1)

        # Iniciar captura de cámara (0 suele ser la cámara integrada)
        self.capture = cv2.VideoCapture(0)

        # Actualizar a 30 cuadros por segundo
        Clock.schedule_interval(self.update, 1.0 / 30.0)
        return layout

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            # Buscar códigos en el cuadro actual
            barcodes = pyzbar.decode(frame)
            for barcode in barcodes:
                barcode_data = barcode.data.decode('utf-8')
                print(f"Código detectado: {barcode_data}")

            # Convertir para mostrar en la ventana de Kivy
            buf1 = cv2.flip(frame, 0)
            buf = buf1.tobytes()
            image_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            self.img1.texture = image_texture

    def on_stop(self):
        # Soltar la cámara al cerrar para que no quede "trabada"
        self.capture.release()

if __name__ == '__main__':
    BarcodeScanner().run()
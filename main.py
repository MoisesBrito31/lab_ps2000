import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    pass

class Livre(Screen):
    pass

class Configurar(Screen):
    pass

class Testar(Screen):
    pass

class Construtor(Screen):
    pass

class Rodape(BoxLayout):
    def conectar(self):
        com = self.ids.porta.text
        baundrate = self.ids.baundrate.text
        print(f'Conectado na porta {com} com baudrate {baundrate}')
    pass

class MainApp(App):
    def build(self):
        return Gerenciador()

if __name__ == "__main__":
    MainApp().run()
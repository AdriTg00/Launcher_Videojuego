from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal
from views.VentanaInicio import launcher
from views.cargarPartidas import cargar
from views.configuracion import configuracion
from PySide6.QtGui import QPixmap

class AppController:
    def __init__(self):
        self.launcher = launcher()
        self.config_window = configuracion()
        self.carg_partidas = cargar()
        self.launcher.abrir_config_signal.connect(self.mostrar_configuracion)
        self.launcher.abrir_cargar_signal.connect(self.mostrar_partidas_guardadas)
        

    def mostrar_partidas_guardadas(self):
        print("Abriendo ventana de configuración desde el controlador")
        self.carg_partidas.show()  

    def mostrar_configuracion(self):
        print("Abriendo ventana de cargar partida desde el controlador")
        self.config_window.show()  
    

   
   

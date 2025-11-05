from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMainWindow
from generated.VentanaInicio_ui import Ui_launcher
import recursos_rc



class launcher(QMainWindow):
    abrir_config_signal = Signal()
    abrir_cargar_signal = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_launcher()
        self.ui.setupUi(self)
    
        self.ui.nuevaPartida.clicked.connect(self.nueva_partida)
        self.ui.cargarDatos.clicked.connect(self.cargar_datos)

        self.ui.opciones.clicked.connect(self.emitir_abrir_config)

    # === FUNCIONES ===
    def nueva_partida(self):
        print("Nueva partida iniciada")
       

    def cargar_datos(self):
        print("Cargar datos de partida")
        self.abrir_cargar_signal.emit()
        

    def emitir_abrir_config(self):
        print("Señal para abrir configuración emitida")
        self.abrir_config_signal.emit() 
      

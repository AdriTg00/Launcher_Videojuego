from PySide6.QtWidgets import QWidget, QMessageBox
from views.configuracion_ui import Ui_configuracion
from model.config_bd import guardar_configuracion



class configuracion(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_configuracion()
        self.ui.setupUi(self)
        self.ui.ventana.setChecked(True)
        self.ui.ventana.stateChanged.connect(self.sync_checkboxes)
        self.ui.completa.stateChanged.connect(self.sync_checkboxes)
        #Sliders
        self.ui.volumenGeneralSlider.valueChanged.connect(self.actualizar_volumen_general)
        self.ui.volumenSFXSlider.valueChanged.connect(self.actualizar_volumen_sfx)
        # Mostrar valores iniciales
        self.actualizar_volumen_general()
        self.actualizar_volumen_sfx()
        #Guardar configuracion
        self.ui.guardar.clicked.connect(self.guardar_configuracion)


    def sync_checkboxes(self):
        sender = self.sender()

        if sender == self.ui.ventana and self.ui.ventana.isChecked():
            self.ui.completa.setChecked(False)

        elif sender == self.ui.completa and self.ui.completa.isChecked():
            self.ui.ventana.setChecked(False)

        if not self.ui.ventana.isChecked() and not self.ui.completa.isChecked():
            sender.setChecked(True)

        # === SLIDERS ===
    def actualizar_volumen_general(self):
        valor = self.ui.volumenGeneralSlider.value()
        self.ui.volumenGeneral.setText(f"{valor}%")

    def actualizar_volumen_sfx(self):
        valor = self.ui.volumenSFXSlider.value()
        self.ui.volumenSFX.setText(f"{valor}%")

    def guardar_configuracion(self):
        volumen_musica = self.ui.volumenGeneralSlider.value()
        volumen_sfx = self.ui.volumenSFXSlider.value()
        resolucion = self.ui.resolucion.currentText()
        modo_pantalla = "ventana" if self.ui.ventana.isChecked() else "completa"

        guardar_configuracion(volumen_musica, volumen_sfx, resolucion, modo_pantalla)

        msg = QMessageBox(self)
        msg.setWindowTitle("Guardado")
        msg.setText("Configuración guardada correctamente.")
        msg.exec()
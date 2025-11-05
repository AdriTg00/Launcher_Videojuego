# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuracion.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QLabel, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QWidget)

class Ui_configuracion(object):
    def setupUi(self, configuracion):
        if not configuracion.objectName():
            configuracion.setObjectName(u"configuracion")
        configuracion.resize(479, 330)
        configuracion.setStyleSheet(u"background-color: #faf0d6;")
        self.gridLayout = QGridLayout(configuracion)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(configuracion)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"QLabel {\n"
"    color: #3C3C3C;\n"
"    font-size: 11px;\n"
"    font-weight: bold;\n"
"    padding: 6px;\n"
"    letter-spacing: 1px;\n"
"}")

        self.gridLayout.addWidget(self.label_2, 4, 2, 1, 1)

        self.guardar = QPushButton(configuracion)
        self.guardar.setObjectName(u"guardar")
        self.guardar.setStyleSheet(u"#guardar {\n"
"    background-color: #7DA23A;          /* Verde oliva oscuro */\n"
"    border: 3px solid #5C7A28;          /* Borde m\u00e1s oscuro para contraste */\n"
"    border-radius: 12px;\n"
"    color: #FDF5C9;                     /* Texto claro, c\u00e1lido */\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    padding: 8px 15px;\n"
"}\n"
"\n"
"#guardar:hover {\n"
"    background-color: #8FBF42;          /* Un verde m\u00e1s vivo al pasar el rat\u00f3n */\n"
"    border: 3px solid #6E9230;\n"
"}\n"
"\n"
"#guardar:pressed {\n"
"    background-color: #6E8D2E;          /* M\u00e1s oscuro al presionar */\n"
"    border: 3px solid #4F6B21;\n"
"}\n"
"\n"
"#guardar:disabled {\n"
"    background-color: #A0A0A0;          /* Gris cuando est\u00e1 desactivado */\n"
"    color: #D8D8D8;\n"
"    border: 3px solid #808080;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.guardar, 6, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 7, 2, 1, 1)

        self.label_3 = QLabel(configuracion)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel {\n"
"    color: #3C3C3C;\n"
"    font-size: 11px;\n"
"    font-weight: bold;\n"
"    padding: 6px;\n"
"    letter-spacing: 1px;\n"
"}")

        self.gridLayout.addWidget(self.label_3, 5, 2, 1, 1)

        self.resolucion = QComboBox(configuracion)
        self.resolucion.addItem("")
        self.resolucion.addItem("")
        self.resolucion.addItem("")
        self.resolucion.addItem("")
        self.resolucion.setObjectName(u"resolucion")
        self.resolucion.setMaximumSize(QSize(150, 50))
        font1 = QFont()
        font1.setFamilies([u"Press Start 2P"])
        self.resolucion.setFont(font1)
        self.resolucion.setStyleSheet(u"QComboBox {\n"
"    background-color: #E2C75E;       /* Amarillo m\u00e1s oscuro */\n"
"    border: 3px solid #B28A2A;       /* Dorado oscuro */\n"
"    border-radius: 10px;\n"
"    padding: 5px 10px;\n"
"    font-size: 10px;\n"
"    color: #2E2404;                  /* Marr\u00f3n oscuro para contraste */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #D8B84C;       /* M\u00e1s brillante al pasar el rat\u00f3n */\n"
"    border: 3px solid #C99A25;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    background: transparent;\n"
"    width: 25px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(down_arrow.png);      /* Si tienes una flecha pixelada, ponla aqu\u00ed */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"/* --- LISTA DESPLEGABLE --- */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #EFD77A;       /* Un tono intermedio */\n"
"    border: 2px solid #B28A2A;\n"
"    selection-background-color: #D8B84C;\n"
"    selection-color: #2E2404;\n"
"    ou"
                        "tline: none;\n"
"    font-size: 10px;\n"
"}\n"
"")
        self.resolucion.setModelColumn(0)

        self.gridLayout.addWidget(self.resolucion, 4, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 4, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 5, 5, 1, 1)

        self.ventana = QCheckBox(configuracion)
        self.ventana.setObjectName(u"ventana")
        self.ventana.setStyleSheet(u"/* --- ESTILO GENERAL DE QCheckBox --- */\n"
"QCheckBox {\n"
"    spacing: 8px;\n"
"    font-size: 10px;\n"
"    color: #3B2E05;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"/* --- CHECKBOX SIN MARCAR --- */\n"
"QCheckBox::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border: 2px solid #C9A43A;        /* Borde dorado */\n"
"    border-radius: 4px;\n"
"    background-color: #F4E29B;        /* Amarillo suave */\n"
"}\n"
"\n"
"/* --- CHECKBOX MARCADO --- */\n"
"QCheckBox::indicator:checked {\n"
"    image: none;\n"
"    background-color: #9BCB43;        /* Verde tipo \u201cCargar datos\u201d */\n"
"    border: 2px solid #5F8A2A;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* --- CHECKBOX AL PASAR EL RAT\u00d3N --- */\n"
"QCheckBox::indicator:hover {\n"
"    background-color: #F9D95C;        /* Amarillo m\u00e1s brillante */\n"
"    border: 2px solid #E5B937;\n"
"}\n"
"\n"
"/* --- CHECKBOX DESHABILITADO --- */\n"
"QCheckBox::indicator:disabled {\n"
"    background-color: #EDE2AC;\n"
"    border: 2px solid "
                        "#B8A34F;\n"
"    opacity: 0.6;\n"
"}\n"
"\n"
"QCheckBox:disabled {\n"
"    color: #8E8352;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.ventana, 5, 3, 1, 1)

        self.completa = QCheckBox(configuracion)
        self.completa.setObjectName(u"completa")
        self.completa.setStyleSheet(u"/* --- ESTILO GENERAL DE QCheckBox --- */\n"
"QCheckBox {\n"
"    spacing: 8px;\n"
"    font-size: 10px;\n"
"    color: #3B2E05;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"/* --- CHECKBOX SIN MARCAR --- */\n"
"QCheckBox::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border: 2px solid #C9A43A;        /* Borde dorado */\n"
"    border-radius: 4px;\n"
"    background-color: #F4E29B;        /* Amarillo suave */\n"
"}\n"
"\n"
"/* --- CHECKBOX MARCADO --- */\n"
"QCheckBox::indicator:checked {\n"
"    image: none;\n"
"    background-color: #9BCB43;        /* Verde tipo \u201cCargar datos\u201d */\n"
"    border: 2px solid #5F8A2A;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* --- CHECKBOX AL PASAR EL RAT\u00d3N --- */\n"
"QCheckBox::indicator:hover {\n"
"    background-color: #F9D95C;        /* Amarillo m\u00e1s brillante */\n"
"    border: 2px solid #E5B937;\n"
"}\n"
"\n"
"/* --- CHECKBOX DESHABILITADO --- */\n"
"QCheckBox::indicator:disabled {\n"
"    background-color: #EDE2AC;\n"
"    border: 2px solid "
                        "#B8A34F;\n"
"    opacity: 0.6;\n"
"}\n"
"\n"
"QCheckBox:disabled {\n"
"    color: #8E8352;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.completa, 5, 4, 1, 1)

        self.label = QLabel(configuracion)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel {\n"
"    color: #3C3C3C;\n"
"    font-size: 11px;\n"
"    font-weight: bold;\n"
"    padding: 6px;\n"
"    letter-spacing: 1px;\n"
"}")

        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)

        self.volumenGeneralSlider = QSlider(configuracion)
        self.volumenGeneralSlider.setObjectName(u"volumenGeneralSlider")
        self.volumenGeneralSlider.setMaximumSize(QSize(300, 70))
        self.volumenGeneralSlider.setStyleSheet(u"/* --- QSLIDER HORIZONTAL --- */\n"
"QSlider::groove:horizontal {\n"
"    border: 2px solid #C9A43A;              /* Contorno dorado */\n"
"    height: 10px;\n"
"    background: #F4E29B;                    /* Amarillo suave (igual que botones) */\n"
"    border-radius: 5px;\n"
"    margin: 0px 10px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: 0.4,\n"
"        fx: 0.4, fy: 0.4,\n"
"        radius: 0.6,\n"
"        stop: 0 #FFE873,\n"
"        stop: 1 #C9A43A\n"
"    );\n"
"    border: 2px solid #5A4A00;\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-radius: 10px;\n"
"    margin: -6px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: 0.4,\n"
"        fx: 0.4, fy: 0.4,\n"
"        radius: 0.6,\n"
"        stop: 0 #FFF3B0,\n"
"        stop: 1 #E5B937\n"
"    );\n"
"}\n"
"\n"
"/* --- PARTE IZQUIERDA (LLENA) --- */\n"
"QSlider::sub-page:horizontal {\n"
"    background: #9BCB43;   "
                        "                 /* Verde suave tipo \u201cCargar datos\u201d */\n"
"    border: 2px solid #5F8A2A;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* --- PARTE DERECHA (VAC\u00cdA) --- */\n"
"QSlider::add-page:horizontal {\n"
"    background: #EDE2AC;                    /* Beige claro */\n"
"    border: 2px solid #C9A43A;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* --- QSLIDER VERTICAL (por si lo usas) --- */\n"
"QSlider::groove:vertical {\n"
"    border: 2px solid #C9A43A;\n"
"    width: 10px;\n"
"    background: #F4E29B;\n"
"    border-radius: 5px;\n"
"    margin: 10px 0px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: 0.4,\n"
"        fx: 0.4, fy: 0.4,\n"
"        radius: 0.6,\n"
"        stop: 0 #FFE873,\n"
"        stop: 1 #C9A43A\n"
"    );\n"
"    border: 2px solid #5A4A00;\n"
"    height: 20px;\n"
"    width: 20px;\n"
"    border-radius: 10px;\n"
"    margin: 0 -6px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background: #9BCB43;\n"
"    "
                        "border: 2px solid #5F8A2A;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"    background: #EDE2AC;\n"
"    border: 2px solid #C9A43A;\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.volumenGeneralSlider.setMaximum(100)
        self.volumenGeneralSlider.setValue(0)
        self.volumenGeneralSlider.setTracking(True)
        self.volumenGeneralSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout.addWidget(self.volumenGeneralSlider, 1, 3, 1, 1)

        self.label_4 = QLabel(configuracion)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel {\n"
"    color: #3C3C3C;\n"
"    font-size: 11px;\n"
"    font-weight: bold;\n"
"    padding: 6px;\n"
"    letter-spacing: 1px;\n"
"}")

        self.gridLayout.addWidget(self.label_4, 2, 2, 1, 1)

        self.volumenSFXSlider = QSlider(configuracion)
        self.volumenSFXSlider.setObjectName(u"volumenSFXSlider")
        self.volumenSFXSlider.setMaximumSize(QSize(300, 70))
        self.volumenSFXSlider.setStyleSheet(u"/* --- QSLIDER HORIZONTAL --- */\n"
"QSlider::groove:horizontal {\n"
"    border: 2px solid #C9A43A;              /* Contorno dorado */\n"
"    height: 10px;\n"
"    background: #F4E29B;                    /* Amarillo suave (igual que botones) */\n"
"    border-radius: 5px;\n"
"    margin: 0px 10px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: 0.4,\n"
"        fx: 0.4, fy: 0.4,\n"
"        radius: 0.6,\n"
"        stop: 0 #FFE873,\n"
"        stop: 1 #C9A43A\n"
"    );\n"
"    border: 2px solid #5A4A00;\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-radius: 10px;\n"
"    margin: -6px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: 0.4,\n"
"        fx: 0.4, fy: 0.4,\n"
"        radius: 0.6,\n"
"        stop: 0 #FFF3B0,\n"
"        stop: 1 #E5B937\n"
"    );\n"
"}\n"
"\n"
"/* --- PARTE IZQUIERDA (LLENA) --- */\n"
"QSlider::sub-page:horizontal {\n"
"    background: #9BCB43;   "
                        "                 /* Verde suave tipo \u201cCargar datos\u201d */\n"
"    border: 2px solid #5F8A2A;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* --- PARTE DERECHA (VAC\u00cdA) --- */\n"
"QSlider::add-page:horizontal {\n"
"    background: #EDE2AC;                    /* Beige claro */\n"
"    border: 2px solid #C9A43A;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* --- QSLIDER VERTICAL (por si lo usas) --- */\n"
"QSlider::groove:vertical {\n"
"    border: 2px solid #C9A43A;\n"
"    width: 10px;\n"
"    background: #F4E29B;\n"
"    border-radius: 5px;\n"
"    margin: 10px 0px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: 0.4,\n"
"        fx: 0.4, fy: 0.4,\n"
"        radius: 0.6,\n"
"        stop: 0 #FFE873,\n"
"        stop: 1 #C9A43A\n"
"    );\n"
"    border: 2px solid #5A4A00;\n"
"    height: 20px;\n"
"    width: 20px;\n"
"    border-radius: 10px;\n"
"    margin: 0 -6px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background: #9BCB43;\n"
"    "
                        "border: 2px solid #5F8A2A;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"    background: #EDE2AC;\n"
"    border: 2px solid #C9A43A;\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.volumenSFXSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout.addWidget(self.volumenSFXSlider, 2, 3, 1, 1)

        self.volumenGeneral = QLabel(configuracion)
        self.volumenGeneral.setObjectName(u"volumenGeneral")
        self.volumenGeneral.setStyleSheet(u"QLabel {\n"
"    color: #3C3C3C;\n"
"    font-size: 11px;\n"
"    font-weight: bold;\n"
"    padding: 6px;\n"
"    letter-spacing: 1px;\n"
"}")

        self.gridLayout.addWidget(self.volumenGeneral, 1, 4, 1, 1)

        self.volumenSFX = QLabel(configuracion)
        self.volumenSFX.setObjectName(u"volumenSFX")
        self.volumenSFX.setStyleSheet(u"QLabel {\n"
"    color: #3C3C3C;\n"
"    font-size: 11px;\n"
"    font-weight: bold;\n"
"    padding: 6px;\n"
"    letter-spacing: 1px;\n"
"}")

        self.gridLayout.addWidget(self.volumenSFX, 2, 4, 1, 1)


        self.retranslateUi(configuracion)

        self.resolucion.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(configuracion)
    # setupUi

    def retranslateUi(self, configuracion):
        configuracion.setWindowTitle(QCoreApplication.translate("configuracion", u"Configuracion", None))
        self.label_2.setText(QCoreApplication.translate("configuracion", u"Resoluci\u00f3n:", None))
        self.guardar.setText(QCoreApplication.translate("configuracion", u"Guardar configuraci\u00f3n", None))
        self.label_3.setText(QCoreApplication.translate("configuracion", u"Tipo de visualizaci\u00f3n:", None))
        self.resolucion.setItemText(0, QCoreApplication.translate("configuracion", u"640x480", None))
        self.resolucion.setItemText(1, QCoreApplication.translate("configuracion", u"960x540", None))
        self.resolucion.setItemText(2, QCoreApplication.translate("configuracion", u"1280x720", None))
        self.resolucion.setItemText(3, QCoreApplication.translate("configuracion", u"1920x1080", None))

        self.resolucion.setPlaceholderText("")
        self.ventana.setText(QCoreApplication.translate("configuracion", u"Ventana ", None))
        self.completa.setText(QCoreApplication.translate("configuracion", u"Completa", None))
        self.label.setText(QCoreApplication.translate("configuracion", u"Volumen general:", None))
        self.label_4.setText(QCoreApplication.translate("configuracion", u"Volumen SFX:", None))
        self.volumenGeneral.setText(QCoreApplication.translate("configuracion", u"TextLabel", None))
        self.volumenSFX.setText(QCoreApplication.translate("configuracion", u"TextLabel", None))
    # retranslateUi


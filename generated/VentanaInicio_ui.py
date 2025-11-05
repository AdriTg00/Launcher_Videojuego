# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaInicio.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QWidget)
import recursos_rc

class Ui_launcher(object):
    def setupUi(self, launcher):
        if not launcher.objectName():
            launcher.setObjectName(u"launcher")
        launcher.resize(489, 607)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(launcher.sizePolicy().hasHeightForWidth())
        launcher.setSizePolicy(sizePolicy)
        launcher.setStyleSheet(u"background-color: #faf0d6;\n"
"")
        self.centralwidget = QWidget(launcher)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 70, 251, 121))
        self.label_2.setPixmap(QPixmap(u":/imagenes/assets/rey_y_cerdos.png"))
        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(-50, 300, 211, 241))
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setPixmap(QPixmap(u":/imagenes/assets/rey.png"))
        self.label_3.setScaledContents(True)
        self.nuevaPartida = QPushButton(self.centralwidget)
        self.nuevaPartida.setObjectName(u"nuevaPartida")
        self.nuevaPartida.setGeometry(QRect(140, 260, 211, 41))
        font = QFont()
        font.setFamilies([u"Press Start 2P"])
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        self.nuevaPartida.setFont(font)
        self.nuevaPartida.setStyleSheet(u"QPushButton {\n"
"    background-color: #ffd84a;         /* color dorado */\n"
"    border: 3px solid #6a4e00;         /* borde oscuro */\n"
"    border-radius: 10px;               /* bordes redondeados */\n"
"    color: #2e2e2e;                    /* texto oscuro */\n"
"    padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ffe680;         /* m\u00e1s claro al pasar el rat\u00f3n */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e5c13a;         /* tono m\u00e1s oscuro al pulsar */\n"
"    border: 3px solid #4d3700;\n"
"}\n"
"")
        icon = QIcon(QIcon.fromTheme(u"applications-games"))
        self.nuevaPartida.setIcon(icon)
        self.cargarDatos = QPushButton(self.centralwidget)
        self.cargarDatos.setObjectName(u"cargarDatos")
        self.cargarDatos.setGeometry(QRect(140, 330, 211, 41))
        font1 = QFont()
        font1.setFamilies([u"Press Start 2P"])
        font1.setPointSize(8)
        self.cargarDatos.setFont(font1)
        self.cargarDatos.setStyleSheet(u"#cargarDatos {\n"
"    background-color: #6CDE56;           /* verde base */\n"
"    border: 3px solid #296B20;           /* borde verde oscuro */\n"
"    border-radius: 10px;\n"
"    color: #1E1E1E;                      /* texto casi negro */\n"
"   \n"
"    padding: 8px 16px;\n"
"}\n"
"\n"
"#cargarDatos:hover {\n"
"    background-color: #7FF066;           /* m\u00e1s claro al pasar el rat\u00f3n */\n"
"}\n"
"\n"
"#cargarDatos:pressed {\n"
"    background-color: #58B947;           /* tono m\u00e1s oscuro al pulsar */\n"
"    border: 3px solid #204D1A;\n"
"}\n"
"")
        icon1 = QIcon(QIcon.fromTheme(u"accessories-dictionary"))
        self.cargarDatos.setIcon(icon1)
        self.opciones = QPushButton(self.centralwidget)
        self.opciones.setObjectName(u"opciones")
        self.opciones.setGeometry(QRect(140, 400, 211, 41))
        self.opciones.setFont(font1)
        self.opciones.setStyleSheet(u"#opciones {\n"
"    background-color: #9CC3D5;           /* azul gris\u00e1ceo base */\n"
"    border: 3px solid #2E3F4E;           /* borde m\u00e1s oscuro */\n"
"    border-radius: 10px;\n"
"    color: #1A1A1A;\n"
"\n"
"}\n"
"\n"
"#opciones:hover {\n"
"    background-color: #B5D3E1;           /* tono m\u00e1s claro al pasar el rat\u00f3n */\n"
"}\n"
"\n"
"#opciones:pressed {\n"
"    background-color: #7CA6BB;           /* tono m\u00e1s oscuro al pulsar */\n"
"    border: 3px solid #1E2B35;\n"
"}\n"
"")
        icon2 = QIcon(QIcon.fromTheme(u"applications-development"))
        self.opciones.setIcon(icon2)
        self.salir = QPushButton(self.centralwidget)
        self.salir.setObjectName(u"salir")
        self.salir.setGeometry(QRect(140, 470, 211, 41))
        self.salir.setFont(font1)
        self.salir.setStyleSheet(u"#salir {\n"
"    background-color: #E06C75;\n"
"    border: 3px solid #7A1C1C;\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"}\n"
"#salir:hover {\n"
"    background-color: #EE828A;\n"
"}\n"
"#salir:pressed {\n"
"    background-color: #C1555D;\n"
"    border: 3px solid #5A0F0F;\n"
"}\n"
"")
        icon3 = QIcon(QIcon.fromTheme(u"application-exit"))
        self.salir.setIcon(icon3)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(360, 330, 181, 201))
        self.label.setPixmap(QPixmap(u":/imagenes/assets/cerdito.png"))
        self.label.setScaledContents(True)
        launcher.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(launcher)
        self.statusbar.setObjectName(u"statusbar")
        launcher.setStatusBar(self.statusbar)

        self.retranslateUi(launcher)

        QMetaObject.connectSlotsByName(launcher)
    # setupUi

    def retranslateUi(self, launcher):
        launcher.setWindowTitle(QCoreApplication.translate("launcher", u"Launcher", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.nuevaPartida.setText(QCoreApplication.translate("launcher", u"Nueva partida", None))
        self.cargarDatos.setText(QCoreApplication.translate("launcher", u"Cargar datos", None))
        self.opciones.setText(QCoreApplication.translate("launcher", u"Opciones", None))
        self.salir.setText(QCoreApplication.translate("launcher", u"Salir", None))
        self.label.setText("")
    # retranslateUi


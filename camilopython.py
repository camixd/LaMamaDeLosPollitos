import sys
from PySide.QtCore import *
from PySide.QtGui import *

app = QApplication(sys.argv)

ventana = QDialog ()
ventana.show()

titulo = QLabel("esto es bueno")
titulo.show()

boton = QRadioButton ()
boton.show()

menu = QMainWindow ()
menu.show()

app.exec_()
sys.exit()


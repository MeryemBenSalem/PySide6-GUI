import sys
from PySide6 import QtWidgets
from window import window


app = QtWidgets.QApplication(sys.argv)

window = window()
window.show()

app.exec()
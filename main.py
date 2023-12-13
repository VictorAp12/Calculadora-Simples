import sys
import typing
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from tela import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent: QWidget | None = ..., flags: WindowFlags | WindowType = ...) -> None:
        super().__init__(parent, flags)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow.show()
    sys.exit(app.exec_())
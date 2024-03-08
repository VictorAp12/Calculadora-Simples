"""
This module contains the main window of the application.

It inherits from the QMainWindow class from PySide6.
And contains a QWidget and a QVBoxLayout for the layout.
"""

from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMessageBox


class MainWindow(QMainWindow):
    """
    This class represents the main window of the application.
    """

    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:

        super().__init__(parent, *args, **kwargs)

        # configuring the basic layout
        self.v_layout = QVBoxLayout()
        self.cw = QWidget()
        self.cw.setLayout(self.v_layout)
        self.setCentralWidget(self.cw)

        # window title
        self.setWindowTitle("Calculadora")

    def adjust_fixed_size(self):
        """
        This method adjusts the fixed size of the window.
        """
        # adjusting the window size
        self.adjustSize()
        self.setFixedSize(self.size())

    def add_widget_to_vlayout(self, widget: QWidget):
        """
        This method adds a widget to the v_layout of the main window.
        """
        self.v_layout.addWidget(widget)

    def make_msg_box(self):
        """
        This method creates a message box.
        """
        return QMessageBox(self)

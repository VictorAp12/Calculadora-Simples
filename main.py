"""
This is the main file of the application.

It creates the application, calls the main window and sets the icon.
"""

import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from main_window import MainWindow
from info import Info
from display import Display
from buttons import ButtonsGrid
from styles import setup_theme
from variables import WINDOW_ICON_PATH

if __name__ == "__main__":
    # creates the application
    app = QApplication(sys.argv)
    window = MainWindow()

    setup_theme()
    # sets the icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # sets the info label
    info = Info("Sua Conta")
    window.add_widget_to_vlayout(info)

    # Display which is a QLineEdit that shows the inputs
    display = Display()
    window.add_widget_to_vlayout(display)

    # Grid
    buttons_grid = ButtonsGrid(display, info, window)
    window.v_layout.addLayout(buttons_grid)

    # executes the application
    window.adjust_fixed_size()
    window.show()
    app.exec()
    window.setFocus()

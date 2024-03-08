"""
This module contains the info class, which is a label that displays information.

It inherits from the QLabel class from PySide6.
And contains a QWidget and a QVBoxLayout for the layout.
"""

from PySide6.QtWidgets import QLabel, QWidget
from PySide6.QtCore import Qt
from variables import SMALL_FONT_SIZE


class Info(QLabel):
    """
    This class represents the info class, which is a label that displays information.
    """

    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self._config_style()

    def _config_style(self):
        """
        This method configures the style of the label.
        """
        self.setStyleSheet(f"font-size: {SMALL_FONT_SIZE}px;")
        self.setAlignment(Qt.AlignmentFlag.AlignRight)

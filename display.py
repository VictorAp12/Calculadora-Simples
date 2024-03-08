from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent

from variables import BIG_FONT_SIZE, TEXT_MARGIN, MINIMUM_WIDTH
from utils import is_empty, is_num_or_dot


class Display(QLineEdit):
    """
    This class represents the display class, which is a QLineEdit that shows the inputs.

    It inherits from the QLineEdit class from PySide6.
    """

    equal_pressed = Signal()
    backspace_pressed = Signal()
    clear_pressed = Signal()
    number_or_dot_pressed = Signal(str)
    operator_pressed = Signal(str)

    def config_style(self):
        """
        This method configures the style of the display.

        It sets the font size, minimum height, minimum width, alignment, and margins.
        """
        self.setStyleSheet(f"font-size: {BIG_FONT_SIZE}px;")
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[TEXT_MARGIN for _ in range(4)])

    def keyPressEvent(self, event: QKeyEvent) -> None:
        """
        This method handles the key press event.
        """

        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key

        is_enter = key in [KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal]
        is_backspace = key in [KEYS.Key_Backspace, KEYS.Key_Delete, KEYS.Key_D]
        is_esc = key in [KEYS.Key_Escape, KEYS.Key_C]
        is_operator = key in [
            KEYS.Key_Plus,
            KEYS.Key_Minus,
            KEYS.Key_Slash,
            KEYS.Key_Asterisk,
            KEYS.Key_P,
        ]

        if is_enter:
            self.equal_pressed.emit()

        if is_esc:
            self.clear_pressed.emit()

        if is_backspace:
            self.backspace_pressed.emit()

        if is_empty(text):
            return event.ignore()

        if is_num_or_dot(text):
            self.number_or_dot_pressed.emit(text)

        if is_operator:
            if text.lower() == "p":
                text = "^"

            self.operator_pressed.emit(text)

        return event.ignore()

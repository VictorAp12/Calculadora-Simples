"""
This module contains the buttons class, which is a grid of buttons.

It inherits from the QGridLayout class from PySide6.
And contains a QPushButton.
"""

from typing import TYPE_CHECKING, Callable
import math

from PySide6.QtWidgets import QGridLayout, QPushButton
from PySide6.QtCore import Slot

from variables import MEDIUM_FONT_SIZE
from utils import is_num_or_dot, is_valid_number, is_empty, convert_to_number

if TYPE_CHECKING:
    from display import Display
    from info import Info
    from main_window import MainWindow


class Button(QPushButton):
    """
    This class represents the button class, which is a grid of buttons.
    It inherits from the QPushButton class from PySide6.

    It's like an Abstract class for the buttons.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config_style()

    def config_style(self):
        """
        This method configures the style of the button.
        """
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(50, 50)


class ButtonsGrid(QGridLayout):
    """
    This class represents the buttons grid class, which is a grid of buttons.

    It inherits from the QGridLayout class from PySide6.

    It contains many buttons with different functions.
    """

    def __init__(
        self, display: "Display", info: "Info", window: "MainWindow", *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)

        self.display = display
        self.info = info
        self.window = window
        self._equation = ""
        self._equation_initial_value = "Sua Conta"
        self._left = None
        self._right = None
        self._operator = None

        self._grid_symbols = [
            ["C", "◀", "^", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["N", "0", ".", "="],
        ]

        self.equation = self._equation_initial_value
        self._make_grid()

    @property
    def equation(self):
        """
        This method returns the equation.
        """
        return self._equation

    @equation.setter
    def equation(self, value: str):
        """
        This method sets the equation.
        """
        self._equation = value
        self.info.setText(self._equation)

    def _make_grid(self):
        """
        This method creates the grid of buttons for the calculator.
        """
        self.display.equal_pressed.connect(self._equal)
        self.display.backspace_pressed.connect(self._backspace)
        self.display.clear_pressed.connect(self._clear)
        self.display.number_or_dot_pressed.connect(self._insert_to_display)
        self.display.operator_pressed.connect(self._config_left_operator)

        for row_id, row in enumerate(self._grid_symbols):
            for col_id, button_text in enumerate(row):
                if not button_text:
                    continue

                button = Button()
                button.setText(self._grid_symbols[row_id][col_id])

                if not is_num_or_dot(button_text) and not is_empty(button_text):
                    button.setProperty("cssClass", "specialButton")
                    self._config_special_button(button)

                if button_text == "N":
                    self.addWidget(button, row_id, col_id, 1, 1)

                else:
                    self.addWidget(button, row_id, col_id)

                slot = self._make_slot(self._insert_to_display, button_text)
                self._connect_button_clicked(button, slot)

    def _connect_button_clicked(self, button: Button, slot: Callable):
        """
        This method connects the button to the slot.
        """
        button.clicked.connect(slot)

    def _config_special_button(self, button: Button):
        """
        This method configures the special button.
        """
        text = button.text()

        if text == "C":
            self._connect_button_clicked(button, self._clear)

        if text == "◀":
            self._connect_button_clicked(button, self._backspace)

        if text in "+-/*^":
            self._connect_button_clicked(
                button, self._make_slot(self._config_left_operator, text)
            )

        if text == "N":
            self._connect_button_clicked(button, self._invert_number)
        if text == "=":
            self._connect_button_clicked(button, self._equal)

    def _make_slot(self, func: Callable, *args, **kwargs):
        """
        This method creates the slot.
        """

        @Slot(bool)
        def real_slot(_):
            func(*args, **kwargs)

        return real_slot

    @Slot()
    def _insert_to_display(self, text: str):
        """
        This method inserts a text to the display.
        """
        new_display_text = self.display.text() + text

        if is_valid_number(new_display_text):
            self.display.insert(text)

        self.display.setFocus()

    @Slot()
    def _clear(self):
        """
        This method clears the display.
        """
        self._left = None
        self._right = None
        self._operator = None
        self.display.clear()
        self.info.clear()
        self._equation = ""
        self.equation = self._equation_initial_value
        self.display.setFocus()

    @Slot()
    def _config_left_operator(self, text):
        """
        This method handles the operator button.
        """
        display_text = (
            self.display.text()
        )  # it will be the left number from the equation

        self.display.clear()
        self.display.setFocus()

        if not is_valid_number(display_text) and self._left is None:
            self._show_error("Você não digitou nada!")
            return

        if self._left is None:
            self._left = convert_to_number(display_text)

        self._operator = text
        self.equation = f"{self._left} {self._operator} ??"

        self.display.setFocus()

    @Slot()
    def _invert_number(self, *args):
        display_text = self.display.text()

        if not is_valid_number(display_text):
            return

        new_number = convert_to_number(display_text) * -1

        self.display.setText(str(new_number))

    @Slot()
    def _equal(self):
        """
        This method handles the equal button, which calculates the result.
        """
        display_text = self.display.text()

        if not is_valid_number(display_text) or self._operator is None:
            self._show_error("Conta incompleta!")
            return

        self._right = convert_to_number(display_text)
        self._equation = f"{self._left} {self._operator} {self._right}"
        result = "error"

        try:
            if "^" in self._equation and isinstance(self._left, (int, float)):
                result = math.pow(self._left, self._right)

            else:
                result = eval(self._equation)  # pylint: disable=eval-used

            result = str(result)

        except OverflowError:
            self._show_error(
                "Essa conta não pode ser realizada,"
                "não há memória o suficiente para realizar o cálculo!"
            )

        except ZeroDivisionError:
            self._show_error("Não é possível realizar a divisão por zero!")

        self.display.clear()
        self.display.setFocus()

        if result != "error":
            self._left = None
            self.info.setText(f"{self._equation} = {result}")
            self._right = None

        else:
            self._left = result

    def _make_dialog(self, message: str):
        msg_box = self.window.make_msg_box()
        msg_box.setText(message)

        return msg_box

    @Slot()
    def _backspace(self):
        """
        This method handles the backspace button.
        """
        self.display.backspace()
        self.display.setFocus()

    def _show_error(self, message: str):
        msg_box = self._make_dialog(message)
        msg_box.setIcon(msg_box.Icon.Critical)
        msg_box.exec()

    def _show_info(self, message: str):
        msg_box = self._make_dialog(message)
        msg_box.setIcon(msg_box.Icon.Information)
        msg_box.exec()

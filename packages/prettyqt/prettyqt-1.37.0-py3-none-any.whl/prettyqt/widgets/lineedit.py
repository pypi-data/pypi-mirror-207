from __future__ import annotations

from typing import Literal

from prettyqt import constants, core, gui, widgets
from prettyqt.qt import QtCore, QtGui, QtWidgets
from prettyqt.utils import InvalidParamError, bidict, get_repr


ECHO_MODE = bidict(
    normal=QtWidgets.QLineEdit.EchoMode.Normal,
    no_echo=QtWidgets.QLineEdit.EchoMode.NoEcho,
    password=QtWidgets.QLineEdit.EchoMode.Password,
    echo_on_edit=QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit,
)

EchoModeStr = Literal["normal", "no_echo", "password", "echo_on_edit"]

ACTION_POSITION = bidict(
    leading=QtWidgets.QLineEdit.ActionPosition.LeadingPosition,
    trailing=QtWidgets.QLineEdit.ActionPosition.TrailingPosition,
)

ActionPositionStr = Literal["leading", "trailing"]


class LineEdit(widgets.WidgetMixin, QtWidgets.QLineEdit):
    value_changed = core.Signal(str)
    tab_pressed = core.Signal()

    def __init__(
        self,
        default_value: str = "",
        read_only: bool = False,
        parent: QtWidgets.QWidget | None = None,
    ):
        super().__init__(default_value, parent)
        self.textChanged.connect(self._set_validation_color)
        self.textChanged.connect(self.value_changed)
        self.set_read_only(read_only)

    def __repr__(self):
        return get_repr(self, self.text())

    def __add__(self, other: str):
        self.append_text(other)
        return self

    def font(self) -> gui.Font:
        return gui.Font(super().font())

    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        if event.key() == QtCore.Qt.Key.Key_Tab:
            self.tab_pressed.emit()

    def append_text(self, text: str):
        self.set_text(self.text() + text)

    def set_text(self, text: str):
        self.setText(text)

    def set_completer(self, completer: QtWidgets.QCompleter | Literal["files"]):
        match completer:
            case QtWidgets.QCompleter():
                self.setCompleter(completer)
            case "files":
                model = widgets.FileSystemModel()
                model.set_root_path("")
                completer = widgets.Completer(self)
                completer.setModel(model)
                self.setCompleter(completer)

    def set_read_only(self, value: bool = True):
        """Set text to read-only.

        Args:
            value: True, for read-only, otherwise False
        """
        self.setReadOnly(value)

    def set_regex_validator(self, regex: str, flags=0) -> gui.RegularExpressionValidator:
        validator = gui.RegularExpressionValidator(self)
        validator.set_regex(regex, flags)
        self.set_validator(validator)
        return validator

    def set_range(self, lower: int | None, upper: int | None):
        val = gui.IntValidator()
        val.set_range(lower, upper)
        self.set_validator(val)

    def set_validator(self, validator: gui.Validator):
        self.setValidator(validator)
        self._set_validation_color()

    def set_input_mask(self, mask: str):
        match mask:
            case "ip_address":
                mask = "000.000.000.000;_"
            case "mac_address":
                mask = "HH:HH:HH:HH:HH:HH;_"
            case "iso_date":
                mask = "0000-00-00"
        self.setInputMask(mask)

    def _set_validation_color(self, state: bool = True):
        color = None if self.is_valid() else "orange"
        self.set_background_color(color)

    def set_echo_mode(self, mode: EchoModeStr):
        """Set echo mode.

        Args:
            mode: echo mode to use

        Raises:
            InvalidParamError: invalid echo mode
        """
        if mode not in ECHO_MODE:
            raise InvalidParamError(mode, ECHO_MODE)
        self.setEchoMode(ECHO_MODE[mode])

    def get_echo_mode(self) -> EchoModeStr:
        """Return echo mode.

        Returns:
            echo mode
        """
        return ECHO_MODE.inverse[self.echoMode()]

    def set_cursor_move_style(self, style: constants.CursorMoveStyleStr):
        """Set cursor move style.

        Args:
            style: cursor move style to use

        Raises:
            InvalidParamError: invalid cursor move style
        """
        if style not in constants.CURSOR_MOVE_STYLE:
            raise InvalidParamError(style, constants.CURSOR_MOVE_STYLE)
        self.setCursorMoveStyle(constants.CURSOR_MOVE_STYLE[style])

    def get_cursor_move_style(self) -> constants.CursorMoveStyleStr:
        """Return cursor move style.

        Returns:
            cursor move style
        """
        return constants.CURSOR_MOVE_STYLE.inverse[self.cursorMoveStyle()]

    def add_action(self, action: QtGui.QAction, position: ActionPositionStr = "trailing"):
        self.addAction(action, ACTION_POSITION[position])

    def set_value(self, value: str):
        self.setText(value)

    def get_value(self) -> str:
        return self.text()

    def is_valid(self) -> bool:
        return self.hasAcceptableInput()


if __name__ == "__main__":
    app = widgets.app()
    widget = LineEdit()
    action = gui.Action(text="hallo", icon="mdi.folder")
    # widget.add_action(action)
    widget.setPlaceholderText("test")
    widget.setClearButtonEnabled(True)
    widget.set_completer("files")
    # widget.set_regex_validator("[0-9]+")
    widget.setFont(gui.Font("Consolas"))
    widget.show()
    app.main_loop()

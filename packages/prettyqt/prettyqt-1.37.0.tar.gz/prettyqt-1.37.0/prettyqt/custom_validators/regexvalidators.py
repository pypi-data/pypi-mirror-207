from __future__ import annotations

from re import Pattern
from typing import Union

import regex as re

from prettyqt import gui
from prettyqt.qt import QtCore, QtGui
from prettyqt.utils import get_repr


PatternType = Union[str, Pattern]  # todo: move this to types?


class BaseRegexValidator(gui.Validator):
    def __init__(
        self, parent: QtCore.QObject | None = None, regex: PatternType | None = None
    ):
        super().__init__(parent)
        self.regex: Pattern | None = None
        if regex:
            self.set_regex(regex)

    def __repr__(self):
        return get_repr(self, self.get_regex())

    def __reduce__(self):
        return type(self), (self.get_regex(),)

    def __eq__(self, other: object):
        return self.regex == other.regex if isinstance(other, type(self)) else False

    def set_regex(self, regex: PatternType):
        self.regex = re.compile(regex) if isinstance(regex, str) else regex

    def get_regex(self) -> str:
        if self.regex is None:
            raise TypeError("Validator not initialized")
        return self.regex.pattern

    def validate(  # type: ignore
        self, text: str, pos: int = 0
    ) -> tuple[QtGui.QValidator.State, str, int]:
        if self.regex is None:
            raise TypeError("Validator not initialized")
        if not text:
            return self.State.Intermediate, text, pos
        match = self.regex.match(text, partial=True)  # type: ignore
        if match is None:
            return self.State.Invalid, text, pos
        elif match.partial:  # type: ignore
            return self.State.Intermediate, text, pos
        else:
            return self.State.Acceptable, text, pos


class IntListValidator(BaseRegexValidator):
    def __init__(self, allow_single: bool = True, parent: QtCore.QObject | None = None):
        super().__init__(parent=parent)
        self.allow_single = allow_single
        if allow_single:
            self.set_regex(r"^(\d+)(,\s*\d+)*$")
        else:
            self.set_regex(r"^[0-9][0-9\,]+[0-9]$")

    def __reduce__(self):
        return type(self), (self.allow_single,)

    def __repr__(self):
        return get_repr(self, allow_single=self.allow_single)


class FloatListValidator(BaseRegexValidator):
    def __init__(self, allow_single: bool = True, parent: QtCore.QObject | None = None):
        super().__init__(parent=parent)
        self.allow_single = allow_single
        if allow_single:
            self.set_regex(r"^(\s*-?\d+(\.\d+)?)(\s*,\s*-?\d+(\.\d+)?)*$")
        else:
            self.set_regex(
                r"^(\s*-?\d+(\.\d+)?)(\s*,\s*-?\d+(\.\d+)?)(\s*,\s*-?\d+(\.\d+)?)*$"
            )

    def __reduce__(self):
        return type(self), (self.allow_single,)

    def __repr__(self):
        return get_repr(self, allow_single=self.allow_single)


if __name__ == "__main__":
    from prettyqt import widgets

    app = widgets.app()
    w = widgets.LineEdit()
    val = BaseRegexValidator()
    val.set_regex(r"\w\d\d")
    w.set_validator(val)
    w.show()
    app.main_loop()

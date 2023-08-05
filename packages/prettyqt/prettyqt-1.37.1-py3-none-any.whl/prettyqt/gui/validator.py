from __future__ import annotations

from prettyqt import core
from prettyqt.qt import QtGui
from prettyqt.utils import get_repr


class ValidatorMixin(core.ObjectMixin):
    def __repr__(self):
        return get_repr(self)

    def __add__(self, other: Validator):
        from prettyqt import custom_validators

        return custom_validators.CompositeValidator([self, other])

    def __radd__(self, other: QtGui.QValidator):
        """Needed for sum()."""
        return self.__add__(other)

    def is_valid_value(self, value: str, pos: int = 0) -> bool:
        val = self.validate(value, pos)
        return val[0] == self.State.Acceptable  # type: ignore


class Validator(ValidatorMixin, QtGui.QValidator):
    pass


if __name__ == "__main__":
    val = Validator()

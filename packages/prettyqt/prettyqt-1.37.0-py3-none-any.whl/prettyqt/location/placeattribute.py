from __future__ import annotations

from prettyqt.qt import QtLocation
from prettyqt.utils import get_repr


class PlaceAttribute(QtLocation.QPlaceAttribute):
    def __init__(
        self,
        other_or_label: None | str | QtLocation.QPlaceAttribute = None,
        value: str | None = None,
    ):
        if isinstance(other_or_label, QtLocation.QPlaceAttribute):
            super().__init__(other_or_label)
        else:
            super().__init__()
            self.setLabel(other_or_label or "")
            self.setText(value or "")

    def __repr__(self):
        return get_repr(self, self.label(), self.text())

    def __str__(self):
        return f"{self.label()}: {self.text()}"

    def __bool__(self):
        return not self.isEmpty()


if __name__ == "__main__":
    attr = PlaceAttribute("test", "us")
    print(repr(attr))

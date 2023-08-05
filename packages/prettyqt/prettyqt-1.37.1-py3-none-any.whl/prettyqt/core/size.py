from __future__ import annotations

from typing_extensions import Self

from prettyqt.qt import QtCore
from prettyqt.utils import datatypes, get_repr


class Size(QtCore.QSize):
    def __repr__(self):
        return get_repr(self, self.width(), self.height())

    @property
    def _width(self):
        return self.width()

    @property
    def _height(self):
        return self.height()

    __match_args__ = ("_width", "_height")

    def __getitem__(self, index) -> int:
        return (self.width(), self.height())[index]

    def __reduce__(self):
        return type(self), (self.width(), self.height())

    def expanded_to(self, size: datatypes.SizeType) -> Self:
        if isinstance(size, tuple):
            size = QtCore.QSize(*size)
        return type(self)(self.expandedTo(size))

    def shrunk_by(self, margins: datatypes.MarginsType) -> Self:
        if isinstance(margins, tuple):
            margins = QtCore.QMargins(*margins)
        return type(self)(self.marginsAdded(margins))

    def grown_by(self, margins: datatypes.MarginsType) -> Self:
        if isinstance(margins, tuple):
            margins = QtCore.QMargins(*margins)
        return type(self)(self.marginsRemoved(margins))


if __name__ == "__main__":
    size = Size(10, 20)
    print(tuple(size))
    size = size.expanded_to(QtCore.QSize(100, 100))
    print(type(size))

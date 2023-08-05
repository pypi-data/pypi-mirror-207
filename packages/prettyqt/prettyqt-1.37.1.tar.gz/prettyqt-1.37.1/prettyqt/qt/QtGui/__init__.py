"""Provides QtGui classes and functions."""

from prettyqt.qt import PYQT6, PYSIDE6, PythonQtError


if PYQT6:
    from PyQt6.QtGui import *

    for cls in (QPalette,):
        for attr in dir(cls):
            if not attr[0].isupper():
                continue
            ns = getattr(cls, attr)
            for name, val in vars(ns).items():
                if not name.startswith("_"):
                    setattr(cls, name, val)

    def pos(self, *a):
        _pos = self.position(*a)
        return _pos.toPoint()

    QMouseEvent.pos = pos  # type: ignore
elif PYSIDE6:
    from PySide6.QtGui import *  # type: ignore
else:
    raise PythonQtError("No Qt bindings could be found")

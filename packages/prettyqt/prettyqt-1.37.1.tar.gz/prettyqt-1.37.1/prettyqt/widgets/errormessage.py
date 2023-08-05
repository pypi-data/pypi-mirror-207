from __future__ import annotations

from prettyqt import widgets
from prettyqt.qt import QtWidgets


class ErrorMessage(widgets.DialogMixin, QtWidgets.QErrorMessage):
    pass


if __name__ == "__main__":
    app = widgets.app()
    widget = ErrorMessage()
    widget.set_icon("mdi.timer")
    widget.show()
    app.main_loop()

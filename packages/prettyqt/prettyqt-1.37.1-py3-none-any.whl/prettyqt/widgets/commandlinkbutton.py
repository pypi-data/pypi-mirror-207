from __future__ import annotations

from prettyqt import core, widgets
from prettyqt.qt import QtWidgets


class CommandLinkButton(widgets.PushButtonMixin, QtWidgets.QCommandLinkButton):
    value_changed = core.Signal(bool)


if __name__ == "__main__":
    app = widgets.app()
    widget = CommandLinkButton("This is a test")
    widget.show()
    app.main_loop()

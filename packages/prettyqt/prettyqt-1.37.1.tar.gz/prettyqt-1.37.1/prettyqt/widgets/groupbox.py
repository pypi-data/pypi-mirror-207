from __future__ import annotations

from prettyqt import constants, widgets
from prettyqt.qt import QtWidgets
from prettyqt.utils import get_repr


class GroupBox(widgets.WidgetMixin, QtWidgets.QGroupBox):
    """GroupBox widget.

    A group box provides a frame, a title on top, a keyboard shortcut,
    and displays various other widgets inside itself.
    The keyboard shortcut moves keyboard focus to one of the group box's child widgets.
    """

    def __init__(
        self,
        title: str = "",
        checkable: bool = False,
        parent: QtWidgets.QWidget | None = None,
    ):
        super().__init__(title, parent)
        self.setCheckable(checkable)

    def __repr__(self):
        return get_repr(self, self.title())

    def set_title(self, title: str):
        self.setTitle(title)

    def set_alignment(self, alignment):
        self.setAlignment(constants.H_ALIGNMENT[alignment])

    def set_enabled(self, state):
        for widget in self.layout():
            widget.setEnabled(state)


if __name__ == "__main__":
    app = widgets.app()
    widget = GroupBox()
    ly = widgets.BoxLayout()
    ly += widgets.RadioButton("test")
    widget.set_layout(ly)
    widget.show()
    app.main_loop()

from __future__ import annotations

from prettyqt import gui, widgets
from prettyqt.qt import QtWidgets


class GraphicsColorizeEffect(
    widgets.GraphicsEffectMixin, QtWidgets.QGraphicsColorizeEffect
):
    def serialize_fields(self):
        return dict(strength=self.strength(), color=gui.Color(self.color()))

    def __setstate__(self, state):
        super().__setstate__(state)
        self.setStrength(state["strength"])
        self.setColor(state["color"])

from __future__ import annotations

from prettyqt import core, gui
from prettyqt.qt import QtGui
from prettyqt.utils import get_repr


class LinearGradient(gui.GradientMixin, QtGui.QLinearGradient):
    def __repr__(self):
        return get_repr(self, self.get_start(), self.get_final_stop())

    def serialize_fields(self):
        start = self.start()
        final_stop = self.finalStop()
        return dict(start=(start[0], start[1]), final_stop=(final_stop[0], final_stop[1]))

    def get_start(self) -> core.PointF:
        return core.PointF(self.start())

    def get_final_stop(self) -> core.PointF:
        return core.PointF(self.finalStop())

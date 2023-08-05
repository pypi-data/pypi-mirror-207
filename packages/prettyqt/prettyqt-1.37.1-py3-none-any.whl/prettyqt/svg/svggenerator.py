from __future__ import annotations

from prettyqt import core, gui
from prettyqt.qt import QtSvg


class SvgGenerator(gui.PaintDeviceMixin, QtSvg.QSvgGenerator):
    def get_viewbox(self) -> core.Rect:
        return core.Rect(self.viewBox())

    def get_viewboxf(self) -> core.RectF:
        return core.RectF(self.viewBoxF())

    def get_size(self) -> core.Size:
        return core.Size(self.size())

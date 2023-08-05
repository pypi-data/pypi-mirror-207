from __future__ import annotations

from prettyqt import constants, gui
from prettyqt.qt import QtGui
from prettyqt.utils import InvalidParamError, datatypes, get_repr, serializemixin


class Brush(serializemixin.SerializeMixin, QtGui.QBrush):
    def __repr__(self):
        return get_repr(self, self.get_color(), self.get_style())

    def get_texture_image(self) -> gui.Image | None:
        img = self.textureImage()
        return None if img.isNull() else gui.Image(img)

    def get_color(self) -> gui.Color:
        return gui.Color(self.color())

    def get_style(self) -> constants.BrushStyleStr:
        return constants.BRUSH_STYLE.inverse[self.style()]

    def set_style(self, style: constants.BrushStyleStr):
        if style not in constants.BRUSH_STYLE:
            raise InvalidParamError(style, constants.BRUSH_STYLE)
        self.setStyle(constants.BRUSH_STYLE[style])

    def set_transform(self, transform: datatypes.TransformType):
        if isinstance(transform, tuple):
            transform = gui.Transform(*transform)
        self.setTransform(transform)


if __name__ == "__main__":
    b = Brush()
    print(repr(b))

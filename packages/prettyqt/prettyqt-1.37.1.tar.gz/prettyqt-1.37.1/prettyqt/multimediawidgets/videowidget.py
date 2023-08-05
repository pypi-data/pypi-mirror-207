from __future__ import annotations

from prettyqt import widgets
from prettyqt.qt import QtCore, QtMultimediaWidgets


# QtMultimediaWidgets.QVideoWidget.__bases__ = (
#     widgets.Widget,
#     multimedia.MediaBindableInterface,
# )


class VideoWidget(widgets.WidgetMixin, QtMultimediaWidgets.QVideoWidget):
    def __init__(self, *args, **kwargs):
        self.doubleclick_for_fullscreen = False
        super().__init__(*args, **kwargs)

    def set_doubleclick_for_fullscreen(self, value: bool = True):
        self.doubleclick_for_fullscreen = value

    def mouseDoubleClickEvent(self, event):
        if (
            event.button() == QtCore.Qt.MouseButton.LeftButton
            and self.doubleclick_for_fullscreen
        ):
            self.setFullScreen(not self.isFullScreen())
            event.accept()
        return super().mouseDoubleClickEvent(event)


if __name__ == "__main__":
    app = widgets.app()
    widget = VideoWidget()
    widget.show()
    app.main_loop()

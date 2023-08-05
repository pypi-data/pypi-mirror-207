from __future__ import annotations

from prettyqt import widgets
from prettyqt.qt import QtGui, QtWidgets


class StatusBar(widgets.WidgetMixin, QtWidgets.QStatusBar):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.progress_bar = widgets.ProgressBar()

    def __add__(self, other: QtGui.QAction | QtWidgets.QWidget) -> StatusBar:
        match other:
            case QtGui.QAction():
                self.addAction(other)
                return self
            case QtWidgets.QWidget():
                self.addWidget(other)
                return self
            case _:
                raise TypeError(other)

    def setup_default_bar(self) -> None:
        # This is simply to show the bar
        self.progress_bar.hide()
        self.progress_bar.setRange(0, 0)
        self.progress_bar.setFixedSize(200, 20)
        self.progress_bar.setTextVisible(False)
        self.addPermanentWidget(self.progress_bar)

    def add_action(self, action: QtGui.QAction) -> None:
        self.addAction(action)

    def add_widget(self, widget: QtWidgets.QWidget, permanent: bool = False) -> None:
        if permanent:
            self.addPermanentWidget(widget)
        else:
            self.addWidget(widget)

    def show_message(self, message: str, timeout: int = 0) -> None:
        self.showMessage(message, timeout)


if __name__ == "__main__":
    app = widgets.app()
    dlg = widgets.MainWindow()
    status_bar = StatusBar()
    status_bar.set_color("black")
    label = widgets.Label("test")
    status_bar.addWidget(label)
    status_bar.setup_default_bar()
    dlg.setStatusBar(status_bar)
    dlg.show()
    app.main_loop()

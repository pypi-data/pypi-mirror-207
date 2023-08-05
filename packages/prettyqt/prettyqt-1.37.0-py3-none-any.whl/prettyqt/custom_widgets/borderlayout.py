from __future__ import annotations

from dataclasses import dataclass
import enum
from typing import Literal

from prettyqt import constants, core, widgets
from prettyqt.qt import QtCore, QtWidgets


@dataclass
class ItemWrapper:
    item: QtWidgets.QWidgetItem
    position: BorderLayout.Position


class BorderLayout(widgets.Layout):
    @core.Enum
    class Position(enum.IntEnum):
        """Item position."""

        West = 0
        North = 1
        South = 2
        East = 3
        Center = 4

    def __init__(
        self,
        parent: QtWidgets.QWidget | None = None,
        margin: int = 0,
        spacing: int | None = None,
    ):
        super().__init__(parent)  # type: ignore
        self.set_margin(margin)
        self.setSpacing(spacing if spacing is not None else -1)
        self.items: list[ItemWrapper] = []

    def __del__(self):
        item = self.takeAt(0)
        while item:
            item = self.takeAt(0)

    def addItem(self, item: QtWidgets.QWidgetItem):
        self.add_widgetitem(item, BorderLayout.Position.West)

    def addWidget(
        self,
        widget: QtWidgets.QWidget,
        position: Position | None = None,
    ):
        position = BorderLayout.Position.West if position is None else position
        self.add_widgetitem(widgets.WidgetItem(widget), position)

    def expandingDirections(self) -> QtCore.Qt.Orientation:
        return constants.HORIZONTAL | constants.VERTICAL  # type: ignore

    def hasHeightForWidth(self) -> bool:
        return False

    def count(self) -> int:
        return len(self.items)

    def itemAt(self, index: int) -> QtWidgets.QWidgetItem | None:  # type: ignore
        return self.items[index].item if index < len(self.items) else None

    def minimumSize(self):
        return self.calculate_size("minimum")

    def setGeometry(self, rect: QtCore.QRect):
        center = None
        east_width = 0
        west_width = 0
        north_height = 0
        south_height = 0

        super().setGeometry(rect)

        for wrapper in self.items:
            item = wrapper.item
            match wrapper.position:
                case BorderLayout.Position.North:
                    geom = core.Rect(
                        rect.x(), north_height, rect.width(), item.sizeHint().height()
                    )
                    item.setGeometry(geom)

                    north_height += item.geometry().height() + self.spacing()

                case BorderLayout.Position.South:
                    geom = core.Rect(
                        item.geometry().x(),
                        item.geometry().y(),
                        rect.width(),
                        item.sizeHint().height(),
                    )
                    item.setGeometry(geom)

                    south_height += item.geometry().height() + self.spacing()
                    geom = core.Rect(
                        rect.x(),
                        rect.y() + rect.height() - south_height + self.spacing(),
                        item.geometry().width(),
                        item.geometry().height(),
                    )
                    item.setGeometry(geom)

                case BorderLayout.Position.Center:
                    center = wrapper

        center_height = rect.height() - north_height - south_height

        for wrapper in self.items:
            item = wrapper.item
            match wrapper.position:
                case BorderLayout.Position.West:
                    geom = core.Rect(
                        rect.x() + west_width,
                        north_height,
                        item.sizeHint().width(),
                        center_height,
                    )
                    item.setGeometry(geom)

                    west_width += item.geometry().width() + self.spacing()

                case BorderLayout.Position.East:
                    geom = core.Rect(
                        item.geometry().x(),
                        item.geometry().y(),
                        item.sizeHint().width(),
                        center_height,
                    )
                    item.setGeometry(geom)

                    east_width += item.geometry().width() + self.spacing()

                    geom = core.Rect(
                        rect.x() + rect.width() - east_width + self.spacing(),
                        north_height,
                        item.geometry().width(),
                        item.geometry().height(),
                    )
                    item.setGeometry(geom)

        if center:
            rect = core.Rect(
                west_width,
                north_height,
                rect.width() - east_width - west_width,
                center_height,
            )
            center.item.setGeometry(rect)

    def sizeHint(self) -> core.Size:
        return self.calculate_size("size_hint")

    def takeAt(self, index: int) -> QtWidgets.QWidgetItem | None:  # type: ignore
        if 0 <= index < len(self.items):
            layout_struct = self.items.pop(index)
            return layout_struct.item

        return None

    def add_widgetitem(self, item: QtWidgets.QWidgetItem, position: Position):
        self.items.append(ItemWrapper(item, position))

    def calculate_size(self, size_type: Literal["minimum", "size_hint"]) -> core.Size:
        total_size = core.Size()

        for wrapper in self.items:
            item_size = (
                wrapper.item.minimumSize()
                if size_type == "minimum"
                else wrapper.item.sizeHint()
            )
            if wrapper.position in (
                BorderLayout.Position.North,
                BorderLayout.Position.South,
                BorderLayout.Position.Center,
            ):
                total_size.setHeight(total_size.height() + item_size.height())

            if wrapper.position in (
                BorderLayout.Position.West,
                BorderLayout.Position.East,
                BorderLayout.Position.Center,
            ):
                total_size.setWidth(total_size.width() + item_size.width())

        return total_size


if __name__ == "__main__":

    class Window(widgets.Widget):
        def __init__(self):
            super().__init__()

            central_widget = widgets.TextBrowser()
            central_widget.setPlainText("Central widget")

            layout = BorderLayout()
            layout.addWidget(central_widget, BorderLayout.Position.Center)

            # Because BorderLayout doesn't call its super-class addWidget() it
            # doesn't take ownership of the widgets until setLayout() is called.
            # Therefore we keep a local reference to each label to prevent it being
            # garbage collected too soon.
            label_n = self.create_label("North")
            layout.addWidget(label_n, BorderLayout.Position.North)

            label_w = self.create_label("West")
            layout.addWidget(label_w, BorderLayout.Position.West)

            label_e1 = self.create_label("East 1")
            layout.addWidget(label_e1, BorderLayout.Position.East)

            label_e2 = self.create_label("East 2")
            layout.addWidget(label_e2, BorderLayout.Position.East)

            label_s = self.create_label("South")
            layout.addWidget(label_s, BorderLayout.Position.South)

            self.setLayout(layout)

            self.setWindowTitle("Border Layout")

        @staticmethod
        def create_label(text: str):
            label = widgets.Label(text)
            label.setFrameStyle(widgets.Frame.Shape.Box | widgets.Frame.Shadow.Raised)
            return label

    app = widgets.app()
    window = Window()
    window.show()
    app.main_loop()

from __future__ import annotations

from collections.abc import Callable
from typing import Literal

from prettyqt import constants, gui, iconprovider, widgets
from prettyqt.qt import QtCore, QtWidgets
from prettyqt.utils import datatypes


AreaStr = Literal["top", "bottom"]


class SidebarWidget(widgets.MainWindow):
    SETTINGS_BUTTON_HEIGHT = 28

    def __init__(
        self,
        parent: QtWidgets.QWidget | None = None,
        show_settings: bool = False,
        main_layout: widgets.widget.LayoutStr | QtWidgets.QLayout = "vertical",
    ):
        super().__init__(parent=parent)
        self._button_width = 100
        self._style: constants.ToolButtonStyleStr = "text_below_icon"
        self.button_map: dict[QtWidgets.QWidget, QtWidgets.QToolButton] = {}
        self.icon_map: dict[QtWidgets.QWidget, gui.Icon] = {}
        self.sidebar = widgets.ToolBar()
        self.sidebar.set_id("SidebarWidget")
        self.sidebar.set_title("Sidebar")
        self.sidebar.set_style(self._style)
        self.sidebar.set_context_menu_policy("prevent")
        self.sidebar.setFloatable(False)
        self.sidebar.set_allowed_areas("all")
        self.settings_menu = widgets.Menu()
        self.sidebar.set_icon_size(int(self._button_width * 0.7))
        if show_settings:
            self.settings_btn = self.sidebar.add_menu_button(
                "", icon="mdi.wrench", menu=self.settings_menu
            )
            self.settings_btn.setFixedSize(
                self._button_width, self.SETTINGS_BUTTON_HEIGHT
            )
            self.settings_btn.set_style("icon")
            self.sidebar.orientationChanged.connect(self._on_orientation_change)
            self.sidebar.add_separator()
        self.spacer_action = self.sidebar.add_spacer()
        self.add_toolbar(self.sidebar, "left")
        self.area = widgets.Widget()
        self.area.set_layout("stacked")
        w = widgets.Widget()
        w.set_layout(main_layout)
        self.main_layout = w.box
        self.main_layout.set_margin(0)
        self.main_layout += self.area
        self.setCentralWidget(w)

    def _on_orientation_change(self, orientation: QtCore.Qt.Orientation):
        if orientation == constants.HORIZONTAL:
            self.settings_btn.setFixedSize(34, 34)
        else:
            self.settings_btn.setFixedSize(
                self._button_width, self.SETTINGS_BUTTON_HEIGHT
            )

    def add_tab(
        self,
        item: QtWidgets.QWidget,
        title: str,
        icon: datatypes.IconType | None = None,
        show: bool = False,
        shortcut: str | None = None,
        area: AreaStr = "top",
    ):
        self.area.box.add(item)
        act = gui.Action(
            text=title,
            icon=icon,
            shortcut=shortcut,
            parent=self.sidebar,
            checkable=True,
            callback=lambda: self.set_tab(item),
        )
        button = widgets.ToolButton(self.sidebar)
        button.setDefaultAction(act)
        button.setFixedWidth(self._button_width)
        button.set_style(self._style)
        if area == "top":
            self.sidebar.insertWidget(self.spacer_action, button)
        else:
            self.sidebar.addWidget(button)
        if len(self.area.box) == 1:
            button.setChecked(True)
        self.button_map[item] = button
        self.icon_map[item] = iconprovider.get_icon(icon)
        if show:
            self.area.box.setCurrentWidget(item)

    def set_marker(
        self, item: str | int | widgets.Widget, color: datatypes.ColorType = "red"
    ):
        widget = self._get_widget(item)
        if widget == self._get_current_widget():
            return
        template = self.icon_map[widget]
        px = template.pixmap(100, 100)
        with gui.Painter(px) as painter:
            dot = gui.Pixmap.create_dot(color)
            painter.drawPixmap(0, 0, dot)
        icon = gui.Icon(px)
        self.button_map[widget].setIcon(icon)

    def _get_widget(self, item: str | int | widgets.Widget):
        """Returns widget page specified by name, offset or content."""
        if isinstance(item, int):
            return self.area.box[item]
        elif isinstance(item, str):
            item = self.area.find_child(QtWidgets.QWidget, name=item, recursive=False)
            if item not in self.area.box:
                raise ValueError("Layout does not contain the chosen widget")
        return item

    def _get_current_widget(self) -> QtWidgets.QWidget:
        """Returns the currently selected widget page."""
        for k, v in self.button_map.items():
            if v.isChecked():
                return k
        raise RuntimeError("no page activated.")

    def set_tab(self, item: str | int | widgets.Widget):
        widget = self._get_widget(item)
        current = self.area.box.currentWidget()
        self.button_map[current].setChecked(False)
        self.area.box.setCurrentWidget(widget)
        self.button_map[widget].setChecked(True)

    def add_spacer(self) -> widgets.Widget:
        return self.sidebar.add_spacer()

    def add_separator(self, text: str | None = None, area: AreaStr = "top"):
        if area == "top":
            self.sidebar.add_separator(text, before=self.spacer_action)
        else:
            self.sidebar.add_separator(text)

    def add_action(
        self,
        title: str,
        icon: datatypes.IconType | None = None,
        callback: Callable | None = None,
        checkable: bool = False,
        shortcut: str | None = None,
        area: AreaStr = "top",
    ):
        act = gui.Action(
            text=title,
            icon=icon,
            shortcut=shortcut,
            checkable=checkable,
            callback=callback,
        )
        button = widgets.ToolButton(self.sidebar)
        button.setDefaultAction(act)
        button.setFixedWidth(self._button_width)
        button.set_style(self._style)
        if area == "top":
            self.sidebar.insertWidget(self.spacer_action, button)
        else:
            self.sidebar.addWidget(button)
        return act


if __name__ == "__main__":
    app = widgets.app()
    ex = SidebarWidget(show_settings=True)
    page_1 = widgets.PlainTextEdit()
    page_2 = widgets.ColorDialog()
    page_3 = widgets.FileDialog()
    ex.add_tab(page_1, "Text", "mdi.timer")
    ex.add_tab(page_2, "Color", "mdi.format-color-fill", area="bottom")
    ex.add_tab(page_3, "Help", "mdi.help-circle-outline")
    ex.set_marker(page_3)
    ex.show()
    app.main_loop()

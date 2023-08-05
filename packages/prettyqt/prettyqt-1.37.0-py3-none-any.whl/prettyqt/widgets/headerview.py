from __future__ import annotations

from collections.abc import Iterable
import functools
import hashlib
from typing import Literal

from prettyqt import constants, core, gui, widgets
from prettyqt.qt import QtCore, QtWidgets
from prettyqt.utils import InvalidParamError, bidict


MODES = bidict(
    interactive=QtWidgets.QHeaderView.ResizeMode.Interactive,
    fixed=QtWidgets.QHeaderView.ResizeMode.Fixed,
    stretch=QtWidgets.QHeaderView.ResizeMode.Stretch,
    resize_to_contents=QtWidgets.QHeaderView.ResizeMode.ResizeToContents,
)

ModeStr = Literal["interactive", "fixed", "stretch", "resize_to_contents"]


class HeaderViewMixin(widgets.AbstractItemViewMixin):
    section_vis_changed = core.Signal(int, bool)
    section_resized_by_user = core.Signal(int, int, int)

    def __init__(
        self,
        orientation: constants.OrientationStr | QtCore.Qt.Orientation,
        parent: QtWidgets.QWidget | None = None,
    ):
        if isinstance(orientation, QtCore.Qt.Orientation):
            ori = orientation
        else:
            ori = constants.ORIENTATION[orientation]
        super().__init__(ori, parent=parent)
        self.setSectionsMovable(True)
        self.setSectionsClickable(True)
        self.sectionResized.connect(self.sectionResizeEvent)
        self._handle_section_is_pressed = False
        self.setResizeContentsPrecision(100)
        self._widget_name = parent.objectName() if parent is not None else ""

    def set_sections_movable(self, value: bool, include_first: bool = False):
        self.setSectionsMovable(value)
        self.setFirstSectionMovable(include_first)

    def mousePressEvent(self, e):
        super().mousePressEvent(e)
        shape = self.get_cursor().get_shape()
        self._handle_section_is_pressed = shape == "split_horizontal"

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)
        self._handle_section_is_pressed = False

    def sectionResizeEvent(self, logical_index, old_size, new_size):
        if self._handle_section_is_pressed:
            self.section_resized_by_user.emit(logical_index, old_size, new_size)
        # do we need to call super() otherwise?

    def generate_header_id(self):
        # return f"{self._widget_name}.state"
        column_names = ",".join(self.get_section_labels())
        columns_hash = hashlib.md5(column_names.encode()).hexdigest()
        return f"{type(self).__name__}_{columns_hash}.state"

    def save_state(self, settings: core.Settings | None = None, key: str | None = None):
        settings = core.Settings() if settings is None else settings
        key = self.generate_header_id() if key is None else key
        settings.set_value(key, self.saveState())

    def load_state(
        self, settings: core.Settings | None = None, key: str | None = None
    ) -> bool:
        settings = core.Settings() if settings is None else settings
        key = self.generate_header_id() if key is None else key
        state = settings.get(key, None)
        if state is not None:
            if isinstance(state, str):
                state = state.encode()
            self.restoreState(state)
            return True
        return False

    def resize_sections(self, mode: ModeStr):
        self.resizeSections(MODES[mode])

    def get_resize_mode(self, col: int) -> ModeStr:
        val = self.sectionResizeMode(col)
        return MODES.inverse[val]

    def set_resize_mode(
        self,
        mode: ModeStr,
        col: int | None = None,
        precision: int | None = None,
        cascading: bool | None = None,
        stretch_last_section: bool | None = None,
        default_section_size: int | None = None,
        maximum_section_size: int | None = None,
        minimum_section_size: int | None = None,
    ):
        if col is not None:
            self.setSectionResizeMode(col, MODES[mode])
            return
        if stretch_last_section is not None:
            self.stretchLastSection(stretch_last_section)
        if minimum_section_size is not None:
            self.setMinimumSectionSize(minimum_section_size)
        if default_section_size is not None:
            self.setDefaultSectionSize(default_section_size)
        if maximum_section_size is not None:
            self.setMaximumSectionSize(maximum_section_size)
        if precision is not None:
            self.setResizeContentsPrecision(precision)
        if cascading is not None:
            self.setCascadingSectionResizes(cascading)
        if mode not in MODES:
            raise InvalidParamError(mode, MODES)
        self.setSectionResizeMode(MODES[mode])

    def get_section_labels(self) -> list[str]:
        model = self.model()
        return [
            model.headerData(
                i, constants.HORIZONTAL, constants.DISPLAY_ROLE  # type: ignore
            )
            for i in range(self.count())
        ]

    def contextMenuEvent(self, event):
        """Context menu for our files tree."""
        menu = self.createPopupMenu()
        menu.exec(self.mapToGlobal(event.pos()))

    def get_header_actions(self) -> list[gui.Action]:
        menu = self.createPopupMenu()
        return menu.actions()

    def createPopupMenu(self) -> widgets.Menu:
        menu = widgets.Menu(parent=self)
        actions = []
        labels = self.get_section_labels()[1:]
        for i, header_label in enumerate(labels, start=1):
            val = not self.isSectionHidden(i)
            action = gui.Action(text=header_label, checkable=True, checked=val)
            fn = functools.partial(self.set_section_hidden, i=i, hide=val)
            action.triggered.connect(fn)
            actions.append(action)
        menu.add_actions(actions)
        return menu

    def set_section_hidden(self, i: int, hide: bool):
        self.section_vis_changed.emit(i, hide)
        self.setSectionHidden(i, hide)

    def set_sizes(self, sizes: Iterable[int | None]):
        for i, size in enumerate(sizes):
            if size is not None:
                self.resizeSection(i, size)

    def set_default_section_size(self, size: int | None):
        if size is None:
            self.resetDefaultSectionSize()
        else:
            self.setDefaultSectionSize(size)

    def stretch_last_section(self, stretch: bool = True):
        self.setStretchLastSection(stretch)

    def get_default_alignment(self) -> constants.AlignmentStr:
        return constants.ALIGNMENTS.inverse[self.defaultAlignment()]

    def get_orientation(self) -> constants.OrientationStr:
        """Return current orientation.

        Returns:
            orientation
        """
        return constants.ORIENTATION.inverse[self.orientation()]


class HeaderView(HeaderViewMixin, QtWidgets.QHeaderView):
    pass


if __name__ == "__main__":
    app = widgets.app()
    header = HeaderView("horizontal")
    header.show()
    app.main_loop()

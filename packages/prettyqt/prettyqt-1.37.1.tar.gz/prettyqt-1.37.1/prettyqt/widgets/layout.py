from __future__ import annotations

from collections.abc import Iterator
from typing import Literal

from deprecated import deprecated

from prettyqt import constants, core, widgets
from prettyqt.qt import QtCore, QtWidgets
from prettyqt.utils import InvalidParamError, bidict, get_repr


SIZE_CONSTRAINT = bidict(
    default=QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint,
    fixed=QtWidgets.QLayout.SizeConstraint.SetFixedSize,
    minimum=QtWidgets.QLayout.SizeConstraint.SetMinimumSize,
    maximum=QtWidgets.QLayout.SizeConstraint.SetMaximumSize,
    min_and_max=QtWidgets.QLayout.SizeConstraint.SetMinAndMaxSize,
    none=QtWidgets.QLayout.SizeConstraint.SetNoConstraint,
)

SizeConstraintStr = Literal[
    "default", "fixed", "minimum", "maximum", "min_and_max", "none"
]


class LayoutMixin(core.ObjectMixin, widgets.LayoutItemMixin):
    def __getitem__(
        self, index: str | int
    ) -> QtWidgets.QWidget | QtWidgets.QLayout | None:
        if isinstance(index, int):
            item = self.itemAt(index)
            widget = item.widget()
            if widget is None:
                widget = item.layout()
        elif isinstance(index, str):
            return self.find_child(typ=QtCore.QObject, name=index)
        return widget

    def __delitem__(self, index: int):
        item = self.itemAt(index)
        self.removeItem(item)

    def __len__(self) -> int:
        return self.count()

    def __repr__(self):
        return get_repr(self)

    def __iter__(self) -> Iterator[QtWidgets.QWidget | QtWidgets.QLayout | None]:
        return iter(self[i] for i in range(self.count()))

    def __contains__(self, item: QtWidgets.QWidget | QtWidgets.QLayoutItem):
        return self.indexOf(item) >= 0

    def serialize_fields(self):
        return dict(
            size_mode=self.get_size_mode(),
            spacing=self.spacing(),
            enabled=self.isEnabled(),
        )

    def get_children(self) -> list[QtWidgets.QWidget | QtWidgets.QLayout]:
        return list(self)

    def set_margin(self, margin: int | None):
        if margin is None:
            self.unsetContentsMargins()
        else:
            self.setContentsMargins(margin, margin, margin, margin)

    def set_spacing(self, pixels: int):
        self.setSpacing(pixels)

    @deprecated(reason="Use set_size_constraint instead")
    def set_size_mode(self, mode: SizeConstraintStr):
        self.set_size_constraint(mode)

    def set_size_constraint(self, mode: SizeConstraintStr):
        """Set the size mode of the layout.

        Args:
            mode: size mode for the layout

        Raises:
            InvalidParamError: size mode does not exist
        """
        if mode not in SIZE_CONSTRAINT:
            raise InvalidParamError(mode, SIZE_CONSTRAINT)
        self.setSizeConstraint(SIZE_CONSTRAINT[mode])

    @deprecated(reason="Use set_size_constraint instead")
    def get_size_mode(self) -> SizeConstraintStr:
        return self.get_size_constraint()

    def get_size_constraint(self) -> SizeConstraintStr:
        """Return current size mode.

        Returns:
            size mode
        """
        return SIZE_CONSTRAINT.inverse[self.sizeConstraint()]

    def set_alignment(
        self,
        alignment: constants.AlignmentStr,
        item: QtWidgets.QWidget | QtWidgets.QLayout | None = None,
    ) -> bool:
        """Set the alignment for widget / layout to alignment.

        Returns true if w is found in this layout (not including child layouts).

        Args:
            alignment: alignment for the layout
            item: set alignment for specific child only

        Raises:
            InvalidParamError: alignment does not exist
        """
        if alignment not in constants.ALIGNMENTS:
            raise InvalidParamError(alignment, constants.ALIGNMENTS)
        if item is not None:
            return self.setAlignment(item, constants.ALIGNMENTS[alignment])
        else:
            return self.setAlignment(constants.ALIGNMENTS[alignment])

    def add_widget(self, widget: QtWidgets.QWidget, *args, **kwargs):
        self.addWidget(widget, *args, **kwargs)

    def add(self, *items: QtWidgets.QWidget | QtWidgets.QLayout):
        for i in items:
            match i:
                case QtWidgets.QWidget():
                    self.addWidget(i)
                case QtWidgets.QLayout():
                    w = widgets.Widget()
                    w.set_layout(i)
                    self.addWidget(w)
                case _:
                    raise TypeError("add_item only supports widgets and layouts")


class Layout(LayoutMixin, QtWidgets.QLayout):
    pass

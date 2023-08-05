from __future__ import annotations

from prettyqt import constants, gui, iconprovider
from prettyqt.qt import QtCore, QtWidgets
from prettyqt.utils import InvalidParamError, datatypes, get_repr, serializemixin


class ListWidgetItem(serializemixin.SerializeMixin, QtWidgets.QListWidgetItem):
    def __repr__(self):
        return get_repr(self, self.icon(), self.text())

    def __setitem__(self, index: int, value):
        self.setData(index, value)

    def __getitem__(self, index: int):
        return self.data(index)

    def serialize_fields(self):
        return dict(
            text=self.text(),
            tool_tip=self.toolTip(),
            status_tip=self.statusTip(),
            checkstate=self.get_checkstate(),
            icon=self.get_icon(),
            data=self.data(constants.USER_ROLE),  # type: ignore
        )

    def set_icon(self, icon: datatypes.IconType):
        """Set the icon for the action.

        Args:
            icon: icon to use
        """
        icon = iconprovider.get_icon(icon)
        self.setIcon(icon)

    def set_checkstate(self, state: constants.StateStr):
        """Set checkstate of the checkbox.

        Args:
            state: checkstate to use

        Raises:
            InvalidParamError: invalid checkstate
        """
        if state not in constants.STATE:
            raise InvalidParamError(state, constants.STATE)
        self.setCheckState(constants.STATE[state])

    def get_checkstate(self) -> constants.StateStr:
        """Return checkstate.

        Returns:
            checkstate
        """
        return constants.STATE.inverse[self.checkState()]

    def get_background(self) -> gui.Brush:
        return gui.Brush(self.background())

    def get_foreground(self) -> gui.Brush:
        return gui.Brush(self.foreground())

    def get_font(self) -> gui.Font:
        return gui.Font(self.font())

    def get_icon(self) -> gui.Icon | None:
        icon = self.icon()
        return None if icon.isNull() else gui.Icon(icon)

    def set_data(self, role: str, data):
        role_id = constants.ITEM_DATA_ROLE[role]
        self.setData(role_id, data)

    def set_size_hint(self, hint: datatypes.SizeType):
        if isinstance(hint, tuple):
            hint = QtCore.QSize(*hint)
        self.setSizeHint(hint)

    def set_text_alignment(
        self,
        horizontal: constants.HorizontalAlignmentStr | None = None,
        vertical: constants.VerticalAlignmentStr | None = None,
    ):
        """Set text alignment of the checkbox.

        Args:
            horizontal: horizontal text alignment to use
            vertical: vertical text alignment to use

        Raises:
            InvalidParamError: invalid text alignment
        """
        match horizontal, vertical:
            case None, None:
                return
            case None, _:
                flag = constants.V_ALIGNMENT[vertical]
            case _, None:
                flag = constants.H_ALIGNMENT[horizontal]
            case _, _:
                flag = constants.V_ALIGNMENT[vertical] | constants.H_ALIGNMENT[horizontal]
        self.setTextAlignment(flag)


if __name__ == "__main__":
    from prettyqt import widgets

    app = widgets.app()
    widget = widgets.ListWidget()
    item = ListWidgetItem("AB")
    item.set_data("display", "test")
    widget.add(item)
    widget.show()
    app.main_loop()

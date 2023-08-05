from __future__ import annotations

from typing import Literal

from typing_extensions import Self

from prettyqt import gui
from prettyqt.qt import QtGui
from prettyqt.utils import (
    InvalidParamError,
    bidict,
    colors,
    datatypes,
    get_repr,
    serializemixin,
)


ROLE = bidict(
    window=QtGui.QPalette.ColorRole.Window,  # same as Background
    window_text=QtGui.QPalette.ColorRole.WindowText,  # same as Foreground
    base=QtGui.QPalette.ColorRole.Base,
    alternate_base=QtGui.QPalette.ColorRole.AlternateBase,
    tool_tip_base=QtGui.QPalette.ColorRole.ToolTipBase,
    tool_tip_text=QtGui.QPalette.ColorRole.ToolTipText,
    placeholder_text=QtGui.QPalette.ColorRole.PlaceholderText,
    text=QtGui.QPalette.ColorRole.Text,
    button=QtGui.QPalette.ColorRole.Button,
    button_text=QtGui.QPalette.ColorRole.ButtonText,
    bright_text=QtGui.QPalette.ColorRole.BrightText,
    light=QtGui.QPalette.ColorRole.Light,
    midlight=QtGui.QPalette.ColorRole.Midlight,
    dark=QtGui.QPalette.ColorRole.Dark,
    mid=QtGui.QPalette.ColorRole.Mid,
    shadow=QtGui.QPalette.ColorRole.Shadow,
    highlight=QtGui.QPalette.ColorRole.Highlight,
    highlighted_text=QtGui.QPalette.ColorRole.HighlightedText,
    link=QtGui.QPalette.ColorRole.Link,
    link_visited=QtGui.QPalette.ColorRole.LinkVisited,
    none=QtGui.QPalette.ColorRole.NoRole,
)

RoleStr = Literal[
    "window",
    "window_text",
    "base",
    "alternate_base",
    "tool_tip_base",
    "tool_tip_text",
    "placeholder_text",
    "text",
    "button",
    "button_text",
    "bright_text",
    "light",
    "midlight",
    "dark",
    "mid",
    "shadow",
    "highlight",
    "highlighted_text",
    "link",
    "link_visited",
    "none",
]

GROUP = bidict(
    disabled=QtGui.QPalette.ColorGroup.Disabled,
    active=QtGui.QPalette.ColorGroup.Active,  # normal
    inactive=QtGui.QPalette.ColorGroup.Inactive,
)

GroupStr = Literal["disabled", "active", "inactive"]


class Palette(serializemixin.SerializeMixin, QtGui.QPalette):
    def __getitem__(self, index: RoleStr) -> gui.Color:
        return self.get_color(index)

    def __setitem__(self, index: RoleStr, value: datatypes.ColorType):
        self.set_color(index, value)

    def __repr__(self):
        return get_repr(self, self.get_color("button"), self.get_color("window"))

    def highlight_inactive(self):
        color = self.color(self.ColorGroup.Active, self.ColorRole.Highlight)
        self.setColor(self.ColorGroup.Inactive, self.ColorRole.Highlight, color)

    def set_color(
        self, role: RoleStr, color: datatypes.ColorType, group: GroupStr = "active"
    ):
        color = colors.get_color(color)
        self.setColor(GROUP[group], ROLE[role], color)

    def get_colors(self, group: GroupStr = "active") -> dict[str, gui.Color]:
        return {k: self.get_color(k, group) for k in ROLE}

    def get_color(self, role: RoleStr, group: GroupStr = "active") -> gui.Color:
        return gui.Color(self.color(GROUP[group], ROLE[role]))

    def set_brush(
        self,
        role: RoleStr,
        brush: datatypes.ColorAndBrushType,
        group: GroupStr = "active",
    ):
        if not isinstance(brush, QtGui.QBrush):
            brush = gui.Brush(colors.get_color(brush))
        self.setBrush(GROUP[group], ROLE[role], brush)

    def get_brushes(self, group: GroupStr = "active") -> dict[str, gui.Brush]:
        return {k: self.get_brush(k, group) for k in ROLE}

    def get_brush(self, role: RoleStr, group: GroupStr = "active") -> gui.Brush:
        return gui.Brush(self.brush(GROUP[group], ROLE[role]))

    def set_color_group(self, group: GroupStr, **kwargs: QtGui.QBrush):
        """Set the color group.

        Args:
            group: color group to use
            kwargs: keyword arguments passed to setColorGroup

        Raises:
            InvalidParamError: invalid color group
        """
        if group not in GROUP:
            raise InvalidParamError(group, GROUP)
        self.setColorGroup(GROUP[group], **kwargs)

    def get_color_group(self) -> GroupStr:
        """Return color group.

        Returns:
            color group
        """
        return GROUP.inverse[self.colorGroup()]

    def inverted(self) -> Self:
        pal = type(self)()
        for group in GROUP:
            for role in ROLE:
                color = self.get_color(role, group)
                pal.set_color(role, color.inverted(), group)
        return pal

    @classmethod
    def create_dark_palette(cls) -> Self:
        pal = cls()
        pal.set_color("window", gui.Color(53, 53, 53))
        pal.set_color("window_text", "white")
        pal.set_color("window_text", "grey", group="disabled")
        pal.set_color("base", gui.Color(25, 25, 25))
        pal.set_color("alternate_base", gui.Color(53, 53, 53))
        pal.set_color("tool_tip_base", "slategrey")
        pal.set_color("tool_tip_base", "slategrey", group="inactive")
        pal.set_color("tool_tip_text", "white")
        pal.set_color("tool_tip_text", "white", group="inactive")
        pal.set_color("text", "white")
        pal.set_color("text", "grey", group="disabled")
        pal.set_color("button", gui.Color(53, 53, 53))
        pal.set_color("button_text", "white")
        pal.set_color("button_text", "grey", group="disabled")
        pal.set_color("bright_text", "red")
        pal.set_color("link", "dodgerblue")
        pal.set_color("highlight", "dodgerblue")
        pal.set_color("highlight", gui.Color(80, 80, 80), group="disabled")
        pal.set_color("highlighted_text", "black")
        pal.set_color("highlighted_text", "grey", group="disabled")
        return pal

    def is_dark(self) -> bool:
        col = self.color(self.ColorRole.Window)
        return max(col.getRgb()[:3]) < 115


if __name__ == "__main__":
    pal = Palette()
    print(pal.get_colors())

from __future__ import annotations

from typing import Literal

from prettyqt import core, gui
from prettyqt.qt import QtCharts
from prettyqt.utils import bidict, get_repr


VALUE_POSITION = bidict(
    lower_extreme=QtCharts.QBoxSet.ValuePositions.LowerExtreme,
    lower_quartile=QtCharts.QBoxSet.ValuePositions.LowerQuartile,
    median=QtCharts.QBoxSet.ValuePositions.Median,
    upper_quartile=QtCharts.QBoxSet.ValuePositions.UpperQuartile,
    upper_extreme=QtCharts.QBoxSet.ValuePositions.UpperExtreme,
)

ValuePositionStr = Literal[
    "lower_extreme", "lower_quartile", "median", "upper_quartile", "upper_extreme"
]


class BoxSet(core.ObjectMixin, QtCharts.QBoxSet):
    def __repr__(self):
        return get_repr(
            self,
            self["lower_extreme"],
            self["lower_quartile"],
            self["median"],
            self["upper_quartile"],
            self["upper_extreme"],
            self.label(),
        )

    def __getitem__(self, index: int | ValuePositionStr) -> float:
        val = VALUE_POSITION[index] if isinstance(index, str) else index
        if not (0 <= val.value <= 4):
            raise KeyError(val)
        return self.at(val.value)

    def __setitem__(self, index: int | ValuePositionStr, value: int):
        val = VALUE_POSITION[index] if isinstance(index, str) else index
        if not (0 <= val.value <= 4):
            raise KeyError(val)
        self.setValue(val.value, value)

    def get_pen(self) -> gui.Pen:
        return gui.Pen(self.pen())

    def get_brush(self) -> gui.Brush:
        return gui.Brush(self.brush())


if __name__ == "__main__":
    boxset = BoxSet()
    print(repr(boxset))

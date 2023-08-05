from __future__ import annotations

from collections.abc import Callable
from typing import overload

from prettyqt import core
from prettyqt.qt import QtCore


class AnimationGroupMixin(core.AbstractAnimationMixin):
    @overload
    def __getitem__(self, index: int) -> QtCore.QAbstractAnimation:
        ...

    @overload
    def __getitem__(self, index: slice) -> list[QtCore.QAbstractAnimation]:
        ...

    def __getitem__(self, index: int | slice):
        if isinstance(index, int):
            if index < 0:
                index = self.animationCount() + index
            anim = self.animationAt(index)
            if anim is None:
                raise KeyError(index)
            return anim
        else:
            anims = [self.animationAt(i) for i in range(len(self))]
            return anims[index]

    def __setitem__(self, index: int, value: QtCore.QAbstractAnimation):
        if not (0 <= index < self.animationCount()):
            raise KeyError(index)
        self.takeAnimation(index)
        self.insertAnimation(index, value)

    def __len__(self):
        return self.animationCount()

    def __delitem__(self, index: int):
        if not (0 <= index < self.animationCount()):
            raise KeyError(index)
        self.takeAnimation(index)

    def __add__(self, other: QtCore.QAbstractAnimation):
        self.addAnimation(other)
        return self

    def add_property_animation(self, obj: Callable) -> core.PropertyAnimation:
        anim = core.PropertyAnimation()
        anim.apply_to(obj)
        self.addAnimation(anim)
        return anim


class AnimationGroup(AnimationGroupMixin, QtCore.QAnimationGroup):
    pass


if __name__ == "__main__":
    group = AnimationGroup()
    a1 = core.PauseAnimation()
    a2 = core.PauseAnimation()
    group += a1
    group += a2
    sliced = group[:2]

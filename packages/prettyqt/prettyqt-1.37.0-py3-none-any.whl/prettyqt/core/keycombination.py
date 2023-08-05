from __future__ import annotations

from prettyqt import constants
from prettyqt.qt import QtCore
from prettyqt.utils import serializemixin


class KeyCombination(serializemixin.SerializeMixin, QtCore.QKeyCombination):
    def __init__(self, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0], str) and args[0] in constants.KEY:
            super().__init__(constants.KEY[args[0]], **kwargs)
        else:
            super().__init__(*args, **kwargs)

    def get_key(self) -> constants.KeyStr:
        return constants.KEY.inverse[self.key()]

    def get_modifiers(self) -> list[constants.KeyboardmodifierStr]:
        return constants.KEYBOARD_MODIFIERS.get_list(self.modifiers())


if __name__ == "__main__":
    seq = KeyCombination("a")

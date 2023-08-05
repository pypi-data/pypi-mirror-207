from __future__ import annotations

from prettyqt import constants, core, gui
from prettyqt.qt import QtCore, QtGui
from prettyqt.utils import InvalidParamError


class Shortcut(core.ObjectMixin, QtGui.QShortcut):
    def __init__(self, *args, **kwargs):
        if args and isinstance(args[0], str):
            args = (gui.KeySequence(args[0]), *args[1:])
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.key().toString()

    def serialize_field(self):
        return dict(
            auto_repeat=self.autoRepeat(),
            context=self.get_context(),
            enabled=self.isEnabled(),
            key=self.get_key(),
            whats_this=self.whatsThis(),
        )

    def set_context(self, context: constants.ShortcutContextStr):
        """Set shortcut context.

        Args:
            context: shortcut context

        Raises:
            InvalidParamError: shortcut context does not exist
        """
        if context not in constants.SHORTCUT_CONTEXT:
            raise InvalidParamError(context, constants.SHORTCUT_CONTEXT)
        self.setContext(constants.SHORTCUT_CONTEXT[context])

    def get_context(self) -> constants.ShortcutContextStr:
        """Return shortcut context.

        Returns:
            shortcut context
        """
        return constants.SHORTCUT_CONTEXT.inverse[self.context()]

    def set_key(
        self,
        key: str
        | QtCore.QKeyCombination
        | QtCore.QKeySequence
        | QtGui.QKeySequence.StandardKey,
    ):
        keysequence = gui.KeySequence(key)
        self.setKey(keysequence)

    def set_keys(
        self,
        keys: list[
            str
            | QtCore.QKeyCombination
            | QtCore.QKeySequence
            | QtGui.QKeySequence.StandardKey
        ],
    ):
        keysequences = [gui.KeySequence(key) for key in keys]
        self.setKeys(keysequences)

    def get_key(self) -> gui.KeySequence:
        """Return the shortcut's key sequence.

        Returns:
            Key sequence
        """
        return gui.KeySequence(self.key())

    def get_keys(self) -> list[gui.KeySequence]:
        return [gui.KeySequence(i) for i in self.keys()]


if __name__ == "__main__":
    shortcut = Shortcut("enter", None)
    shortcut.get_key()

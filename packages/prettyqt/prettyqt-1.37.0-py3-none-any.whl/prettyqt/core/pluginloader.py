from __future__ import annotations

from typing import Literal

from prettyqt import core
from prettyqt.qt import QtCore


LoadHintStr = Literal[
    "resolve_all_symbols",
    "export_external_symbols",
    "load_archive_member",
    "prevent_unload",
    "deep_bind",
]


class PluginLoader(core.ObjectMixin, QtCore.QPluginLoader):
    def get_load_hints(self) -> list[LoadHintStr]:
        return core.library.LOAD_HINTS.get_list(self.loadHints())

    def set_load_hints(self, **kwargs):
        flag = QtCore.QLibrary.LoadHint(0)  # type: ignore
        for k, v in kwargs.items():
            if v is True:
                flag |= core.library.LOAD_HINTS[k]  # type: ignore
        self.setLoadHints(flag)  # type: ignore

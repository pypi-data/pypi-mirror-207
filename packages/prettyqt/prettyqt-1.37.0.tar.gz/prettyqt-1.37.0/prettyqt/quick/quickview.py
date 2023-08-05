from __future__ import annotations

import os
import pathlib
from typing import Literal

from prettyqt import core, quick
from prettyqt.qt import QtQuick
from prettyqt.utils import bidict, datatypes


RESIZE_MODES = bidict(
    view_to_root_object=QtQuick.QQuickView.ResizeMode.SizeViewToRootObject,
    root_object_to_view=QtQuick.QQuickView.ResizeMode.SizeRootObjectToView,
)

ResizeModeStr = Literal["view_to_root_object", "root_object_to_view"]

STATUS = bidict(
    null=QtQuick.QQuickView.Status.Null,
    ready=QtQuick.QQuickView.Status.Ready,
    loading=QtQuick.QQuickView.Status.Loading,
    error=QtQuick.QQuickView.Status.Error,
)

StatusStr = Literal["null", "ready", "loading", "error"]


class QuickView(quick.quickwindow.QuickWindowMixin, QtQuick.QQuickView):
    def set_source(self, source: datatypes.UrlType | datatypes.PathType):
        if isinstance(source, os.PathLike):
            source = os.fspath(source)
        if isinstance(source, str):
            source = core.Url.fromLocalFile(source)
        self.setSource(source)

    def get_source(self) -> pathlib.Path:
        return pathlib.Path(self.source().toLocalFile())

    def get_status(self) -> StatusStr:
        return STATUS.inverse[self.status()]

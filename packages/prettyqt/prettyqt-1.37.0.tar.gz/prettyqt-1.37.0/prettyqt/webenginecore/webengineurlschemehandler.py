from __future__ import annotations

from prettyqt import core
from prettyqt.qt import QtWebEngineCore


class WebEngineUrlSchemeHandler(
    core.ObjectMixin, QtWebEngineCore.QWebEngineUrlSchemeHandler
):
    pass


if __name__ == "__main__":
    item = WebEngineUrlSchemeHandler()

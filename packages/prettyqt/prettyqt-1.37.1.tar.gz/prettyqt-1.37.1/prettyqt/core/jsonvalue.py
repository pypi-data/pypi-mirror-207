from __future__ import annotations

from prettyqt.qt import QtCore
from prettyqt.utils import get_repr


class JsonValue(QtCore.QJsonValue):
    def __str__(self):
        return str(self.toVariant())

    def __repr__(self):
        return get_repr(self, self.toVariant())


if __name__ == "__main__":
    from prettyqt import core

    doc = core.JsonDocument.from_variant(dict(a="b"))
    print(doc.toVariant())
    print(doc)
    new = core.JsonDocument()
    new.setObject(doc.object())
    val = doc["a"]
    print(type(val), val)

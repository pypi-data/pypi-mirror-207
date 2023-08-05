"""Provides QtCore classes and functions."""

from __future__ import annotations

import datetime

from prettyqt.qt import PYQT6, PYSIDE6

# sys.setrecursionlimit(2000)


def to_datetime(self) -> datetime.datetime:
    return self.toPyDateTime()


def to_date(self) -> datetime.date:
    return self.toPyDate()


def to_time(self) -> datetime.time:
    return self.toPyTime()


if PYQT6:
    from PyQt6.QtCore import (
        QT_VERSION_STR,
        QT_VERSION_STR as __version__,
        QDateTime,
        QDate,
        QTime,
        pyqtBoundSignal,
        pyqtBoundSignal as SignalInstance,
        pyqtProperty,
        pyqtProperty as Property,
        pyqtSignal,
        pyqtSignal as Signal,
        pyqtSlot,
        pyqtSlot as Slot,
        pyqtEnum,
        pyqtEnum as QEnum,
        pyqtEnum as QFlag,
        pyqtClassInfo,
        pyqtClassInfo as QClassInfo,
        Q_ARG,
        Q_ARG as QGenericArgument,
        PYQT_VERSION_STR as BINDING_VERSION,
        QtMsgType,
    )

    QtCriticalMsg = QtMsgType.QtCriticalMsg
    QtDebugMsg = QtMsgType.QtDebugMsg
    QtFatalMsg = QtMsgType.QtFatalMsg
    QtInfoMsg = QtMsgType.QtInfoMsg
    QtSystemMsg = QtMsgType.QtSystemMsg
    QtWarningMsg = QtMsgType.QtWarningMsg

    # For issue #153
    from PyQt6.QtCore import *

    QDateTime.toPython = to_datetime
    QDate.toPython = to_date
    QTime.toPython = to_time
    QCoreApplication.exec_ = QCoreApplication.exec  # type: ignore
    QLibraryInfo.location = QLibraryInfo.path  # type: ignore
    # Those are imported from `import *`
    del (
        pyqtSignal,
        pyqtBoundSignal,
        pyqtSlot,
        pyqtProperty,
        QT_VERSION_STR,
        pyqtEnum,
        Q_ARG,
        pyqtClassInfo,
    )
    for cls in (QEvent, Qt):
        for attr in dir(cls):
            if not attr[0].isupper():
                continue
            ns = getattr(cls, attr)
            for name, val in vars(ns).items():
                if not name.startswith("_"):
                    setattr(cls, name, val)
elif PYSIDE6:
    from PySide6.QtCore import *  # type: ignore
    from PySide6.QtCore import __version__  # type: ignore
    from PySide6 import __version__ as BINDING_VERSION

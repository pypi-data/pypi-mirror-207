from __future__ import annotations

from collections.abc import Callable
import logging
import os
import pathlib
import sys

from prettyqt import constants, core
from prettyqt.qt import QtCore
from prettyqt.utils import InvalidParamError, datatypes


logger = logging.getLogger(__name__)


class CoreApplicationMixin(core.ObjectMixin):
    translators: dict[str, core.Translator] = {}

    @classmethod
    def call_on_exit(cls, func: Callable):
        instance = cls.instance()
        if instance is None:
            raise RuntimeError("No QApplication running")
        instance.aboutToQuit.connect(func)

    @classmethod
    def get_application_file_path(cls) -> pathlib.Path:
        return pathlib.Path(cls.applicationFilePath())

    @classmethod
    def get_application_dir_path(cls) -> pathlib.Path:
        return pathlib.Path(cls.applicationDirPath())

    @classmethod
    def add_library_path(cls, path: datatypes.PathType):
        cls.addLibraryPath(os.fspath(path))

    @classmethod
    def get_library_paths(cls) -> list[pathlib.Path]:
        return [pathlib.Path(i) for i in cls.libraryPaths()]

    @classmethod
    def disable_window_help_button(cls, state: bool = True):
        try:
            aa = QtCore.Qt.ApplicationAttribute
            attr = aa.AA_DisableWindowContextHelpButton  # type: ignore
            cls.setAttribute(attr, state)
        except AttributeError:  # attribute not available in Qt6
            pass

    def set_metadata(
        self,
        app_name: str | None = None,
        app_version: None | datatypes.SemanticVersionType = None,
        org_name: str | None = None,
        org_domain: str | None = None,
    ):
        if app_name is not None:
            self.setApplicationName(app_name)
        if app_version is not None:
            if isinstance(app_version, QtCore.QVersionNumber):
                app_version = app_version.toString()
            elif isinstance(app_version, tuple):
                app_version = ".".join(str(i) for i in app_version)
            self.setApplicationVersion(app_version)
        if org_name is not None:
            self.setOrganizationName(org_name)
        if org_domain is not None:
            self.setOrganizationDomain(org_domain)
        # if sys.platform.startswith("win"):
        #     import ctypes
        #     myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
        #     ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    @classmethod
    def load_language_file(cls, file: datatypes.PathType) -> core.Translator:
        translator = core.Translator()
        translator.load_file(file)
        cls.installTranslator(translator)
        cls.translators[str(file)] = translator
        return translator

    @classmethod
    def load_language(cls, language: str) -> core.Translator:
        translator = core.Translator.for_language(language)
        cls.installTranslator(translator)
        cls.translators[language] = translator
        return translator

    def post_event(
        self,
        obj: QtCore.QObject,
        event: QtCore.QEvent,
        priority: int | constants.EventPriorityStr = "normal",
    ):
        if isinstance(priority, int):
            prio = priority
        elif priority in constants.EVENT_PRIORITY:
            prio = constants.EVENT_PRIORITY[priority]
        else:
            raise InvalidParamError(priority, constants.EVENT_PRIORITY)
        return self.postEvent(obj, event, prio)

    def main_loop(self) -> int:
        return self.exec()

    @staticmethod
    def restart():
        os.execl(sys.executable, sys.executable, *sys.argv)


class CoreApplication(CoreApplicationMixin, QtCore.QCoreApplication):
    pass

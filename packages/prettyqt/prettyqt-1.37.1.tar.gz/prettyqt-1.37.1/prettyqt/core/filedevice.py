from __future__ import annotations

import datetime
from typing import Literal

import dateutil.parser

from prettyqt import core
from prettyqt.qt import QtCore
from prettyqt.utils import InvalidParamError, bidict, datatypes, get_repr


FILE_ERROR = bidict(
    none=QtCore.QFileDevice.FileError.NoError,
    read=QtCore.QFileDevice.FileError.ReadError,
    write=QtCore.QFileDevice.FileError.WriteError,
    fatal=QtCore.QFileDevice.FileError.FatalError,
    resource=QtCore.QFileDevice.FileError.ResourceError,
    open=QtCore.QFileDevice.FileError.OpenError,
    abort=QtCore.QFileDevice.FileError.AbortError,
    time_out=QtCore.QFileDevice.FileError.TimeOutError,
    unspecified=QtCore.QFileDevice.FileError.UnspecifiedError,
    remove=QtCore.QFileDevice.FileError.RemoveError,
    rename=QtCore.QFileDevice.FileError.RenameError,
    position=QtCore.QFileDevice.FileError.PositionError,
    resize=QtCore.QFileDevice.FileError.ResizeError,
    permissions=QtCore.QFileDevice.FileError.PermissionsError,
    copy=QtCore.QFileDevice.FileError.CopyError,
)

FileErrorStr = Literal[
    "none",
    "read",
    "write",
    "fatal",
    "resource",
    "open",
    "abort",
    "time_out",
    "unspecified",
    "remove",
    "rename",
    "position",
    "resize",
    "permissions",
    "copy",
]

FILE_TIME = bidict(
    access=QtCore.QFileDevice.FileTime.FileAccessTime,
    birth=QtCore.QFileDevice.FileTime.FileBirthTime,
    metadata_change=QtCore.QFileDevice.FileTime.FileMetadataChangeTime,
    modification=QtCore.QFileDevice.FileTime.FileModificationTime,
)

FileTimeStr = Literal["access", "birth", "metadata_change", "modification"]

PERMISSIONS = bidict(
    read_owner=QtCore.QFileDevice.Permission.ReadOwner,
    write_owner=QtCore.QFileDevice.Permission.WriteOwner,
    exe_owner=QtCore.QFileDevice.Permission.ExeOwner,
    read_user=QtCore.QFileDevice.Permission.ReadUser,
    write_user=QtCore.QFileDevice.Permission.WriteUser,
    exe_user=QtCore.QFileDevice.Permission.ExeUser,
    read_group=QtCore.QFileDevice.Permission.ReadGroup,
    write_group=QtCore.QFileDevice.Permission.WriteGroup,
    exe_group=QtCore.QFileDevice.Permission.ExeGroup,
    read_other=QtCore.QFileDevice.Permission.ReadOther,
    write_other=QtCore.QFileDevice.Permission.WriteOther,
    exe_other=QtCore.QFileDevice.Permission.ExeOther,
)

PermissionStr = Literal[
    "read_owner",
    "write_owner",
    "exe_owner",
    "read_user",
    "write_user",
    "exe_user",
    "read_group",
    "write_group",
    "exe_group",
    "read_other",
    "write_other",
    "exe_other",
]


class FileDeviceMixin(core.IODeviceMixin):
    def __repr__(self):
        return get_repr(self, self.fileName())

    def __str__(self):
        return self.fileName()

    def get_permissions(self) -> list[PermissionStr]:
        return PERMISSIONS.get_list(self.permissions())

    def set_file_time(self, file_time: datatypes.DateTimeType, typ: FileTimeStr) -> bool:
        """Set file time.

        Args:
            file_time: file time to set
            typ: file time type

        Raises:
            InvalidParamError: file time does not exist
        """
        if isinstance(file_time, str):
            file_time = dateutil.parser.parse(file_time)
        if typ not in FILE_TIME:
            raise InvalidParamError(typ, FILE_TIME)
        return self.setFileTime(file_time, FILE_TIME[typ])  # type: ignore

    def get_file_time(self, typ: FileTimeStr) -> datetime.datetime | None:
        """Return current file time.

        Returns:
            file time
        """
        if typ not in FILE_TIME:
            raise InvalidParamError(typ, FILE_TIME)
        if date := self.fileTime(FILE_TIME[typ]):
            return date.toPython()  # type: ignore

    def get_error(self) -> FileErrorStr:
        """Return file error status.

        Returns:
            file error status
        """
        return FILE_ERROR.inverse[self.error()]


class FileDevice(FileDeviceMixin, QtCore.QFileDevice):
    pass

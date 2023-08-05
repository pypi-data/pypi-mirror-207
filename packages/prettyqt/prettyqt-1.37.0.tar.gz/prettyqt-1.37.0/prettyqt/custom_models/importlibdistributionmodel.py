from __future__ import annotations

from collections.abc import Sequence
from importlib import metadata
import pkgutil

from typing_extensions import Self

from prettyqt import constants, core, custom_models
from prettyqt.qt import QtCore
from prettyqt.utils import treeitem


def load_dist_info(name: str) -> metadata.Distribution | None:
    try:
        return metadata.distribution(name)
    except metadata.PackageNotFoundError:
        return None


def list_system_modules() -> list[metadata.Distribution]:
    modules = (test.name for test in pkgutil.iter_modules())
    distributions = (load_dist_info(i) for i in modules)
    return [i for i in distributions if i is not None]


def list_package_requirements(package_name: str) -> list[metadata.Distribution]:
    dist = metadata.distribution(package_name)
    modules = {i.split(" ")[0] for i in dist.requires} if dist.requires else set()
    distributions = (load_dist_info(i) for i in modules)
    return [i for i in distributions if i is not None]


COL_NAME = custom_models.ColumnItem(
    name="Name",
    doc="Package name",
    label=lambda x: x.obj.metadata["Name"],
)

COL_VERSION = custom_models.ColumnItem(
    name="Version",
    doc="Version number.",
    label=lambda x: x.obj.version,
)

COL_SUMMARY = custom_models.ColumnItem(
    name="Summary",
    doc="Module description.",
    label=lambda x: x.obj.metadata["Summary"],
)

COL_HOMEPAGE = custom_models.ColumnItem(
    name="Homepage",
    doc="Homepage URL.",
    label=lambda x: x.obj.metadata["Home-Page"],
)

COL_AUTHOR = custom_models.ColumnItem(
    name="Author",
    doc="Author name.",
    label=lambda x: x.obj.metadata["Author"],
)

COL_LICENSE = custom_models.ColumnItem(
    name="License",
    doc="License type.",
    label=lambda x: x.obj.metadata["License"],
)

COLUMNS = [COL_NAME, COL_VERSION, COL_SUMMARY, COL_HOMEPAGE, COL_AUTHOR, COL_LICENSE]


class ImportlibTreeModel(custom_models.ColumnItemModel):
    """Model that provides an interface to an objectree that is build of tree items."""

    def __init__(
        self,
        obj: metadata.Distribution,
        show_root: bool = False,
        parent: QtCore.QObject | None = None,
    ):
        super().__init__(obj=obj, columns=COLUMNS, parent=parent, show_root=show_root)

    @classmethod
    def from_system(cls, parent: QtCore.QObject | None = None) -> Self:
        distributions = list_system_modules()
        return cls(distributions, parent)

    @classmethod
    def from_package(
        cls, package_name: str, parent: QtCore.QObject | None = None
    ) -> Self:
        distributions = list_package_requirements(package_name)
        return cls(distributions, parent)

    def hasChildren(self, parent: core.ModelIndex | None = None):
        parent = core.ModelIndex() if parent is None else parent
        if parent.column() > 0:
            return False
        if self.show_root and self.tree_item(parent) == self._root_item:
            return True
        return bool(self.tree_item(parent).obj.requires)

    def _fetch_object_children(self, item: treeitem.TreeItem) -> list[treeitem.TreeItem]:
        """Fetch the children of a Python object.

        Returns: list of treeitem.TreeItems
        """
        return [
            treeitem.TreeItem(obj=dist, parent=item)
            for dist in list_package_requirements(item.obj.metadata["Name"])
        ]


class ImportlibDistributionModel(core.AbstractTableModel):
    HEADER = ["Name", "Version", "Summary", "Homepage", "Author", "License"]

    def __init__(
        self,
        distributions: Sequence[metadata.Distribution],
        parent: QtCore.QObject | None = None,
    ):
        super().__init__(parent)
        self.distributions = distributions

    def rowCount(self, parent=None):
        return 0 if parent is not None else len(self.distributions)

    def columnCount(self, parent=None):
        return 0 if parent is not None else len(self.HEADER)

    def headerData(self, offset: int, orientation, role):  # type: ignore
        match orientation, role:
            case constants.HORIZONTAL, constants.DISPLAY_ROLE:
                return self.HEADER[offset]

    def data(self, index, role=constants.DISPLAY_ROLE):
        dist = self.distributions[index.row()]
        match role, index.column():
            case constants.DISPLAY_ROLE, 0:
                return dist.metadata["Name"]
            case constants.DISPLAY_ROLE, 1:
                return dist.version
            case constants.DISPLAY_ROLE, 2:
                return dist.metadata["Summary"]
            case constants.DISPLAY_ROLE, 3:
                return dist.metadata["Home-Page"]
            case constants.DISPLAY_ROLE, 4:
                return dist.metadata["Author"]
            case constants.DISPLAY_ROLE, 5:
                return dist.metadata["License"]
            case constants.USER_ROLE, _:
                return dist

    @classmethod
    def from_system(cls, parent: QtCore.QObject | None = None) -> Self:
        distributions = list_system_modules()
        return cls(distributions, parent)

    @classmethod
    def from_package(
        cls, package_name: str, parent: QtCore.QObject | None = None
    ) -> Self:
        distributions = list_package_requirements(package_name)
        return cls(distributions, parent)


# if __name__ == "__main__":
#     from prettyqt import widgets

#     app = widgets.app()
#     modules = list_system_modules()
#     tableview = widgets.TableView()
#     model = ImportlibDistributionModel.from_package("prettyqt")
#     tableview.set_model(model)
#     tableview.show()
#     app.main_loop()


if __name__ == "__main__":
    from prettyqt import widgets

    app = widgets.app()
    dist = metadata.distribution("prettyqt")
    model = ImportlibTreeModel(dist, show_root=False)
    table = widgets.TreeView()
    table.setRootIsDecorated(True)
    # table.setSortingEnabled(True)
    table.set_model(model)
    table.show()
    app.main_loop()

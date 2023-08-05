from __future__ import annotations

import datetime
from typing import Literal

import dateutil.parser

from prettyqt import core, widgets
from prettyqt.qt import QtWidgets
from prettyqt.utils import InvalidParamError, bidict, datatypes


SECTIONS = bidict(
    none=QtWidgets.QDateTimeEdit.Section.NoSection,
    am_pm=QtWidgets.QDateTimeEdit.Section.AmPmSection,
    msec=QtWidgets.QDateTimeEdit.Section.MSecSection,
    second=QtWidgets.QDateTimeEdit.Section.SecondSection,
    minute=QtWidgets.QDateTimeEdit.Section.MinuteSection,
    hour=QtWidgets.QDateTimeEdit.Section.HourSection,
    day=QtWidgets.QDateTimeEdit.Section.DaySection,
    month=QtWidgets.QDateTimeEdit.Section.MonthSection,
    year=QtWidgets.QDateTimeEdit.Section.YearSection,
)

SectionsStr = Literal[
    "none",
    "am_pm",
    "msec",
    "second",
    "minute",
    "hour",
    "day",
    "month",
    "year",
]


class DateTimeEditMixin(widgets.AbstractSpinBoxMixin):
    value_changed = core.Signal(datetime.datetime)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setCalendarPopup(True)
        self.dateTimeChanged.connect(self.datetime_changed)

    def datetime_changed(self, date):
        dt = self.get_datetime()
        self.value_changed.emit(dt)

    def get_section_text(self, section: SectionsStr) -> str:
        if section not in SECTIONS:
            raise InvalidParamError(section, SECTIONS)
        return self.sectionText(SECTIONS[section])

    def get_current_section(self) -> SectionsStr:
        return SECTIONS.inverse[self.currentSection()]

    def set_current_section(self, section: SectionsStr):
        if section not in SECTIONS:
            raise InvalidParamError(section, SECTIONS)
        self.setCurrentSection(SECTIONS[section])

    def get_displayed_sections(self) -> list[SectionsStr]:
        return SECTIONS.get_list(self.displayedSections())

    def set_range(
        self,
        lower: datatypes.DateTimeType,
        upper: datatypes.DateTimeType,
    ):
        if isinstance(lower, str):
            lower = dateutil.parser.parse(lower)
        if isinstance(upper, str):
            upper = dateutil.parser.parse(upper)
        self.setToolTip(f"{lower} <= x <= {upper}")
        self.setDateTimeRange(lower, upper)  # type: ignore

    def set_format(self, fmt: str):
        self.setDisplayFormat(fmt)

    def get_value(self) -> datetime.datetime:
        return self.get_datetime()

    def set_value(self, value: datetime.datetime):
        self.setDateTime(value)  # type: ignore

    def get_datetime(self) -> datetime.datetime:
        return self.dateTime().toPython()  # type: ignore

    def min_datetime(self) -> datetime.datetime:
        return self.minimumDateTime().toPython()  # type: ignore

    def max_datetime(self) -> datetime.datetime:
        return self.maximumDateTime().toPython()  # type: ignore

    def min_date(self) -> datetime.date:
        return self.minimumDate().toPython()  # type: ignore

    def max_date(self) -> datetime.date:
        return self.maximumDate().toPython()  # type: ignore

    def get_date(self) -> datetime.date:
        return self.date().toPython()  # type: ignore

    def min_time(self) -> datetime.time:
        return self.minimumTime().toPython()  # type: ignore

    def max_time(self) -> datetime.time:
        return self.maximumTime().toPython()  # type: ignore

    def get_time(self) -> datetime.time:
        return self.time().toPython()  # type: ignore


class DateTimeEdit(DateTimeEditMixin, QtWidgets.QDateTimeEdit):
    pass


if __name__ == "__main__":
    app = widgets.app()
    widget = DateTimeEdit()
    widget.show()
    app.main_loop()

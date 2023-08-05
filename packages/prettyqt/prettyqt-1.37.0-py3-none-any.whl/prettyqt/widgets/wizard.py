from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING, Literal

from prettyqt import core, gui, widgets
from prettyqt.qt import QtCore, QtGui, QtWidgets
from prettyqt.utils import InvalidParamError, bidict


if TYPE_CHECKING:
    from collections.abc import Iterator


mod = QtWidgets.QWizard

WIZARD_BUTTON = bidict(
    back=mod.WizardButton.BackButton,
    next=mod.WizardButton.NextButton,
    commit=mod.WizardButton.CommitButton,
    finish=mod.WizardButton.FinishButton,
    cancel=mod.WizardButton.CancelButton,
    help=mod.WizardButton.HelpButton,
    custom_1=mod.WizardButton.CustomButton1,
    custom_2=mod.WizardButton.CustomButton2,
    custom_3=mod.WizardButton.CustomButton3,
)

WizardButtonStr = Literal[
    "back",
    "next",
    "commit",
    "finish",
    "cancel",
    "help",
    "custom_1",
    "custom_2",
    "custom_3",
]

WIZARD_OPTIONS = bidict(
    independent_pages=mod.WizardOption.IndependentPages,
    ignore_subtitles=mod.WizardOption.IgnoreSubTitles,
    extended_watermark_bitmap=mod.WizardOption.ExtendedWatermarkPixmap,
    no_default_button=mod.WizardOption.NoDefaultButton,
    no_back_button_on_start_page=mod.WizardOption.NoBackButtonOnStartPage,
    no_back_button_on_last_page=mod.WizardOption.NoBackButtonOnLastPage,
    disabled_back_button_on_last_page=mod.WizardOption.DisabledBackButtonOnLastPage,
    next_button_on_last_page=mod.WizardOption.HaveNextButtonOnLastPage,
    finish_button_on_early_pages=mod.WizardOption.HaveFinishButtonOnEarlyPages,
    no_cancel_button=mod.WizardOption.NoCancelButton,
    cancel_button_on_left=mod.WizardOption.CancelButtonOnLeft,
    help_button=mod.WizardOption.HaveHelpButton,
    help_button_on_right=mod.WizardOption.HelpButtonOnRight,
    custom_button_1=mod.WizardOption.HaveCustomButton1,
    custom_button_2=mod.WizardOption.HaveCustomButton2,
    custom_button_3=mod.WizardOption.HaveCustomButton3,
    no_cancel_button_on_last_page=mod.WizardOption.NoCancelButtonOnLastPage,
)

WizardOptionStr = Literal[
    "independent_pages",
    "ignore_subtitles",
    "extended_watermark_bitmap",
    "no_default_button",
    "no_back_button_on_start_page",
    "no_back_button_on_last_page",
    "disabled_back_button_on_last_page",
    "next_button_on_last_page",
    "finish_button_on_early_pages",
    "no_cancel_button",
    "cancel_button_on_left",
    "help_button",
    "help_button_on_right",
    "custom_button_1",
    "custom_button_2",
    "custom_button_3",
    "no_cancel_button_on_last_page",
]

WIZARD_PIXMAP = bidict(
    watermark=mod.WizardPixmap.WatermarkPixmap,
    logo=mod.WizardPixmap.LogoPixmap,
    banner=mod.WizardPixmap.BannerPixmap,
    background=mod.WizardPixmap.BackgroundPixmap,
)

WizardPixmapStr = Literal["watermark", "logo", "banner", "background"]

WIZARD_STYLE = bidict(
    classic=mod.WizardStyle.ClassicStyle,
    modern=mod.WizardStyle.ModernStyle,
    mac=mod.WizardStyle.MacStyle,
    aero=mod.WizardStyle.AeroStyle,
)

WizardStyleStr = Literal["classic", "modern", "mac", "aero"]

TEXT_FORMATS = bidict(
    rich=QtCore.Qt.TextFormat.RichText,
    plain=QtCore.Qt.TextFormat.PlainText,
    auto=QtCore.Qt.TextFormat.AutoText,
    markdown=QtCore.Qt.TextFormat.MarkdownText,
)

TextFormatStr = Literal["rich", "plain", "auto", "markdown"]


class WizardMixin(widgets.DialogMixin):
    custom_button_1_clicked = core.Signal()
    custom_button_2_clicked = core.Signal()
    custom_button_3_clicked = core.Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.customButtonClicked.connect(self._on_custom_button_clicked)

    def __getitem__(self, key: int) -> QtWidgets.QWizardPage:
        p = self.page(key)
        if p is None:
            raise KeyError(key)
        return p

    def __setitem__(self, key: int, value: QtWidgets.QWizardPage):
        return self.setPage(key, value)

    def __delitem__(self, key: int):
        if key not in self.pageIds():
            raise KeyError(key)
        return self.removePage(key)

    def __iter__(self) -> Iterator[QtWidgets.QWizardPage]:
        return iter(self.page(i) for i in self.pageIds())

    def __add__(self, other: QtWidgets.QWizardPage) -> Wizard:
        self.addPage(other)
        return self

    def _on_custom_button_clicked(self, which: int):
        match which:
            case 6:
                self.custom_button_1_clicked.emit()
            case 7:
                self.custom_button_2_clicked.emit()
            case 8:
                self.custom_button_3_clicked.emit()

    def serialize_fields(self):
        return dict(
            current_id=self.currentId(),
            start_id=self.startId(),
            sub_title_format=self.get_subtitle_format(),
            title_format=self.get_title_format(),
            wizard_style=self.get_wizard_style(),
        )

    def add_widget_as_page(self, widget: QtWidgets.QWidget) -> None:
        page = widgets.WizardPage(self)
        layout = widgets.BoxLayout("vertical", self)
        layout += widget
        page.set_layout(layout)

    def set_title_format(self, fmt: TextFormatStr):
        """Set the title format.

        Allowed values are "rich", "plain", "auto", "markdown"

        Args:
            fmt: title format to use

        Raises:
            InvalidParamError: title format does not exist
        """
        if fmt not in TEXT_FORMATS:
            raise InvalidParamError(fmt, TEXT_FORMATS)
        self.setTitleFormat(TEXT_FORMATS[fmt])

    def get_title_format(self) -> TextFormatStr:
        """Return current title format.

        Possible values: "rich", "plain", "auto", "markdown"

        Returns:
            title format
        """
        return TEXT_FORMATS.inverse[self.titleFormat()]

    def set_subtitle_format(self, fmt: TextFormatStr):
        """Set the subtitle format.

        Allowed values are "rich", "plain", "auto", "markdown"

        Args:
            fmt: subtitle format to use

        Raises:
            InvalidParamError: subtitle format does not exist
        """
        if fmt not in TEXT_FORMATS:
            raise InvalidParamError(fmt, TEXT_FORMATS)
        self.setSubTitleFormat(TEXT_FORMATS[fmt])

    def get_subtitle_format(self) -> TextFormatStr:
        """Return current subtitle format.

        Possible values: "rich", "plain", "auto", "markdown"

        Returns:
            subtitle format
        """
        return TEXT_FORMATS.inverse[self.subTitleFormat()]

    def get_button(self, button_type: WizardButtonStr) -> QtWidgets.QAbstractButton:
        if button_type not in WIZARD_BUTTON:
            raise InvalidParamError(button_type, WIZARD_BUTTON)
        return self.button(WIZARD_BUTTON[button_type])

    def set_button_text(self, button_type: WizardButtonStr, value: str):
        """Set text for given button type.

        Args:
            button_type: button to get text from
            value: text to set

        """
        if button_type not in WIZARD_BUTTON:
            raise InvalidParamError(button_type, WIZARD_BUTTON)
        self.setButtonText(WIZARD_BUTTON[button_type], value)

    def get_button_text(self, button_type: WizardButtonStr) -> str:
        """Return text for given button type.

        Args:
            button_type: button to get text from

        Returns:
            Button text
        """
        if button_type not in WIZARD_BUTTON:
            raise InvalidParamError(button_type, WIZARD_BUTTON)
        return self.buttonText(WIZARD_BUTTON[button_type])

    def set_pixmap(self, typ: WizardPixmapStr, pixmap: QtGui.QPixmap | None):
        if typ not in WIZARD_PIXMAP:
            raise InvalidParamError(typ, WIZARD_PIXMAP)
        if pixmap is None:
            pixmap = QtGui.QPixmap()
        self.setPixmap(WIZARD_PIXMAP[typ], pixmap)

    def get_pixmap(self, typ: WizardPixmapStr) -> gui.Pixmap | None:
        if typ not in WIZARD_PIXMAP:
            raise InvalidParamError(typ, WIZARD_PIXMAP)
        pix = gui.Pixmap(self.pixmap(WIZARD_PIXMAP[typ]))
        return None if pix.isNull() else pix

    def set_wizard_style(self, style: WizardStyleStr):
        """Set the wizard style.

        Args:
            style: wizard style

        Raises:
            InvalidParamError: wizard style does not exist
        """
        if style not in WIZARD_STYLE:
            raise InvalidParamError(style, WIZARD_STYLE)
        self.setWizardStyle(WIZARD_STYLE[style])

    def get_wizard_style(self) -> WizardStyleStr:
        """Return current wizard style.

        Returns:
            Wizard style
        """
        return WIZARD_STYLE.inverse[self.wizardStyle()]

    def set_option(self, option: WizardOptionStr, value: bool):
        """Set option to given value.

        Args:
            option: option to use
            value: value to set

        Raises:
            InvalidParamError: option does not exist
        """
        if option not in WIZARD_OPTIONS:
            raise InvalidParamError(option, WIZARD_OPTIONS)
        self.setOption(WIZARD_OPTIONS[option], value)

    def get_option(self, option: WizardOptionStr) -> bool:
        """Return the value assigned to option.

        Args:
            option: option to get

        Returns:
            option
        """
        if option not in WIZARD_OPTIONS:
            raise InvalidParamError(option, WIZARD_OPTIONS)
        return self.testOption(WIZARD_OPTIONS[option])

    def set_custom_button(
        self, button: Literal[1, 2, 3], text: str | None, callback: Callable | None = None
    ):
        self.set_option(f"custom_button_{button}", text is not None)
        if text is None:
            return
        self.setButtonText(WIZARD_BUTTON[f"custom_{button}"], text)
        if callback:
            match button:
                case 1:
                    self.custom_button_1_clicked.connect(callback)
                case 2:
                    self.custom_button_2_clicked.connect(callback)
                case 3:
                    self.custom_button_3_clicked.connect(callback)


class Wizard(WizardMixin, QtWidgets.QWizard):
    pass


if __name__ == "__main__":
    app = widgets.app()
    dlg = Wizard()
    dlg.add_widget_as_page(widgets.RadioButton("test"))
    dlg.set_custom_button(1, "1", lambda: print("1"))
    dlg.set_custom_button(2, "2", lambda: print("2"))
    dlg.set_custom_button(3, "3", lambda: print("3"))
    dlg.show()
    app.main_loop()

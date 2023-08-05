from __future__ import annotations

from typing import Literal

from prettyqt import bluetooth, core
from prettyqt.qt import QtBluetooth
from prettyqt.utils import bidict, get_repr


mod = QtBluetooth.QBluetoothDeviceInfo

CORE_CONFIGURATION = bidict(
    none=mod.CoreConfiguration.UnknownCoreConfiguration,
    base_rate=mod.CoreConfiguration.BaseRateCoreConfiguration,
    base_rate_and_low_energy=mod.CoreConfiguration.BaseRateAndLowEnergyCoreConfiguration,
    low_energy=mod.CoreConfiguration.LowEnergyCoreConfiguration,
)

CoreConfigurationStr = Literal[
    "none", "base_rate", "base_rate_and_low_energy", "low_energy"
]

FIELD = bidict(
    none=mod.Field(0),
    rssi=mod.Field.RSSI,
    manufacturer_data=mod.Field.ManufacturerData,
    service_data=mod.Field.ServiceData,
)

FieldStr = Literal[
    "none",
    "rssi",
    "manufacturer_data",
    "service_data",
]

MAJOR_DEVICE_CLASS = bidict(
    miscellaneous=mod.MajorDeviceClass.MiscellaneousDevice,
    computer=mod.MajorDeviceClass.ComputerDevice,
    phone=mod.MajorDeviceClass.PhoneDevice,
    network=mod.MajorDeviceClass.NetworkDevice,
    audio_video=mod.MajorDeviceClass.AudioVideoDevice,
    peripheral=mod.MajorDeviceClass.PeripheralDevice,
    imaging=mod.MajorDeviceClass.ImagingDevice,
    wearable=mod.MajorDeviceClass.WearableDevice,
    toy=mod.MajorDeviceClass.ToyDevice,
    health=mod.MajorDeviceClass.HealthDevice,
    uncategorized=mod.MajorDeviceClass.UncategorizedDevice,
)

MajorDeviceClassStr = Literal[
    "miscellaneous",
    "computer",
    "phone",
    "network",
    "audio_video",
    "peripheral",
    "imaging",
    "wearable",
    "toy",
    "health",
    "uncategorized",
]

MINOR_AUDIO_VIDEO_CLASS = bidict(
    uncategorized=mod.MinorAudioVideoClass.UncategorizedAudioVideoDevice,
    wearable_headset=mod.MinorAudioVideoClass.WearableHeadsetDevice,
    hands_free=mod.MinorAudioVideoClass.HandsFreeDevice,
    microphone=mod.MinorAudioVideoClass.Microphone,
    loudspeaker=mod.MinorAudioVideoClass.Loudspeaker,
    headphones=mod.MinorAudioVideoClass.Headphones,
    portable_audio=mod.MinorAudioVideoClass.PortableAudioDevice,
    car_audio=mod.MinorAudioVideoClass.CarAudio,
    set_top_box=mod.MinorAudioVideoClass.SetTopBox,
    hifi_audio=mod.MinorAudioVideoClass.HiFiAudioDevice,
    vcr=mod.MinorAudioVideoClass.Vcr,
    video_camera=mod.MinorAudioVideoClass.VideoCamera,
    camcorder=mod.MinorAudioVideoClass.Camcorder,
    video_monitor=mod.MinorAudioVideoClass.VideoMonitor,
    video_display_and_loudspeaker=mod.MinorAudioVideoClass.VideoDisplayAndLoudspeaker,
    video_conferencing=mod.MinorAudioVideoClass.VideoConferencing,
    gaming=mod.MinorAudioVideoClass.GamingDevice,
)

MinorAudioVideoClassStr = Literal[
    "uncategorized",
    "wearable_headset",
    "hands_free",
    "microphone",
    "loudspeaker",
    "headphones",
    "portable_audio",
    "car_audio",
    "set_top_box",
    "hifi_audio",
    "vcr",
    "video_camera",
    "camcorder",
    "video_monitor",
    "video_display_and_loudspeaker",
    "video_conferencing",
    "gaming",
]

MINOR_COMPUTER_CLASS = bidict(
    uncategorized=mod.MinorComputerClass.UncategorizedComputer,
    desktop=mod.MinorComputerClass.DesktopComputer,
    server=mod.MinorComputerClass.ServerComputer,
    laptop=mod.MinorComputerClass.LaptopComputer,
    handheld_clam_shell=mod.MinorComputerClass.HandheldClamShellComputer,
    handheld_computer=mod.MinorComputerClass.HandheldComputer,
    wearable_computer=mod.MinorComputerClass.WearableComputer,
)

MinorComputerClassStr = Literal[
    "uncategorized",
    "desktop",
    "server",
    "laptop",
    "handheld_clam_shell",
    "handheld_computer",
    "wearable_computer",
]

MINOR_HEALTH_CLASS = bidict(
    uncategorized=mod.MinorHealthClass.UncategorizedHealthDevice,
    pressure_monitor=mod.MinorHealthClass.HealthBloodPressureMonitor,
    thermometer=mod.MinorHealthClass.HealthThermometer,
    weight_scale=mod.MinorHealthClass.HealthWeightScale,
    glucose_meter=mod.MinorHealthClass.HealthGlucoseMeter,
    pulse_oximeter=mod.MinorHealthClass.HealthPulseOximeter,
    data_display=mod.MinorHealthClass.HealthDataDisplay,
    step_counter=mod.MinorHealthClass.HealthStepCounter,
)

MinorHealthClassStr = Literal[
    "uncategorized",
    "pressure_monitor",
    "thermometer",
    "weight_scale",
    "glucose_meter",
    "pulse_oximeter",
    "data_display",
    "step_counter",
]

MINOR_IMAGING_CLASS = bidict(
    uncategorized=mod.MinorImagingClass.UncategorizedImagingDevice,
    display=mod.MinorImagingClass.ImageDisplay,
    camera=mod.MinorImagingClass.ImageCamera,
    scanner=mod.MinorImagingClass.ImageScanner,
    printer=mod.MinorImagingClass.ImagePrinter,
)

MinorImagingClassStr = Literal[
    "uncategorized",
    "display",
    "camera",
    "scanner",
    "printer",
]

MINOR_NETWORK_CLASS = bidict(
    full_service=mod.MinorNetworkClass.NetworkFullService,
    load_factor_one=mod.MinorNetworkClass.NetworkLoadFactorOne,
    load_factor_two=mod.MinorNetworkClass.NetworkLoadFactorTwo,
    load_factor_three=mod.MinorNetworkClass.NetworkLoadFactorThree,
    load_factor_four=mod.MinorNetworkClass.NetworkLoadFactorFour,
    load_factor_five=mod.MinorNetworkClass.NetworkLoadFactorFive,
    load_factor_six=mod.MinorNetworkClass.NetworkLoadFactorSix,
    none=mod.MinorNetworkClass.NetworkNoService,
)

MinorNetworkClassStr = Literal[
    "full_service",
    "load_factor_one",
    "load_factor_two",
    "load_factor_three",
    "load_factor_four",
    "load_factor_five",
    "load_factor_six",
    "none",
]

per = mod.MinorPeripheralClass
MINOR_PERIPHERAL_CLASS = bidict(
    uncategorized=per.UncategorizedPeripheral,
    keyboard=per.KeyboardPeripheral,
    pointing_device=per.PointingDevicePeripheral,
    keyboard_with_pointing_device=per.KeyboardWithPointingDevicePeripheral,
    joystick=per.JoystickPeripheral,
    gamepad=per.GamepadPeripheral,
    remote_control=per.RemoteControlPeripheral,
    sensing_device=per.SensingDevicePeripheral,
    digitizer_tablet=per.DigitizerTabletPeripheral,
    card_reader=per.CardReaderPeripheral,
)

MinorPeripheralClassStr = Literal[
    "uncategorized",
    "keyboard",
    "pointing_device",
    "keyboard_with_pointing_device",
    "joystick",
    "gamepad",
    "remote_control",
    "sensing_device",
    "digitizer_tablet",
    "card_reader",
]

MINOR_PHONE_CLASS = bidict(
    uncategorized=mod.MinorPhoneClass.UncategorizedPhone,
    cellular_phone=mod.MinorPhoneClass.CellularPhone,
    cordless_phone=mod.MinorPhoneClass.CordlessPhone,
    smart_phone=mod.MinorPhoneClass.SmartPhone,
    wired_modem_or_voice_gateway=mod.MinorPhoneClass.WiredModemOrVoiceGatewayPhone,
    common_isdn_access=mod.MinorPhoneClass.CommonIsdnAccessPhone,
)

MinorPhoneClassStr = Literal[
    "uncategorized",
    "cellular_phone",
    "cordless_phone",
    "smart_phone",
    "wired_modem_or_voice_gateway",
    "common_isdn_access",
]

MINOR_TOY_CLASS = bidict(
    uncategorized=mod.MinorToyClass.UncategorizedToy,
    robot=mod.MinorToyClass.ToyRobot,
    vehicle=mod.MinorToyClass.ToyVehicle,
    doll=mod.MinorToyClass.ToyDoll,
    controller=mod.MinorToyClass.ToyController,
    game=mod.MinorToyClass.ToyGame,
)

MinorToyClassStr = Literal[
    "uncategorized",
    "robot",
    "vehicle",
    "doll",
    "controller",
    "game",
]

MINOR_WEARABLE_CLASS = bidict(
    uncategorized=mod.MinorWearableClass.UncategorizedWearableDevice,
    wrist_watch=mod.MinorWearableClass.WearableWristWatch,
    pager=mod.MinorWearableClass.WearablePager,
    jacket=mod.MinorWearableClass.WearableJacket,
    helmet=mod.MinorWearableClass.WearableHelmet,
    glasses=mod.MinorWearableClass.WearableGlasses,
)

MinorWearableClassStr = Literal[
    "uncategorized",
    "robot",
    "vehicle",
    "doll",
    "controller",
    "game",
]

SERVICE_CLASS = bidict(
    none=mod.ServiceClass.NoService,
    positioning=mod.ServiceClass.PositioningService,
    networking=mod.ServiceClass.NetworkingService,
    rendering=mod.ServiceClass.RenderingService,
    capturing=mod.ServiceClass.CapturingService,
    object_transfer=mod.ServiceClass.ObjectTransferService,
    audio=mod.ServiceClass.AudioService,
    telephony=mod.ServiceClass.TelephonyService,
    information=mod.ServiceClass.InformationService,
    all=mod.ServiceClass.AllServices,
)

ServiceClassStr = Literal[
    "none",
    "positioning",
    "networking",
    "rendering",
    "capturing",
    "object_transfer",
    "audio",
    "telephony",
    "information",
    "all",
]


class BluetoothDeviceInfo(QtBluetooth.QBluetoothDeviceInfo):
    def __repr__(self):
        return get_repr(self, self.get_address(), self.name())

    def __bool__(self):
        return self.isValid()

    def get_address(self) -> bluetooth.BluetoothAddress:
        return bluetooth.BluetoothAddress(self.address())

    def get_device_ids(self) -> list[bluetooth.BluetoothUuid]:
        return [bluetooth.BluetoothUuid(i) for i in self.deviceIds()]

    def get_service_ids(self) -> list[bluetooth.BluetoothUuid]:
        return [bluetooth.BluetoothUuid(i) for i in self.serviceIds()]

    def get_service_uuids(self) -> list[bluetooth.BluetoothUuid]:
        return [bluetooth.BluetoothUuid(i) for i in self.serviceUuids()]

    def get_major_device_class(self) -> MajorDeviceClassStr:
        return MAJOR_DEVICE_CLASS.inverse[self.majorDeviceClass()]

    def get_minor_device_class(self) -> str:
        major = self.get_major_device_class()
        match major:
            case "computer":
                flag = mod.MinorComputerClass(self.minorDeviceClass())
                return MINOR_COMPUTER_CLASS.inverse[flag]
            case "phone":
                flag = mod.MinorPhoneClass(self.minorDeviceClass())
                return MINOR_PHONE_CLASS.inverse[flag]
            case "network":
                flag = mod.MinorNetworkClass(self.minorDeviceClass())
                return MINOR_NETWORK_CLASS.inverse[flag]
            case "audio_video":
                flag = mod.MinorAudioVideoClass(self.minorDeviceClass())
                return MINOR_AUDIO_VIDEO_CLASS.inverse[flag]
            case "peripheral":
                flag = mod.MinorPeripheralClass(self.minorDeviceClass())
                return MINOR_PERIPHERAL_CLASS.inverse[flag]
            case "imaging":
                flag = mod.MinorImagingClass(self.minorDeviceClass())
                return MINOR_IMAGING_CLASS.inverse[flag]
            case "wearable":
                flag = mod.MinorWearableClass(self.minorDeviceClass())
                return MINOR_WEARABLE_CLASS.inverse[flag]
            case "toy":
                flag = mod.MinorToyClass(self.minorDeviceClass())
                return MINOR_TOY_CLASS.inverse[flag]
            case "health":
                flag = mod.MinorHealthClass(self.minorDeviceClass())
                return MINOR_HEALTH_CLASS.inverse[flag]
            case "uncategorized":
                return "misc"
            case _:
                raise ValueError(major)

    def get_service_classes(self) -> list[ServiceClassStr]:
        return SERVICE_CLASS.get_list(self.serviceClasses())


if __name__ == "__main__":
    app = core.app()
    info = BluetoothDeviceInfo()
    print(info)

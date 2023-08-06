
from __future__ import annotations

from rich.progress import Progress, BarColumn, TextColumn, TaskProgressColumn
from textual.widget import Widget
from textual.widgets import Static, Label, LoadingIndicator
from textual.reactive import reactive
from textual import events, on
from textual.message import Message
from textual.app import ComposeResult
from textual.containers import Horizontal, Container

from rich.pretty import Pretty

import asyncio
import functools


from wireless_demo.demo_sd_sdk import sd


class LoadingWidget(Widget):
    def __init__(self, label):
        super().__init__()
        self.label = label

    def compose(self) -> ComposeResult:
        yield Label(self.label)
        yield LoadingIndicator()


class Notification(Static):
    def on_mount(self) -> None:
        self.set_timer(3, self.remove)

    def on_click(self) -> None:
        self.remove()


class TooltipEvent(Message):
    def __init__(self, tooltip: str) -> None:
        self.tooltip = tooltip
        super().__init__()

class HasDevice(Static):
    def __init__(self, connected_device, content="", **kwargs):
        super().__init__(content, **kwargs)
        self.device = connected_device


class Toggle(Static):
    collapsed = reactive(False)

    def render(self) -> str:
        return (":arrow_forward:" if self.collapsed else ":arrow_down_small:") + " Device Information"


class DeviceInformation(HasDevice):
    collapsed = reactive(False)

    def compose(self,) -> ComposeResult:
        yield Toggle()
        yield Static(Pretty(self.device.device_info.to_dict()))

    def on_mount(self,) -> None:
        self.query_one(Toggle).collapsed = True
        self.add_class("collapsed")

    def on_click(self,) -> None:
        collapsed = self.query_one(Toggle).collapsed
        if collapsed:
            self.remove_class("collapsed")
            self.query_one(Toggle).collapsed = False
        else:
            self.add_class("collapsed")
            self.query_one(Toggle).collapsed = True

class BatteryIndicator(HasDevice):
    level = reactive(0)

    def on_mount(self) -> None:
        self.rich_progress = Progress(
                                        TextColumn("[progress.description]:battery:"),
                                        BarColumn(),
                                        TaskProgressColumn(),
                                        auto_refresh=False,
                                     )
        self.rich_task = self.rich_progress.add_task("level", total=100)
        self.level = self.device.wireless_control.BatteryLevel
        self.update(self.rich_progress)

    def watch_level(self, new_level: int):
        self.rich_progress.update(self.rich_task, completed=new_level, refresh=True)

class VolumeControl(HasDevice):
    volume = reactive(0)

    def on_mount(self) -> None:
        self.rich_progress = Progress(
                                        TextColumn("[progress.description]Volume"),
                                        BarColumn(),
                                        TaskProgressColumn(),
                                        auto_refresh=False,
                                     )
        self.rich_task = self.rich_progress.add_task("volume", total=100)
        self.volume = self.device.wireless_control.Volume
        self.update(self.rich_progress)

    def watch_volume(self, new_volume: int):
        self.rich_progress.update(self.rich_task, completed=new_volume, refresh=True)

    def on_click(self,  event: events.Click) -> None:
        if event.button == 1:
            self.device.wireless_control.ChangeVolume(False)
        elif event.button == 2:
            self.device.wireless_control.Volume = 50
        elif event.button == 3:
            self.device.wireless_control.ChangeVolume(True)

    def on_enter(self, event: events.Enter):
        self.post_message(TooltipEvent("Left-click: Volume Down, Middle-click: Volume 50%, Right-click: Volume Up"))

    def on_leave(self, event: events.Leave):
        self.post_message(TooltipEvent(""))


class MicAttenuation(HasDevice):
    atten = reactive(0)

    def on_mount(self) -> None:
        self.rich_progress = Progress(
                                        TextColumn("[progress.description]Mic Level"),
                                        BarColumn(),
                                        TaskProgressColumn(),
                                        auto_refresh=False,
                                     )
        self.rich_task = self.rich_progress.add_task("atten", total=100)
        self.atten = self.device.wireless_control.MicAttenuation
        self.update(self.rich_progress)

    def watch_atten(self, new_atten: int):
        self.rich_progress.update(self.rich_task, completed=new_atten, refresh=True)

    def on_click(self,  event: events.Click) -> None:
        if event.button == 1:
            self.device.wireless_control.MicAttenuation = max(0, self.atten - 5)
        elif event.button == 2:
            self.device.wireless_control.MicAttenuation = 50
        elif event.button == 3:
            self.device.wireless_control.MicAttenuation = min(100, self.atten + 5)

    def on_enter(self, event: events.Enter):
        self.post_message(TooltipEvent("Left-click: -5%, Middle-click: 50%, Right-click: +5%"))

    def on_leave(self, event: events.Leave):
        self.post_message(TooltipEvent(""))


class AuxAttenuation(HasDevice):
    atten = reactive(0)

    def on_mount(self) -> None:
        self.rich_progress = Progress(
                                        TextColumn("[progress.description]Aux Level"),
                                        BarColumn(),
                                        TaskProgressColumn(),
                                        auto_refresh=False,
                                     )
        self.rich_task = self.rich_progress.add_task("atten", total=100)
        self.atten = self.device.wireless_control.AuxAttenuation
        self.update(self.rich_progress)

    def watch_atten(self, new_atten: int):
        self.rich_progress.update(self.rich_task, completed=new_atten, refresh=True)

    def on_click(self,  event: events.Click) -> None:
        if event.button == 1:
            self.device.wireless_control.AuxAttenuation = max(0, self.atten - 5)
        elif event.button == 2:
            self.device.wireless_control.AuxAttenuation = 50
        elif event.button == 3:
            self.device.wireless_control.AuxAttenuation = min(100, self.atten + 5)

    def on_enter(self, event: events.Enter):
        self.post_message(TooltipEvent("Left-click: -5%, Middle-click: 50%, Right-click: +5%"))

    def on_leave(self, event: events.Leave):
        self.post_message(TooltipEvent(""))


class MemoryPanel(HasDevice):
    class MemorySetEvent(Message):
        def __init__(self, memory: int) -> None:
            self.memory = memory
            super().__init__()

    def on_click(self, event: events.Click) -> None:
        if event.button == 1:
            self.device.wireless_control.ChangeMemory(False)
        elif event.button == 2:
            memory = int(self.id.split("memoryindicator")[1])
            self.device.wireless_control.CurrentMemory = memory
            # No notification when memory is manually set? Force a refresh.
            self.post_message_no_wait(self.MemorySetEvent(self, memory))
        elif event.button == 3:
            self.device.wireless_control.ChangeMemory(True)

    def on_enter(self, event: events.Enter):
        self.post_message(TooltipEvent("Left-click: Memory Down, Middle-click: Memory Set, Right-click:Memory Up"))

    def on_leave(self, event: events.Leave):
        self.post_message(TooltipEvent(""))


class MemoryControl(HasDevice):
    memory = reactive(0)
    num_memories = 0

    def compose(self,) -> ComposeResult:
        memories = []
        self.num_memories = self.device.wireless_control.NumberOfMemories
        for mem in range(self.num_memories):
            s = MemoryPanel(self.device, content=f"{mem}", id=f"memoryindicator{mem}", classes="memoryindicator")
            if not self.device.wireless_control.MemoryEnabled:
                s.add_class("disabled")
            memories.append(s)

        yield Static("Current Memory", classes="currentmemory")
        yield Horizontal(*memories)

    def on_mount(self) -> None:
        self.memory = self.device.wireless_control.CurrentMemory

    def watch_memory(self, new_memory: int):
        for mem in range(self.num_memories):
            if mem == new_memory:
                self.query_one(f"#memoryindicator{mem}").add_class("current")
            else:
                self.query_one(f"#memoryindicator{mem}").remove_class("current")

    def on_memory_panel_memory_set_event(self, event: MemoryPanel.MemorySetEvent) -> None:
        self.memory = self.device.wireless_control.CurrentMemory
        if self.memory != event.memory:
            self.app.logger.info(f"ERROR: Current memory {self.memory} did not match expected {event.memory}!")

class HearingAidWirelessControl(Widget):
    def __init__(self, connected_device):
        super().__init__()
        self.device = connected_device

    def compose(self) -> ComposeResult:
        yield Container(
            BatteryIndicator(self.device),
            VolumeControl(self.device),
            MicAttenuation(self.device),
            AuxAttenuation(self.device),
            MemoryControl(self.device),
            DeviceInformation(self.device),
        )

    def on_hearing_aid_control_panel_sdk_event(self, sdk_event: HearingAidControlPanel.SdkEvent) -> None:
        # Based on the event we got, update the child controls
        # self.app.logger.info(f"Got event type {sdk_event.event_type} with data {sdk_event.event_data}")
        if sdk_event.event_type == sd.kBatteryEvent:
            self.query_one(BatteryIndicator).level = int(sdk_event.event_data["BatteryLevel"])
        elif sdk_event.event_type == sd.kVolumeEvent:
            self.query_one(VolumeControl).volume = int(sdk_event.event_data["VolumeLevel"])
        elif sdk_event.event_type == sd.kMicAttenuationEvent:
            self.query_one(MicAttenuation).atten = int(sdk_event.event_data["MicLevel"])
        elif sdk_event.event_type == sd.kAuxAttenuationEvent:
            self.query_one(AuxAttenuation).atten = int(sdk_event.event_data["AuxLevel"])
        elif sdk_event.event_type == sd.kMemoryEvent:
            self.query_one(MemoryControl).memory = int(sdk_event.event_data["CurrentMemory"])
        else:
            self.app.logger.info(f"Got event type {sdk_event.event_type} with data {sdk_event.event_data}")
        # Avoid event bubbling back up to parent widget
        sdk_event.stop(True)


class HearingAidControlPanel(Widget):
    device_info: reactive[dict | None] = reactive(None)
    connected_device: reactive[object | None] = reactive(None)

    class SdkEvent(Message):
        def __init__(self, event_type: int, event_data: dict) -> None:
            self.event_type = event_type
            self.event_data = event_data
            super().__init__()

    class DeviceDisconnectedEvent(Message):
        pass

    def on_mount(self) -> None:
        self.display = False

    def watch_device_info(self, _old: dict, _new: dict) -> None:
        if _old is None and _new is not None:
            self.display = True
            self.mount(LoadingWidget(f"Connecting to '{self.device_info['DeviceName']}' ({self.device_info['DeviceID']})..."))
            asyncio.create_task(self.connect_device())

        elif _new is None:
            if self.connected_device:
                self.connected_device.close()
                self.connected_device = None
            self.display = False

    def watch_connected_device(self, _old: dict, _new: dict) -> None:
        if _new is not None:
            self.app.logger.info(f"Connected: ({self.device_info})")
            self.query_one(LoadingWidget).remove()
            self.connected_device.on_event = self.on_sdk_event
            # Change UI to show wireless control panel
            self.mount(HearingAidWirelessControl(self.connected_device))
        else:
            try:
                self.query_one(HearingAidWirelessControl).remove()
            except:
                pass
            self.app.logger.debug("Device disconnected")

    async def connect_device(self,) -> None:
        loop = asyncio.get_running_loop()
        self.connected_device = await loop.run_in_executor(None,
                                        functools.partial(self.app.sdk.connect_device,
                                                          self.device_info))

    def on_sdk_event(self, event_type, event_data):
        if event_type == sd.kConnectionEvent and int(event_data["ConnectionState"]) in [sd.kDisconnected, sd.kDisconnecting]:
            self.post_message(self.DeviceDisconnectedEvent())
        else:
            try:
                widget = self.query_one(HearingAidWirelessControl)
                widget.post_message(self.SdkEvent(event_type, event_data))
            except:
                pass

    @on(DeviceDisconnectedEvent)
    def device_disconnected(self):
        if self.device_info is not None:
            self.app.logger.info(f"Device disconnected: ({self.device_info})")
            self.app.mount(Notification(f"{self.device_info['DeviceID']} disconnected"))
            self.disconnect_device()

    def disconnect_device(self,):
        self.device_info = None


class HearingAidControlPanels(Widget):
    def compose(self) -> ComposeResult:
        yield Container(
            Horizontal (
                HearingAidControlPanel(id="deviceleft"),
                HearingAidControlPanel(id="deviceright"),
            ),
        )

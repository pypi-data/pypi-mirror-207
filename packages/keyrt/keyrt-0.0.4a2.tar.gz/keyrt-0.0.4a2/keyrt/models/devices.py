from datetime import datetime
from typing import Iterator

from pydantic import BaseModel


class Capability(BaseModel):
    name: str
    setup: bool


class InterCode(BaseModel):
    id: int
    code: str
    start_date: datetime
    end_date: datetime | None
    inter_code_type: str


class Device(BaseModel):
    id: str
    device_type: str
    serial_number: str
    device_group: list[str]
    entrance: int
    utc_offset_minutes: int
    camera_id: str
    description: str
    is_favorite: bool
    is_active: bool
    name_by_company: str
    name_by_user: str | None
    accept_concierge_call: bool
    capabilities: list[Capability]
    inter_codes: list[InterCode]


class Devices(BaseModel):
    devices: list[Device]

    def __getitem__(self, item) -> Device:
        # by device id
        for device in self.devices:
            if device.id == str(item):
                return device

        # by serial_number
        for device in self.devices:
            if device.serial_number == str(item):
                return device

        # by camera_id
        for device in self.devices:
            if device.camera_id == str(item):
                return device

        # by name_by_user or name_by_company
        for device in self.devices:
            if str(item) in (device.name_by_company, device.name_by_user):
                return device

        return self.devices[item]

    def __iter__(self) -> Iterator[Device]:
        return iter(self.devices)

    def __len__(self) -> int:
        return len(self.devices)


class DevicesResponse(BaseModel):
    data: Devices

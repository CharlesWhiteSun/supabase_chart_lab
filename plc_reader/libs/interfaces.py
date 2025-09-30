from typing import Protocol, Any

class IResultHandler(Protocol):
    """
    Interface for handling results from PLC devices.
    """
    def handle(self, device_id: str, voltage: float, current: float) -> None:
        ...

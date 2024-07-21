"""Constant Variables"""
from __future__ import annotations

from enum import Enum


class Os(Enum):
    """Os Type Enum"""

    LINUX = "linux"
    WINDOWS = "windows"
    DARWIN = "darwin"


class HostAttributes(Enum):
    """Host Attribute"""

    HOST_PATH = {
        Os.LINUX.value: r"/opt/Automation",
        Os.WINDOWS.value: r"C:\Automation",
        Os.DARWIN.value: r"/opt/Automation",
    }

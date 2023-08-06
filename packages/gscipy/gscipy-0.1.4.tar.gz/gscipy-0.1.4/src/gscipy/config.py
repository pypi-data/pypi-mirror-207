"""Module with general utility functions."""
from __future__ import annotations

__author__ = "Matteo Gabba"
__copyright__ = "Copyright 2022, all right reserved Gabba Scientific"
__status__ = "Development"

from dataclasses import dataclass

from gscipy.json_io import JsonIOInterface


@dataclass
class BaseConfigurator(JsonIOInterface):
    @property
    def kwargs(self):
        return self.__dict__

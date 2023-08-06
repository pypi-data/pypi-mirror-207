"""
"""

import json
import pathlib
import typing


class CAPEData:
    """
    """
    def __init__(self, path: typing.Union[str, pathlib.Path]):
        self.path = path
        if self.path.suffix != ".json":
            raise ValueError(
                f"expected .json file extension, got {self.path.suffix}"
            )

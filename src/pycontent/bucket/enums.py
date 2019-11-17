from enum import Enum


class ItemTypes(Enum):
    IGNORABLE = 1
    MANIFEST = 2
    BASE = 3
    FILE = 4
    DIRECTORY = 5

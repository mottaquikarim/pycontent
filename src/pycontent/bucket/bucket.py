import os

from pycontent.bucket.enums import ItemTypes
from pycontent.conf import BASE, MANIFEST


class Bucket:
    @staticmethod
    def get_path(base, name):
        if not name:
            return base

        return f"{base}/{name}"

    @staticmethod
    def get_item_type(base, name):
        path = Bucket.get_path(base, name)
        if name.startswith('.'):
            return ItemTypes.IGNORABLE
        if name == BASE:
            return ItemTypes.BASE
        if name == MANIFEST:
            return ItemTypes.MANIFEST
        if os.path.isdir(path):
            return ItemTypes.DIRECTORY
        if os.path.isfile(path):
            return ItemTypes.FILE

    @staticmethod
    def get_base_path(path):
        path_bits = path.split('.')
        return ".".join(path_bits[0:-1])

    def __init__(self, base, out, name):
        self.path = Bucket.get_path(base, name)
        self.out_path = Bucket.get_path(out, name)
        self.name = name
        self.base = base
        self.out = out

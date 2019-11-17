import json
import os

from enum import Enum

MANIFEST = os.environ['MANIFEST']
HOME = os.environ['HOME']


class ItemTypes(Enum):
    IGNORABLE = 1
    MANIFEST = 2
    HOME = 3
    FILE = 4
    DIRECTORY = 5


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
        if name == HOME:
            return ItemTypes.HOME
        if name == MANIFEST:
            return ItemTypes.MANIFEST
        if os.path.isdir(path):
            return ItemTypes.DIRECTORY
        if os.path.isfile(path):
            return ItemTypes.FILE

    def __init__(self, base, out, name):
        self.path = Bucket.get_path(base, name)
        self.base = base
        self.out = out


class File(Bucket):

    def __repr__(self):
        return self.path

    @property
    def content(self):
        try:
            return self._content
        except:
            pass

        with open(self.path) as f:
            self._content = f.read()

        return self._content


class Manifest(File):
    STARTSWITH = '- '
    SPLITSWITH = ':'

    @staticmethod
    def parse_line(line):
        if line.startswith(Manifest.STARTSWITH):
            line = line[len(Manifest.STARTSWITH):]

        if Manifest.SPLITSWITH in line:
            line = line.split(Manifest.SPLITSWITH)

        return line

    def __repr__(self):
        return f"MANIFEST {self.content}"

    @property
    def content(self):
        try:
            super().content
        except:
            self._content = None

        return self._content

    @property
    def parsed_manifest(self):
        try:
            return self._parsed_manifest
        except:
            pass

        self._parsed_manifest = []
        items = self.content.splitlines()
        for item in items:
            if not item:
                continue

            file_name, title = Manifest.parse_line(item)
            self._parsed_manifest.append((file_name, title))

        return self._parsed_manifest


class Directory(Bucket):

    def collect_children(self):
        for file_name, title in self.manifest.parsed_manifest:
            type_ = Bucket.get_item_type(self.path, file_name)

            if type_ == ItemTypes.IGNORABLE:
                continue

            if type_ == ItemTypes.DIRECTORY:
                self.children[file_name] = Directory(self.path, self.out, file_name)

            if type_ == ItemTypes.HOME:
                pass

            if type_ == ItemTypes.FILE:
                self.children[file_name] = File(self.path, self.out, file_name)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.home = None
        self.children = {}

        self.manifest = Manifest(self.path, self.out, MANIFEST)
        if self.manifest.content:
            self.collect_children()

        try:
            self.home = File(self.path, self.out, HOME)
        except:
            self.home = None

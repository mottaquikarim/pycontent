import json
import os
import shutil

from collections import OrderedDict

from pycontent.bucket.bucket import Bucket
from pycontent.bucket.enums import ItemTypes
from pycontent.bucket.file import File
from pycontent.bucket.manifest import Manifest
from pycontent.conf import BASE, MANIFEST


class Directory(Bucket):

    def transform(self, cb_tfrmer=None):
        shutil.rmtree(self.out, ignore_errors=True)
        try:
            os.mkdir(self.out)
        except:
            raise Exception("failed to make output directory")

        queue = [] + self.children
        while len(queue) > 0:
            name, inst = queue.pop(0)
            if isinstance(inst, Directory):
                os.mkdir(inst.out_path)
                queue.extend(inst.children)
                continue

            if cb_tfrmer:
                print(inst.out_path)
                cb_tfrmer(inst.content, Bucket.get_base_path(inst.out_path))

    def collect_children(self):
        self.full_manifest = self.manifest.filenames

        for file_name, title in self.manifest.parsed_manifest:
            type_ = Bucket.get_item_type(self.path, file_name)

            if type_ == ItemTypes.IGNORABLE:
                continue

            if type_ == ItemTypes.DIRECTORY:
                d = Directory(self.path, self.out, file_name)
                self.children.append((
                    file_name,
                    d
                ))
                self.full_manifest += d.manifest.filenames

            if type_ == ItemTypes.BASE:
                pass

            if type_ == ItemTypes.FILE:
                self.children.append((
                    file_name,
                    File(self.path, f"{self.out}/{self.name}", file_name)
                ))

    def collect_fileorder(self):
        if not self.full_manifest:
            return

        output = OrderedDict()
        for item in self.full_manifest:
            item_bits = item.split('/')[1:]
            if len(item_bits) == 1:
                output[item_bits[0]] = []
            else:
                item_base = item.split('.')[:-1]
                output[item_bits[0]].append(item_base)

        with open(f"{self.out}/manifest.json", "w") as f:
            f.write(json.dumps({"files": output}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.children = []
        self.full_manifest = []

        self.manifest = Manifest(self.path, self.out, MANIFEST)
        if self.manifest.content:
            self.collect_children()

        try:
            self.base_file = File(self.path, self.out, BASE)
        except:
            self.base_file = None

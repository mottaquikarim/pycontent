import os
import shutil

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
                cb_tfrmer(inst.content, inst.out_path)
            # with open(inst.out_path, "w") as f:
            #     if cb_tfrmer:
            #         f.write(cb_tfrmer(inst.content))

    def collect_children(self):
        for file_name, title in self.manifest.parsed_manifest:
            type_ = Bucket.get_item_type(self.path, file_name)

            if type_ == ItemTypes.IGNORABLE:
                continue

            if type_ == ItemTypes.DIRECTORY:
                self.children.append((
                    file_name,
                    Directory(self.path, self.out, file_name)
                ))

            if type_ == ItemTypes.BASE:
                pass

            if type_ == ItemTypes.FILE:
                self.children.append((
                    file_name,
                    File(self.path, f"{self.out}/{self.name}", file_name)
                ))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.base = None
        self.children = []

        self.manifest = Manifest(self.path, self.out, MANIFEST)
        if self.manifest.content:
            self.collect_children()

        try:
            self.base = File(self.path, self.out, BASE)
        except:
            self.base = None

import os

from pycontent.bucket.directory import Directory
from pycontent.conf import OUT, SRC
from pycontent.transformers.markdown_to_nb import tform


if __name__ == '__main__':
    d = Directory(SRC, OUT, '')
    for item in d.children:
        print(item)
#
    d.transform(cb_tfrmer=tform)
    d.collect_fileorder()

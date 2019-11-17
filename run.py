import os

from pycontent.bucket.directory import Directory
from pycontent.transformers.markdown_to_nb import tform

SRC = os.environ['SRC']
OUT = os.environ['OUT']

if __name__ == '__main__':
    d = Directory(SRC, OUT, '')
    print('here')
    for item in d.children:
        print(item)

    print(d.transform(cb_tfrmer=tform))
    # print(item)
    # print(d.base)
    # print(d.children[item])
    # if isinstance(d.children[item], Directory):
    #     print(d.children[item].children)

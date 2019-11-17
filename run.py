import os

from src.pycontent.main import Directory

SRC = os.environ['SRC']
OUT = os.environ['OUT']

if __name__ == '__main__':
    d = Directory(SRC, OUT, '')
    for item in d.children:
        pass
        # print(item)
        # print(d.home)
        # print(d.children[item])
        # if isinstance(d.children[item], Directory):
        #     print(d.children[item].children)

from pycontent.bucket.bucket import Bucket


class File(Bucket):

    @property
    def content(self):
        try:
            return self._content
        except:
            pass

        with open(self.path) as f:
            self._content = f.read()

        return self._content

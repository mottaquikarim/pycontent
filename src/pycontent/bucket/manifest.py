from pycontent.bucket.file import File
from pycontent.conf import SRC


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

    @property
    def content(self):
        try:
            super().content
        except:
            self._content = None

        return self._content

    @property
    def filenames(self):
        try:
            return self._filenames
        except:
            pass

        self.__parse_manifest()

        return self._filenames

    @property
    def parsed_manifest(self):
        try:
            return self._parsed_manifest
        except:
            pass

        self.__parse_manifest()

        return self._parsed_manifest

    def __parse_manifest(self):
        try:
            items = self.content.splitlines()
        except:
            self._filenames = []
            self._parsed_manifest = []
            return

        file_names = []
        parsed_manifest = []
        local_base = self.base.replace(SRC, '')

        for item in items:
            if not item:
                continue

            file_name, title = Manifest.parse_line(item)
            parsed_manifest.append((file_name, title))
            file_names.append(f"{local_base}/{file_name}")

        self._filenames = file_names
        self._parsed_manifest = parsed_manifest

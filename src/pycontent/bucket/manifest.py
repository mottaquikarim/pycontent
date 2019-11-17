from pycontent.bucket.file import File


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

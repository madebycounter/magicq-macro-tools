from macro import Macro


class Showfile:
    def __init__(self, header=[], data=[]):
        self.header = header
        self.unparsed = data
        self.macros = []

    def read(self, path):
        with open(path, "rb") as f:
            # Show files begin with a commented "header" that needs to be seperated
            self.header = []
            remaining_lines = []
            lines = f.read().decode().split("\r\n")
            for l in lines:
                if l.startswith("\\"):
                    self.header.append(l)
                else:
                    remaining_lines.append(l)

            remaining_lines = "".join(remaining_lines)

            # Extract each data block denoted by a semicolon followed by a newline
            data = [
                list(filter(lambda x: x, l.split(",")))
                for l in filter(
                    lambda x: x,
                    [
                        l.strip().replace("\r", "").replace("\n", "")
                        for l in remaining_lines.split(";")
                    ],
                )
            ]

            # Extract parsable data and store unparsed data
            self.unparsed = []
            self.macros = []

            for line in data:
                if Macro.verify(line):
                    self.macros.append(Macro.parse(line))

                else:
                    self.unparsed.append(line)

    def write(self, path):
        with open(path, "wb+") as f:
            all_data = self.unparsed + [Macro.format(m) for m in self.macros]
            file_data = (
                "\r\n".join(self.header)
                + "\r\n\r\n"
                + ";\r\n".join([",".join(l) for l in all_data])
            )
            f.write(file_data.encode())

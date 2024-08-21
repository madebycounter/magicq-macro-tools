class Showfile:
    def __init__(self, header=[], data=[]):
        self.header = header
        self.data = data

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
            self.data = [
                list(filter(lambda x: x, l.split(",")))
                for l in filter(
                    lambda x: x,
                    [
                        l.strip().replace("\r", "").replace("\n", "")
                        for l in remaining_lines.split(";")
                    ],
                )
            ]

    def write(self, path):
        with open(path, "wb+") as f:
            data = (
                "\r\n".join(self.header)
                + "\r\n\r\n"
                + ";\r\n".join([",".join(l) for l in self.data])
            )
            f.write(data.encode())

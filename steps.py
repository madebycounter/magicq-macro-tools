from format import Hex


class Mouse:
    CODE = "0009"
    PRESSED = 1
    RELEASED = 0

    def __init__(self, time=1, var1="0000", x=0, y=0, direction=PRESSED):
        self.time = time
        self.var1 = var1
        self.x = x
        self.y = y
        self.direction = direction

    def __repr__(self):
        direction = "PRESSED" if self.direction == Mouse.PRESSED else "RELEASED"
        return "Mouse<({}, {}), {}>".format(self.x, self.y, direction)

    @staticmethod
    def verify(line):
        return line[1] == Mouse.CODE

    @staticmethod
    def parse(line):
        time = Hex.parse(line[0])
        x = Hex.parse(line[3][0:4])
        y = Hex.parse(line[3][4:8])
        direction = Hex.parse(line[4])

        return Mouse(time=time, x=x, y=y, direction=direction, var1=line[2])

    @staticmethod
    def format(mouse):
        return [
            Hex.format(mouse.time, fill=8),
            Mouse.CODE,
            mouse.var1,
            Hex.format(mouse.x) + Hex.format(mouse.y),
            Hex.format(mouse.direction, fill=8),
        ]

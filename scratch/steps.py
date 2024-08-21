from format import Hex

KEY_MAP = {}
KEY_MAP_REVERSED = {}

with open("keys.txt", "r") as f:
    mapping = [l.split() for l in f.read().split("\n")]
    for m in mapping:
        KEY_MAP[m[0]] = m[1]
        KEY_MAP_REVERSED[m[1]] = m[0]

print(KEY_MAP)


class MQKey:
    CODE = "0100"
    DIR_SIGNIFIERS = {
        "BTN": ["0020", "00a0"],
        "KEY": ["0010", "0090"],
        "MOD": ["0000", "0080"],
    }

    PRESSED = 1
    RELEASED = 0

    def __init__(
        self, time=1, var1="0000", key="KEY_A", var3="00000000", direction=PRESSED
    ):
        self.time = time
        self.var1 = var1
        self.key = key
        self.var3 = var3
        self.direction = direction

    def __repr__(self):
        direction = "PRESSED" if self.direction == MQKey.PRESSED else "RELEASED"
        return "MQKey<{}, {}>({})".format(self.key, direction, self.time)

    @staticmethod
    def verify(line):
        return line[1] == MQKey.CODE

    @staticmethod
    def parse(line):
        time = Hex.parse(line[0])
        var1 = line[2]
        key = KEY_MAP_REVERSED[line[3][4:8]]
        direction = int(line[3][0:4] == MQKey.DIR_SIGNIFIERS[key.split("_")[0]][1])

        return MQKey(time=time, var1=var1, key=key, direction=direction)

    @staticmethod
    def format(mqkey):
        return [
            Hex.format(mqkey.time, fill=8),
            MQKey.CODE,
            mqkey.var1,
            MQKey.DIR_SIGNIFIERS[mqkey.key.split("_")[0]][mqkey.direction]
            + KEY_MAP[mqkey.key],
            mqkey.var3,
        ]

    @staticmethod
    def press(key, time=1):
        return [
            MQKey(time=time, key=key, direction=MQKey.PRESSED),
            MQKey(time=time + 1, key=key, direction=MQKey.RELEASED),
        ]


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
        return "Mouse<({}, {}), {}>({})".format(self.x, self.y, direction, self.time)

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

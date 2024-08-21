from format import Hex, String


class Macro:
    CODE = "K"

    def __init__(
        self,
        id=1,
        name="Macro",
        steps=[],
        var4="",
        var5="",
        var6="",
        var7="",
        var8="",
        var9="",
        var10="",
        var11="",
    ):
        self.id = id
        self.name = name
        self.steps = steps

        # Unknown vars (before steps)
        self.var4 = var4
        self.var5 = var5
        self.var6 = var6
        self.var7 = var7
        self.var8 = var8

        # Unknown vars (after steps)
        self.var9 = var9
        self.var10 = var10
        self.var11 = var11

    def __repr__(self):
        return 'Macro<M{}, "{}">({})'.format(self.id, self.name, len(self.steps))

    @staticmethod
    def verify(line):
        return line[0] == Macro.CODE

    @staticmethod
    def parse(line):
        id = Hex.parse(line[1])
        name = String.parse(line[2])
        n_steps = Hex.parse(line[3])

        steps = []

        for i in range(n_steps):
            steps.append(line[9 + i * 5 : 9 + ((i + 1) * 5)])

        return Macro(
            id=id,
            name=name,
            steps=steps,
            var4=line[4],
            var5=line[5],
            var6=line[6],
            var7=line[7],
            var8=line[8],
            var9=line[-3],
            var10=line[-2],
            var11=line[-1],
        )

    @staticmethod
    def format(macro):
        line = [
            Macro.CODE,
            Hex.format(macro.id),
            String.format(macro.name),
            Hex.format(len(macro.steps)),
            macro.var4,
            macro.var5,
            macro.var6,
            macro.var7,
            macro.var8,
        ]

        for step in macro.steps:
            line += step

        line += [macro.var9, macro.var10, macro.var11]

        return line

from format import Hex, String
from steps import Mouse, MQKey


class Macro:
    CODE = "K"

    def __init__(
        self,
        id=1,
        name="Macro",
        steps=[],
        var4="00000000",
        var5="0000",
        var6="0000",
        var7="0000",
        var8="0000",
        var9="00000000",
        var10="00000003",
        var11="0",
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

    def fix_times(self):
        for idx, step in enumerate(self.steps):
            step.time = idx

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
            step = line[9 + i * 5 : 9 + ((i + 1) * 5)]
            steps.append(step)

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
        line = (
            [
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
            + macro.steps
            + [macro.var9, macro.var10, macro.var11]
        )

        return line

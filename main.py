from showfile import Showfile
from format import Hex, String
from macro import Macro

IN_FILE = "L:\\MagicQ\\MacroTest5.shw"
OUT_FILE = "L:\\MagicQ\\FileWriteTest.shw"

show = Showfile()
show.read(IN_FILE)

for i in range(len(show.data)):
    if Macro.verify(show.data[i]):
        macro = Macro.parse(show.data[i])

        for step in macro.steps:
            print(step)


show.write(OUT_FILE)

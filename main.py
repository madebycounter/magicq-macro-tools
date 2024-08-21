from showfile import Showfile
from macro import Macro
import steps

IN_FILE = "L:\\MagicQ\\MacroTest5.shw"
OUT_FILE = "L:\\MagicQ\\FileWriteTest.shw"

show = Showfile()
show.read(IN_FILE)

for i in range(len(show.data)):
    if Macro.verify(show.data[i]):
        macro = Macro.parse(show.data[i])

        for j in range(len(macro.steps)):
            if steps.Mouse.verify(macro.steps[j]):
                step = steps.Mouse.parse(macro.steps[j])
                step.x = 99
                step.y = 99
                macro.steps[j] = steps.Mouse.format(step)

        show.data[i] = Macro.format(macro)

show.write(OUT_FILE)

from showfile import Showfile
from macro import Macro
from steps import Mouse

IN_FILE = "L:\\MagicQ\\MacroTest5.shw"
OUT_FILE = "L:\\MagicQ\\FileWriteTest.shw"

show = Showfile()
show.read(IN_FILE)

# Edit an existing macro
show.macros[0].name = "ABCDEFG"

for step in show.macros[0].steps:
    if isinstance(step, Mouse):
        step.x = 99
        step.y = 99

# Create a new macro
my_macro = Macro(
    id=2,
    name="Generated Macro",
    steps=[
        Mouse(time=1, x=100, y=400),
        Mouse(time=2, x=200, y=300, direction=Mouse.RELEASED),
        Mouse(time=3, x=300, y=200),
        Mouse(time=4, x=400, y=100, direction=Mouse.RELEASED),
    ],
)

show.macros.append(my_macro)

show.write(OUT_FILE)

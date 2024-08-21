from showfile import Showfile
from macro import Macro
import steps

IN_FILE = "L:\\MagicQ\\MacroTest5.shw"
OUT_FILE = "L:\\MagicQ\\FileWriteTest.shw"

show = Showfile()
show.read(IN_FILE)

show.macros[0].name = "ABCDEFG"

print(show.macros)

show.write(OUT_FILE)

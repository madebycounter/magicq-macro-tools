from showfile import Showfile
from macro import Macro
from steps import MQKey

IN_FILE = "C:\\Users\\william\\Documents\\MagicQ\\show\\NewShow.shw"
OUT_FILE = "C:\\Users\\william\\Documents\\MagicQ\\show\\NewShowUpdated.shw"

# Load show file
show = Showfile()
show.read(IN_FILE)

# Create a new macro
my_macro = Macro(
    id=1,
    name="Generated Macro With Keys",
    steps=MQKey.press("KEY_H")
    + MQKey.press("KEY_e")
    + MQKey.press("KEY_l")
    + MQKey.press("KEY_l")
    + MQKey.press("KEY_o")
    + MQKey.press("KEY_SPACE")
    + MQKey.press("KEY_W")
    + MQKey.press("KEY_o")
    + MQKey.press("KEY_r")
    + MQKey.press("KEY_l")
    + MQKey.press("KEY_d"),
)

# Fix times (since we didn't specify)
# This gives each macro step a subsequent time so MagicQ can understand it
my_macro.fix_times()

# Add macro to the show
show.macros.append(my_macro)

# Write to new showfile
show.write(OUT_FILE)

from magicq import macro, key, mouse

macro.title("My Macro")
macro.id(1)

for letter in "William":
    key.press("KEY_{}".format(letter))

mouse.press(100, 100)

macro.write("C:\\Users\\william\\Documents\\MagicQ\\show\\TestShow.shw")

COLORS = ["White", "Red", "Amber", "Yellow", "Green", "Cyan", "Blue", "Magenta"]
EXEC_PAGE = 2
EXEC_START = 2

combos = []
for y, c1 in enumerate(COLORS):
    for x, c2 in enumerate(reversed(COLORS)):
        if c2 == c1:
            break
        combos.append((c1, c2, (x, y)))

print(combos)

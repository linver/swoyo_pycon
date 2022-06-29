import pyxel

CHARS = {
    'А': [(0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2), (0, 3), (2, 3), (0, 3), (2, 3), (0, 4),
          (2, 4)],
    'Б': [(0, 0), (1, 0), (2, 0), (0, 1), (0, 2), (1, 2), (2, 2), (0, 3), (2, 3), (0, 3), (2, 3), (0, 4), (1, 4),
          (2, 4)],
    'В': [(0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2), (0, 3), (2, 3), (0, 3), (2, 3), (0, 4),
          (1, 4), (2, 4)],
    'Г': [(0, 0), (1, 0), (0, 1), (0, 2), (0, 3), (0, 4)],
    'Д': [(1, 0), (2, 0), (3, 0), (1, 1), (3, 1), (1, 2), (3, 2), (1, 3), (3, 3), (0, 4), (1, 4), (2, 4), (3, 4),
          (4, 4)],
    'Е': [(0, 0), (1, 0), (0, 1), (0, 2), (1, 2), (0, 3), (0, 4), (1, 4)],
    'Ж': [(0, 0), (2, 0), (4, 0), (0, 1), (2, 1), (4, 1), (1, 2), (2, 2), (3, 2), (0, 3), (2, 3), (4, 3), (0, 4),
          (2, 4), (4, 4)],
    'З': [(0, 0), (1, 0), (1, 1), (0, 2), (1, 3), (0, 4), (1, 4)],
    'И': [(0, 0), (3, 0), (0, 1), (3, 1), (0, 2), (2, 2), (3, 2), (0, 3), (1, 3), (3, 3), (0, 4), (3, 4)],
    'Й': [(0, 0), (3, 0), (0, 1), (3, 1), (0, 2), (2, 2), (3, 2), (0, 3), (1, 3), (3, 3), (0, 4), (3, 4), (1, -1),
          (2, -1)],
    'К': [(0, 0), (0, 1), (2, 1), (0, 2), (1, 2), (0, 3), (2, 3), (0, 4), (2, 4), (2, 0)],
    'Л': [(1, 0), (2, 0), (1, 1), (2, 1), (0, 2), (2, 2), (0, 3), (2, 3), (0, 4), (2, 4)],
    'М': [(0, 0), (4, 0), (0, 1), (1, 1), (3, 1), (4, 1), (0, 2), (2, 2), (4, 2), (0, 3), (4, 3), (0, 4), (4, 4)],
    'Н': [(0, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2), (0, 3), (2, 3), (0, 4), (2, 4)],
    'О': [(0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (2, 2), (0, 3), (2, 3), (0, 4), (1, 4), (2, 4)],
    'П': [(0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (2, 2), (0, 3), (2, 3), (0, 4), (2, 4)],
    'Р': [(0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2), (0, 3), (0, 4)],
    'С': [(0, 0), (1, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4)],
    'Т': [(0, 0), (1, 0), (2, 0), (1, 1), (1, 2), (1, 3), (1, 4)],
    'У': [(0, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2), (2, 3), (0, 4), (1, 4), (2, 4)],
    'Ф': [(2, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (0, 2), (2, 2), (4, 2), (0, 3), (1, 3), (2, 3), (3, 3),
          (4, 3), (2, 4)],
    'Х': [(0, 0), (2, 0), (0, 1), (2, 1), (1, 2), (0, 3), (2, 3), (0, 4), (2, 4)],
    'Ц': [(0, 0), (2, 0), (0, 1), (2, 1), (0, 2), (2, 2), (0, 3), (2, 3), (0, 4), (1, 4), (2, 4), (3, 4)],
    'Ч': [(0, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2), (2, 3), (2, 4)],
    'Ш': [(0, 0), (2, 0), (4, 0), (0, 1), (2, 1), (4, 1), (0, 2), (2, 2), (4, 2), (0, 3), (2, 3), (4, 3), (0, 4),
          (1, 4), (2, 4), (3, 4), (4, 4)],
    'Щ': [(0, 0), (2, 0), (4, 0), (0, 1), (2, 1), (4, 1), (0, 2), (2, 2), (4, 2), (0, 3), (2, 3), (4, 3), (0, 4),
          (1, 4), (2, 4), (3, 4), (4, 4), (5, 4)],
    'Ъ': [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2), (3, 2), (1, 3), (3, 3), (1, 4), (2, 4), (3, 4)],
    'Ы': [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (0, 3), (2, 3), (0, 4), (1, 4), (2, 4), (4, 0), (4, 1), (4, 2),
          (4, 3), (4, 4)],
    'Ь': [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (0, 3), (2, 3), (0, 4), (1, 4), (2, 4)],
    'Э': [(0, 0), (1, 1), (0, 2), (1, 3), (0, 4), (1, 2)],
    'Ю': [(0, 0), (2, 0), (3, 0), (4, 0), (0, 1), (2, 1), (4, 1), (0, 2), (1, 2), (2, 2), (4, 2), (0, 3), (2, 3),
          (4, 3), (0, 4), (2, 4), (3, 4), (4, 4)],
    'Я': [(0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2), (1, 3), (2, 3), (0, 4), (2, 4)],
    '0': [(0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (2, 2), (0, 3), (2, 3), (0, 4), (1, 4), (2, 4)],
    '1': [(1, 0), (0, 1), (1, 1), (1, 2), (1, 3), (1, 4)],
    '2': [(0, 0), (1, 0), (1, 1), (0, 2), (1, 2), (0, 3), (0, 4), (1, 4)],
    '3': [],
    '4': [],
    '5': [],
    '6': [],
    '7': [],
    '8': [],
    '9': [],
    '.': [(0, 4)],
    ',': [(0, 4), (0, 5)],
    '?': [(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (3, 1), (2, 2), (3, 2), (2, 4)],
    '!': [(0, 0), (0, 1), (0, 2), (0, 4)],
    '-': [(0, 2), (1, 2)],
    '[': [(0, 0), (1, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4)],
    ']': [(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (0, 4)],
    ':': [(2, 1), (2, 3)],
    '(': [(0, 1), (0, 2), (0, 3), (1, 0), (1, 4)],
    ')': [(0, 0), (0, 4), (1, 1), (1, 2), (1, 3)]
}


def text(t, x, y, color):
    t = t.upper()
    offset_x = 0
    for char in t:
        if char == ' ':
            offset_x += 3
        else:
            for pixel in CHARS[char]:
                pyxel.pset(x+pixel[0]+offset_x, y+pixel[1], color)
            offset_x += max([x[0] for x in CHARS[char]]) + 2
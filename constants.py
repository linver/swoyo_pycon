# -*- coding: cp1251 -*-
import pyxel

LAUNCH = 'LAUNCH'

START_GAME = 'START_GAME'
END_GAME = 'END_GAME'

TYPE_CHARACTER = 'TYPE_CHARACTER'
HIT_CHARACTER = 'HIT_CHARACTER'
# MISS_CHARACTER = 'MISS_CHARACTER'

COMPLETE_WORD = 'COMPLETE_WORD'
# NEXT_WORD = 'NEXT_WORD'

prizes = ["подставка  под  чашку", "набор  наклеек", "головоломка", "коврик  для  мышки", "тетрис", "термокружка"]
prizes_eng = ["coaster for a cup", "sticker pack", "puzzle", "mousepad", "tetris", "thermal mug"]
borders = [
    (-1, 0), (1, 0), (0, -1), (0, 1),
    (-2, 0), (2, 0), (0, -2), (0, 2),
    (-1, 2), (1, 2), (-1, -2), (1, -2),
    (-2, 1), (-2, -1), (2, 1), (2, -1),
    (-1, 1), (1, -1), (-1, -1), (1, 1)
]


character_map = {
    'a': pyxel.KEY_A,
    'b': pyxel.KEY_B,
    'c': pyxel.KEY_C,
    'd': pyxel.KEY_D,
    'e': pyxel.KEY_E,
    'f': pyxel.KEY_F,
    'g': pyxel.KEY_G,
    'h': pyxel.KEY_H,
    'i': pyxel.KEY_I,
    'j': pyxel.KEY_J,
    'k': pyxel.KEY_K,
    'l': pyxel.KEY_L,
    'm': pyxel.KEY_M,
    'n': pyxel.KEY_N,
    'o': pyxel.KEY_O,
    'p': pyxel.KEY_P,
    'q': pyxel.KEY_Q,
    'r': pyxel.KEY_R,
    's': pyxel.KEY_S,
    't': pyxel.KEY_T,
    'u': pyxel.KEY_U,
    'v': pyxel.KEY_V,
    'w': pyxel.KEY_W,
    'x': pyxel.KEY_X,
    'y': pyxel.KEY_Y,
    'z': pyxel.KEY_Z,
}

character_map_str = {
    'KEY_A': 'a',
    'KEY_B': 'b',
    'KEY_C': 'c',
    'KEY_D': 'd',
    'KEY_E': 'e',
    'KEY_F': 'f',
    'KEY_G': 'g',
    'KEY_H': 'h',
    'KEY_I': 'i',
    'KEY_J': 'j',
    'KEY_K': 'k',
    'KEY_L': 'l',
    'KEY_M': 'm',
    'KEY_N': 'n',
    'KEY_O': 'o',
    'KEY_P': 'p',
    'KEY_Q': 'q',
    'KEY_R': 'r',
    'KEY_S': 's',
    'KEY_T': 't',
    'KEY_U': 'u',
    'KEY_V': 'v',
    'KEY_W': 'w',
    'KEY_X': 'x',
    'KEY_Y': 'y',
    'KEY_Z': 'z',
    'KEY_1': '1',
    'KEY_2': '2',
    'KEY_3': '3',
    'KEY_4': '4',
    'KEY_5': '5',
    'KEY_6': '6',
    'KEY_7': '7',
    'KEY_8': '8',
    'KEY_9': '9',
    'KEY_0': '0',
    'KEY_MINUS': '-',
    'KEY_PERIOD': '.',
}

character_map_int = {
    pyxel.KEY_A: 'a',
    pyxel.KEY_B: 'b',
    pyxel.KEY_C: 'c',
    pyxel.KEY_D: 'd',
    pyxel.KEY_E: 'e',
    pyxel.KEY_F: 'f',
    pyxel.KEY_G: 'g',
    pyxel.KEY_H: 'h',
    pyxel.KEY_I: 'i',
    pyxel.KEY_J: 'j',
    pyxel.KEY_K: 'k',
    pyxel.KEY_L: 'l',
    pyxel.KEY_M: 'm',
    pyxel.KEY_N: 'n',
    pyxel.KEY_O: 'o',
    pyxel.KEY_P: 'p',
    pyxel.KEY_Q: 'q',
    pyxel.KEY_R: 'r',
    pyxel.KEY_S: 's',
    pyxel.KEY_T: 't',
    pyxel.KEY_U: 'u',
    pyxel.KEY_V: 'v',
    pyxel.KEY_W: 'w',
    pyxel.KEY_X: 'x',
    pyxel.KEY_Y: 'y',
    pyxel.KEY_Z: 'z',
    pyxel.KEY_1: '1',
    pyxel.KEY_2: '2',
    pyxel.KEY_3: '3',
    pyxel.KEY_4: '4',
    pyxel.KEY_5: '5',
    pyxel.KEY_6: '6',
    pyxel.KEY_7: '7',
    pyxel.KEY_8: '8',
    pyxel.KEY_9: '9',
    pyxel.KEY_0: '0',
    pyxel.KEY_MINUS: '-',
    pyxel.KEY_PERIOD: '.',
}

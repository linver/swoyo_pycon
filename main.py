import pyxel
import pyxelcyrillic

from pyxel_extensions.actions import action
from pyxel_extensions.game import Game
from pyxel_extensions.scene import Scene
from constants import character_map_str, borders

# !!!! change 'pyxel.init(160, 120)' string to 'pass' in init_pyxel() in pyxel-extensions/pyxel_extensions/game.py
#    def init_pyxel(self):
#       pyxel.init(160, 120) ==> pass


class Start(Game):
    def __init__(self, initial_state, initial_scene, width, height):
        super().__init__(initial_state, initial_scene)
        pyxel.init(width, height, title='SWOYO game')
        pyxel.load("swoyo.pyxres")

    def get_scenes(self):
        return SwoyoGame,


class SwoyoGame(Scene):
    def update(self):
        buff = 0

        for k in pyxel.__dict__.keys():
            if k.startswith('KEY_'):
                if pyxel.btn(pyxel.KEY_SHIFT):
                    buff += 1
                if pyxel.btnp(pyxel.KEY_BACKSPACE):
                    self.store.state['email'] = self.store.state['email'][:-1]
                    self.store.state['count'] = 0
                    buff = 0
                if pyxel.btnp(pyxel.KEY_RETURN):
                    self.store.state['result'] = True
                    self.save_email('emails.txt')
                    break
                if pyxel.btnp(pyxel.KEY_SPACE):
                    self.store.state["result"] = ''
                    self.store.state["count"] = 0
                    self.store.state["email"] = ''
                if pyxel.btnp(getattr(pyxel, k)):
                    if buff:
                        if k == 'KEY_MINUS':
                            self.store.state['email'] += '_'
                        elif k == 'KEY_2':
                            self.store.state['email'] += '@'
                        else:
                            self.store.state['email'] += character_map_str.get(k, '').upper()
                        buff = 0
                    else:
                        self.store.state['email'] += character_map_str.get(k, '')
                    if character_map_str.get(k, 'none').upper() in 'SWOYO':
                        self.store.dispatch(count_identical_letters())

    def draw(self):
        pyxel.cls(9)
        self.swoyo(145, 20)
        self.cat(225, 20)
        pyxel.rectb(5, 5, 374, 190, 7)
        if not self.store.state['result']:
            self.hello(60, 80, 4, 7)
            pyxel.rect(91, 104, 190, 11, 4)
            pyxel.rect(89, 102, 190, 11, 15)
            pyxel.text(92, 105, str(self.store.state['email']), 4)
            self.command_finish(220, 180, 7)
        else:
            self.thank_and_get_result(150, 80, 15, 8)
            self.command_restart(220, 180, 7)

    @staticmethod
    def text_with_border(x, y, s, col, bcol):
        for x_offset, y_offset in borders:
            pyxel.text(x + x_offset, y + y_offset, s, bcol)
        pyxel.text(x, y, s, col)

    @staticmethod
    def text_with_border_cyrillic(x, y, s, col, bcol):
        for x_offset, y_offset in borders:
            pyxelcyrillic.text(s, x + x_offset, y + y_offset, bcol)
        pyxelcyrillic.text(s, x, y, col)

    def hello(self, x, y, col, bcol):
        self.text_with_border(x, y, "> > > ", col, bcol)
        self.text_with_border_cyrillic(x + 30, y, "Добрый  день! ", col, bcol)
        self.text_with_border_cyrillic(x + 90, y, "Пожалуйста,  введите  ваш", col, bcol)
        self.text_with_border(x + 195, y, 'EMAIL:', col, bcol)

    @staticmethod
    def command_finish(x, y, col):
        pyxelcyrillic.text('Нажмите', x, y, col)
        pyxel.text(x + 30, y, ' <ENTER>,', col)
        pyxelcyrillic.text(' чтобы узнать результат', x + 65, y, col)

    @staticmethod
    def command_restart(x, y, col):
        pyxelcyrillic.text('Нажмите', x, y, col)
        pyxel.text(x + 30, y, ' <SPACE>,', col)
        pyxelcyrillic.text(' чтобы начать заново', x + 65, y, col)

    def thank_and_get_result(self, x, y, col, bcol):
        pyxel.rect(x - 17, y - 17, 115, 75, 4)
        pyxel.rect(x - 20, y - 20, 115, 75, 7)
        pyxel.rectb(x - 15, y - 15, 105, 65, 9)
        pyxelcyrillic.text('Спасибо  за  участие!', x, y, col)
        pyxelcyrillic.text('Спасибо  за  участие!', x - 1, y - 1, bcol)
        pyxelcyrillic.text('Количество  баллов: ', x - 2, y + 30, col)
        pyxelcyrillic.text('Количество  баллов: ', x - 3, y + 29, bcol)
        pyxel.text(x + 73, y + 30, str(self.store.state["count"]), col)
        pyxel.text(x + 72, y + 29, str(self.store.state["count"]), bcol)

    def points(self, x, y, col, bcol):
        text = 'Баллы:'
        pyxel.text(x + 34, y, str(self.store.state["count"]), col)
        pyxel.text(x + 35, y, str(self.store.state["count"]), bcol)
        pyxelcyrillic.text(text, x, y, col)
        pyxelcyrillic.text(text, x + 1, y, bcol)

    @staticmethod
    def cat(x, y):
        offset = pyxel.sin(pyxel.frame_count * 5.73)
        pyxel.blt(x + offset, y, 0, 32, 0, 16, 16, 13)

    @staticmethod
    def swoyo(x, y):
        offset = pyxel.sin(pyxel.frame_count * 5.73)
        pyxel.blt(x + offset, y, 0, 24, 16, 68, 16, 13)

    def save_email(self, filename):
        with open(filename, 'a+') as f:
            f.write(self.store.state['email'] + '\n')


@action
def count_identical_letters(state):
    return {**state, 'count': state['count'] + 1, 'email': state['email']}


if __name__ == '__main__':
    while True:
        Start(
            initial_state={'count': 0, 'email': '', 'result': False},
            initial_scene=SwoyoGame,
            width=384,
            height=200
        ).run()

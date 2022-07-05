#### Небольшое приложение для поиска количества совпадающих символов в введённом слове и слове-эталоне (в данном случае эталоном является 'swoyo').

Для того, чтобы пользоваться приложением, необходимо:

* установить python 3.10 (https://www.python.org/downloads/release/python-3105/)
* установить пакетный менеджер pip (https://pip.pypa.io/en/stable/cli/pip_download/)
* установить git (https://git-scm.com/downloads)
* установить PyCharm Community (https://www.jetbrains.com/pycharm/download/#section=windows) - опционально, можно запускать через консоль

0. открыть Git Bash (можно и Windows PowerShell)
1. клонировать данный репозиторий к себе в проект (перейти в папку с проектом, в терминале ввести `git clone https://github.com/linver/swoyo_pycon.git`)
2. установить библиотеку pyxel (pip install pyxel) 
3. установить библиотеку pyxel-extensions (перейти в директорию /swoyo_pycon в папке проекта и ввести в терминале `pip install -e git+https://github.com/gediminasz/pyxel-extensions.git@v0.0.2#egg=pyxel_extensions`):
4. перейти в директорию pyxel-extensions-master/pyxel_extensions (`cd src/pyxel-extensions/pyxel_extensions`), открыть файл game.py (nano game.py) и изменить в нём дефолтные границы окна приложения в строчке 27 функции def init_pyxel(self) => заменить '**pyxel.init(160, 120)**' на '**pass**'
5. перейти обратно в папку /swoyo_pycon и запустить приложение: `python main.py`


В файле swoyo.pyxres содержится графика, созданная с помощью встроенного pyxel editor (запускается командой pyxel edit swoyo в командной строке).

Файл emails.txt содержит все введённые email'ы.

Общая информация о модуле pyxel: https://github.com/kitao/pyxel

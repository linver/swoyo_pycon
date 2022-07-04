Небольшое приложение для поиска количества совпадающих символов в введённом слове и слове-эталоне (в данном случае эталоном является 'swoyo').

Чтобы пользоваться приложением, необходимо:
1) клонировать данный репозиторий к себе в проект
2) установить библиотеку pyxel https://github.com/kitao/pyxel (скачать архив, распаковать, скопировать абсолютный путь до папки с распакованными файлами, сделать pip install <путь до папки> в директории с проектом)
3) установить библиотеку pyxel-extensions https://github.com/gediminasz/pyxel-extensions

Так же в модуле pyxel-extensions/pyxel_extensions/game.py в методе init_pyxel необходимо заменить строку "pyxel.init(160, 120)" на "pass" - это сделано для того, чтобы изменить размер окна по умолчанию (в данном приложении он равен 384х200, по умолчанию же 160x120).

В файле swoyo.pyxres содержится графика, созданная с помощью встроенного pyxel editor (запускается командой pyxel edit swoyo в командной строке).

Файл emails.txt содержит все введённые email'ы.

Общая информация о модуле pyxel: https://github.com/kitao/pyxel

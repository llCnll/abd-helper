import numpy as np
import cv2
import subprocess
from hashlib import md5
from datetime import date
from time import sleep

from aobi import log_execution_time

ADB_ROOT = r'D:\test'
DATA_ROOT = r'.\data'

DEBUG = True


def adb(cmd):
    process = subprocess.Popen(rf'{ADB_ROOT}\adb {cmd}', shell=True, stdout=subprocess.PIPE)
    return process.stdout.read()


def device_check():
    result = adb('devices')
    if DEBUG:
        print(result)
    assert len(result.split(b'\r\n')) == 4

    result = adb('shell wm size')
    if DEBUG:
        print(result)
    assert result == b'Physical size: 1920x1080\r\r\n'

@log_execution_time
def screen_cap():
    return adb('shell screencap -p').replace(b'\r\r\n', b'\r\n').replace(b'\r\n', b'\n')


def sc():
    return cv2.imdecode(np.frombuffer(screen_cap(), np.uint8), cv2.IMREAD_COLOR)

@log_execution_time
def match(template_name, ac=0.8, img=None):
    if img is None:
        img = sc()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(rf'{DATA_ROOT}\template\{template_name}.png', 0)

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    w, h = template.shape[::-1]

    if DEBUG:
        print(max_val, min_loc, max_loc)

    if max_val < ac:
        return None

    return w // 2 + max_loc[0], h // 2 + max_loc[1]


def save_sc(sc_name=None):
    img_bytes = screen_cap()
    if sc_name is None:
        sc_name = '{:s}_{:s}.png'.format(date.today().strftime('%Y%m%d'), md5(img_bytes).hexdigest())
    with open(rf'{DATA_ROOT}\sc\{sc_name}', 'wb') as f:
        f.write(img_bytes)

@log_execution_time
def click(x, y):
    if DEBUG:
        print(f'click ({x}, {y})')
    adb(f'shell input tap {x} {y}')

@log_execution_time
def swipe(src_x, src_y, dist_x, dist_y, speed=200):
    if DEBUG:
        print(f'swipe ({src_x}, {src_y}) -> ({dist_x}, {dist_y})')
    adb(f'shell input swipe {src_x} {src_y} {dist_x} {dist_y} {speed}')


def wait(time=0.2):
    sleep(time)


def page_left():
    if DEBUG:
        print(f'Page left')
    swipe(1300, 540, 500, 540)


def page_right():
    if DEBUG:
        print(f'Page right')
    swipe(500, 540, 1300, 540)


def page_up():
    if DEBUG:
        print(f'Page up')
    swipe(960, 800, 960, 300)


def page_down():
    if DEBUG:
        print(f'Page down')
    swipe(960, 300, 960, 800)


if __name__ == '__main__':
    device_check()
    # save_sc('test.png')
    # click(*match('mature'))

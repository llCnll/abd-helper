import functools

from adb import *
from time import time

sc_length = 1920
sc_width = 1080
speed = sc_length / 1.71


# 日志耗时装饰器
def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        res = func(*args, **kwargs)
        end = time()
        print('【%s】 cost time %.2f s' % (func.__name__, (end - start)))
        return res
    return wrapper


def get_center(img):
    match_row = [_[2] for _ in img[sc_width - 10]]
    # print(match_row)
    for index in range(sc_length):
        if match_row[index] < 110:
            left = index
            while index < sc_length:
                if match_row[index] > 100:
                    return (left + index) >> 1
                index += 1


@log_execution_time
def fishing(only_king=False):
    start_state = match('fish5', 0.8)
    print(f'start_state {start_state}')
    if start_state is None:
        # click(541, 332)
        click(1400, 669)
	# click(800, 469)
        wait(1.5)

    swipe(800, 960, 800, 600)

    wait(3)

    start = time()
    img = screen_cap()
    save_img(img, 'x3.png')
    img_a = cv2.imdecode(np.frombuffer(img, np.uint8), cv2.IMREAD_COLOR)
    label_x = match('label', 0.8, img_a[-300:])[0]
    print(f'label_x {label_x}')
    center_x = get_center(img_a)
    print(f'center_x {center_x}')
    king = match('king', 0.8, img_a[-300:])
    print(f'king {king}')
    delay = time() - start
    delay += 0.4

    print(f'delay: {delay}')

    sleep_time = ((sc_length * 4 + center_x - label_x) - (speed * delay)) / (speed+5)
    print(f'sleep_time {sleep_time}')
    if king is not None:
        print(f'king is not None')
        if sleep_time > 0:
            wait(sleep_time)
        click(701, 624)
        wait(2)
        adb('shell monkey -f /storage/emulated/0/data/tap.mks -v 1')
        wait(0.5)
        # 确定
        click(956, 815)
        wait(2)

    elif only_king:
        print(f'only_king')
        if center_x < 1250:
            click(702, 624)
        else:
            wait(sleep_time)
            click(702, 624)
        wait(2.3)
        # 确定
        click(956, 815)
        wait(2)

    else:
        print(f'normal')
        if sleep_time > 0:
            wait(sleep_time)
        click(703, 624)
        wait(5)
        # 确定
        click(956, 815)
        wait(2)


@log_execution_time
def save_img(img, pic_name):
    f = open(pic_name, 'wb')
    f.write(img)
    f.close()


if __name__ == '__main__':
    print(f'speed : {speed}')

    # fishing(only_king=False)
    loop = 0
    while loop < 100:
        try:
            fishing(only_king=False)
            loop = loop + 1
        except Exception as e:
            print('exception')
            print(e)
            wait(3)
            # 确定
            click(956, 815)
            wait(5)
            loop = loop + 1
            continue

    click(1818, 1007)

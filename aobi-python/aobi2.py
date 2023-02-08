from adb import *
from time import time


def yama():

    while True:
        while True:
            point = match('blank', 0.9)
            if point is None:
                break
            click(*point)
            wait(0.5)
            swipe(*match('yama'), 950, 515, 1000)
            wait(1)

        wait(15 * 60 - 40)

        while True:
            point = match('myama', 0.8)
            if point is None:
                break
            click(*point)
            wait(0.5)
            swipe(820, 460, 1100, 700, 1000)
            wait(1)


def get_center(img):
    match_row = [_[2] for _ in img[1070]]
    # print(match_row)
    for index in range(1920):
        if match_row[index] < 110:
            left = index
            while index < 1920:
                if match_row[index] > 100:
                    return (left + index) >> 1
                index += 1


def fishing(only_king=False):
    module = 3.41 / 2
    swipe(565, 960, 565, 600)

    wait(3)

    start = time()
    img = screen_cap()
    img_a = cv2.imdecode(np.frombuffer(img, np.uint8), cv2.IMREAD_COLOR)
    label_x = match('label', 0.8, img_a[-300:])[0]
    center_x = get_center(img_a)
    king = match('king', 0.8, img_a[-300:])
    delay = time() - start

    delay += 0.4

    if king is not None:
        if (3840 - label_x - center_x) * module / 1920 - delay > 0:
            wait((3840 - label_x - center_x) * module / 1920 - delay)
        else:
            wait(0.1)
        click(565, 600)
        wait(2)
        adb('shell monkey -f /data/tap.mks -v 1')
        wait(0.5)
        click(565, 600)
        wait(5)

    elif only_king:
        if center_x < 1250:
            click(565, 600)
        else:
            wait((1920 - center_x + 330) * module / 1920)
            click(565, 600)
        wait(2.3)

    else:
        if (3840 - label_x - center_x) * module / 1920 - delay > 0:
            wait((3840 - label_x - center_x) * module / 1920 - delay)
        else:
            wait(0.1)
        click(565, 600)
        wait(5)


if __name__ == '__main__':

    # yama()

    while True:
        try:
            fishing(only_king=False)
        except Exception as e:
            print(e)
            wait(3)
            click(565, 600)
            wait(5)
            continue

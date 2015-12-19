# coding=utf-8
import time
import os
from datetime import datetime
from naoqi import ALBroker, ALProxy
from PIL import Image
from lib.qiwrapper import QiImage
from lib.converter import ImageConverter

PEPPER_IP = "192.168.10.101"
PEPPER_PORT = 9559

RESOLUTION = 0  # 0:160*120, 1:320*240, 7:80*60, 8:40*30
FRAMERATE = 15

# ref: Choregraphe Suite 2.4/share/doc/family/pepper_technical/video_pep.html?highlight=color space
RGB_CAMERA_NAME = "rgb_camera"
RGB_CAMERA_ID = 0  # top
RGB_COLOR_SPACE = 11  # AL::kRGBColorSpace
RGB_FILE_PREFIX = os.path.join(os.path.dirname(__file__), "images/rgb_raw")

TIMES = 20
WAIT = 0.1

broker = None


def main():
    global broker
    broker = ALBroker("myBroker", "0.0.0.0", 0, PEPPER_IP, PEPPER_PORT)

    # init camera
    video = ALProxy('ALVideoDevice')
    subscribers = video.getSubscribers()

    # init rgb camera
    exists_camera_name = "{0}_0".format(RGB_CAMERA_NAME)
    if exists_camera_name in subscribers:
        rgb_subscribe_id = exists_camera_name
    else:
        rgb_subscribe_id = video.subscribeCamera(RGB_CAMERA_NAME, RGB_CAMERA_ID, RESOLUTION, RGB_COLOR_SPACE, FRAMERATE)
    print u"rgb_subscribe_id: {0}".format(rgb_subscribe_id)

    # get image
    for i in range(0, TIMES):
        print u"try: {0} {1}".format(i, datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

        rgb_ary = video.getDirectRawImageRemote(rgb_subscribe_id)
        video.releaseImage(rgb_subscribe_id)
        rgb = QiImage(rgb_ary)

        savepath = RGB_FILE_PREFIX + "_" + str(i) + "_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".bmp"
        print len(rgb.binary)
        ary = zip(*[iter(list(bytearray(rgb.binary)))] * 4)
        ary2 = ImageConverter.yuv422ToRGB(ary)

        with Image.new("RGB", (rgb.width, rgb.height)) as im:
            im.putdata(ary2)
            im.save(savepath, format='bmp')

        time.sleep(WAIT)

    video.unsubscribe(rgb_subscribe_id)


if __name__ == '__main__':
    main()

# coding=utf-8
import time
import os
import struct
from datetime import datetime
from naoqi import ALBroker, ALProxy
from PIL import Image
from lib.qiwrapper import QiImage

PEPPER_IP = "192.168.10.101"
PEPPER_PORT = 9559

RESOLUTION = 0  # 0:160*120, 1:320*240, 7:80*60, 8:40*30
FRAMERATE = 15

# ref:Choregraphe Suite 2.4/share/doc/family/pepper_technical/video_3D_pep.html
DEPTH_CAMERA_NAME = "depth_camera"
DEPTH_CAMERA_ID = 2  # depth
DEPTH_COLOR_SPACE = 21  # AL::kDistanceColorSpace 2byte
# DEPTH_COLOR_SPACE = 17  # AL::kDepthColorSpace
DEPTH_FILE_PREFIX = os.path.join(os.path.dirname(__file__), "images/depth")

# ref: Choregraphe Suite 2.4/share/doc/family/pepper_technical/video_pep.html?highlight=color space
RGB_CAMERA_NAME = "rgb_camera"
RGB_CAMERA_ID = 0  # top
RGB_COLOR_SPACE = 11  # AL::kRGBColorSpace
RGB_FILE_PREFIX = os.path.join(os.path.dirname(__file__), "images/rgb")

BOTH_FILE_PREFIX = os.path.join(os.path.dirname(__file__), "images/both")

TIMES = 20
WAIT = 0.5

broker = None


def main():
    global broker
    broker = ALBroker("myBroker", "0.0.0.0", 0, PEPPER_IP, PEPPER_PORT)

    # init camera
    video = ALProxy('ALVideoDevice')
    subscribers = video.getSubscribers()

    # init depth camera
    exists_camera_name = "{0}_0".format(DEPTH_CAMERA_NAME)
    if exists_camera_name in subscribers:
        depth_subscribe_id = exists_camera_name
    else:
        depth_subscribe_id = video.subscribeCamera(DEPTH_CAMERA_NAME, DEPTH_CAMERA_ID, RESOLUTION, DEPTH_COLOR_SPACE, FRAMERATE)
    print u"subscribe_id: {0}".format(depth_subscribe_id)

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

        depth_ary = video.getImageRemote(depth_subscribe_id)
        rgb_ary = video.getImageRemote(rgb_subscribe_id)

        depth = QiImage(depth_ary)
        depth_binary = [struct.unpack('B', x)[0] for x in depth.binary]
        depth_save_path = DEPTH_FILE_PREFIX + "_" + str(i) + "_" + datetime.now().strftime("%Y%m%d_%H%M%S") + '.bmp'
        with Image.new("L", (depth.width, depth.height)) as im:
            im.putdata(depth_binary[::2])
            im.save(depth_save_path, format='bmp')
        print u"depth image file was created: {0}".format(depth_save_path)

        rgb = QiImage(rgb_ary)
        rgb_save_path = RGB_FILE_PREFIX + "_" + str(i) + "_" + datetime.now().strftime("%Y%m%d_%H%M%S") + '.bmp'
        rgb_binary = [struct.unpack('B', x)[0] for x in rgb.binary]
        with Image.new("RGB", (rgb.width, rgb.height)) as im:
            im.putdata(zip(*[iter(rgb_binary)] * 3))
            im.save(rgb_save_path, format='bmp')
        print u"rgb image file was created: {0}".format(rgb_save_path)

        both_save_path = BOTH_FILE_PREFIX + "_" + str(i) + "_" + datetime.now().strftime("%Y%m%d_%H%M%S") + '.bmp'
        with Image.new("RGB", (rgb.width, rgb.height * 2)) as im:
            im.putdata(zip(*[iter(rgb_binary)] * 3) + [(x, x, x) for x in depth_binary[::2]])
            im.save(both_save_path, format='bmp')
            im.show()
        print u"both image file was created: {0}".format(both_save_path)

        time.sleep(WAIT)

    video.unsubscribe(depth_subscribe_id)
    video.unsubscribe(rgb_subscribe_id)


if __name__ == '__main__':
    main()

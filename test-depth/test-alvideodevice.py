import time
from datetime import datetime
from naoqi import ALBroker, ALProxy
from PIL import Image

PEPPER_IP = "192.168.10.101"
PEPPER_PORT = 9559

CAMERA_NAME = "_depth_camera"
CAMERA_ID = 2  # depth
RESOLUTION = 1  # 320*240
FRAMERATE = 15
COLOR_SPACE = 17  # mono16 = 2byte
FILE_PREFIX = "images/depth"
TIMES = 20
WAIT = 0.5

broker = None


def main():
    global broker
    broker = ALBroker("myBroker", "0.0.0.0", 0, PEPPER_IP, PEPPER_PORT)

    # camera init
    video = ALProxy('ALVideoDevice')
    subscribers = video.getSubscribers()
    exists_camera_name = "{0}_0".format(CAMERA_NAME)
    if exists_camera_name in subscribers:
        subscribe_id = exists_camera_name
    else:
        subscribe_id = video.subscribeCamera(CAMERA_NAME, CAMERA_ID, RESOLUTION, COLOR_SPACE, FRAMERATE)
    print u"subscribe_id: {0}".format(subscribe_id)

    # get image
    for i in range(0, TIMES):
        print u"try: {0}".format(i)

        depth_ary = video.getImageRemote(subscribe_id)
        depth = NAOqiDepth(depth_ary)

        path = FILE_PREFIX + "_" + str(i) + "_" + datetime.now().strftime("%Y%m%d_%H%M%S") + '.bmp'
        # ref: http://effbot.org/imagingbook/decoder.htm
        with Image.new("L", (depth.width / 2, depth.height / 2)) as im:
            im.putdata(depth.binary[:((depth.width / 2) * (depth.height / 2))])
            im.save(path, format='bmp')

        print u"created: {0}".format(path)

        time.sleep(WAIT)

    video.unsubscribe(subscribe_id)


class NAOqiDepth:
    PARAMS = [
        'width', 'height', 'number_of_layer', 'color_space',
        'time_stamp_sec', 'time_stamp_ms',
        'binary',  # binary array of size height * width * nblayers containing image data.
        'cameraID',
        'left_angle', 'top_angle', 'right_angle', 'bottom_angle'
    ]

    def __init__(self, ary):
        for i, key in enumerate(self.PARAMS):
            setattr(self, key, ary[i])

if __name__ == '__main__':
    main()

# coding=utf-8


class QiImage:
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

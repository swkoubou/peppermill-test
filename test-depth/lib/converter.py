# coding=utf-8

class ImageConverter:
    @staticmethod
    def yuv422ToRGB(src):
        # [(U, Y, V, Y’)*]
        res = []
        for x in src:
            res.append(ImageConverter.yuvToRGB(x[0], x[1], x[3]))
            res.append(ImageConverter.yuvToRGB(x[2], x[1], x[3]))
        return res

    @staticmethod
    def yuvToRGB(y, u, v):
        r = 1.164 * (y - 16) + 0.000 * (u - 128) + 1.596 * (v - 128)
        g = 1.164 * (y - 16) - 0.391 * (u - 128) - 0.813 * (v - 128)
        b = 1.164 * (y - 16) + 2.018 * (u - 128) + 0.000 * (v - 128)
        return tuple(map(int, (r, g, b)))

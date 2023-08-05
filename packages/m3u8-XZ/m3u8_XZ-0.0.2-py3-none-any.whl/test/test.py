# -- coding:utf-8 --
# Time:2023-04-21 17:35
# Author:XZ
# File:test.py
# IED:PyCharm

from packaging_m3u8.m3u8_XZ.xz import M3U8


if __name__ == '__main__':
    url = "https://vip1.155bf.com/20221212/xoXK2XDb/1000kb/hls/max.m3u8"
    obj = M3U8(url=url, folder='有坂深雪2')
    # M3U8(m3u8_file='fileName.m3u8', folder='test')
    obj.run()



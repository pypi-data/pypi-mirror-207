#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      _base
   Description:
   Author:          dingyong.cui
   date：           2023/5/6
-------------------------------------------------
   Change Activity:
                    2023/5/6
-------------------------------------------------
"""
import cv2
import numpy
import os


class Image:

    def __init__(self, image: str):
        if os.path.isfile(image) is False:
            raise AssertionError('The image file does not exist: {}'.format(image))
        self.image = cv2.imread(image, cv2.IMREAD_UNCHANGED)

    @property
    def width(self):
        return self.image.shape[1]

    @property
    def height(self):
        return self.image.shape[0]


class MatchImg:

    def __init__(self, source: str, temp: str, threshold=0.95):
        self.source_img = Image(source)
        self.temp_img = Image(temp)
        self.threshold = threshold

    @property
    def mask(self):
        return self.parse_mask()

    def match_temp(self, method=cv2.TM_CCOEFF_NORMED):
        try:
            mt = cv2.matchTemplate(self.source_img.image, self.temp_img.image, method)
            locations = numpy.where(mt >= self.threshold)

            return list(zip(locations[1], locations[0]))
        except cv2.error as e:
            print(e)

    def parse_mask(self, match_method=cv2.TM_CCOEFF_NORMED):
        mask_list = []
        match_list = self.match_temp(method=match_method)
        for m in match_list:
            mj = {
                'type': 'coordinates',
                "page": "all",
                'x': m[0],
                'y': m[1],
                'width': self.temp_img.width,
                'height': self.temp_img.height
            }
            mask_list.append(mj)

        return mask_list

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      test_compare_image
   Description:
   Author:          dingyong.cui
   date：           2023/5/6
-------------------------------------------------
   Change Activity:
                    2023/5/6
-------------------------------------------------
"""


class TestCompareImage:

    def setup(self):
        from visual_compare.doc.visual_test import VisualTest
        self.cls = VisualTest
        self.image_base = '../../files/images/'

    def get_path(self, filename):
        return self.image_base + filename

    def test_compare_images(self):
        from visual_compare.doc.image.image import MatchImg
        img1 = self.get_path('123.png')
        img11 = self.get_path('000.png')
        img2 = self.get_path('124.png')
        mi = MatchImg(img1, img11)
        mask = mi.mask
        self.cls().compare_images(img1, img2, mask=mask)

    def test_compare_images_show_diff(self):
        from visual_compare.doc.image.image import MatchImg
        img1 = self.get_path('123.png')
        img11 = self.get_path('000.png')
        img2 = self.get_path('124.png')
        mi = MatchImg(img1, img11)
        mask = mi.mask
        self.cls(show_diff=True).compare_images(img1, img2, mask=mask)

    def test_compare_images_check_text_content(self):
        img1 = self.get_path('i1.png')
        img2 = self.get_path('i2.png')
        self.cls().compare_images(img1, img2, check_text_content=False)

    def test_compare_pdf(self):
        img1 = self.get_path('sample_1_page.pdf')
        img2 = self.get_path('sample_1_page_changed.pdf')
        self.cls().compare_images(img1, img2)

    def test_compare_pdf_watermark(self):
        img1 = self.get_path('sample_1_page.pdf')
        img2 = self.get_path('sample_1_page_with_watermark.pdf')
        self.cls().compare_images(img1, img2)

    # def test_compare_images_error_size(self):
    #     img1 = self.get_path('y1.png')
    #     img2 = self.get_path('y2.png')
    #     self.cls().compare_images(img1, img2, check_text_content=False)

    def test_compare_images_with_screenshot_dir(self):
        img1 = self.get_path('123.png')
        img2 = self.get_path('124.png')
        screenshot_dir = '/screenshots'
        cls = self.cls(screenshot_dir=screenshot_dir)
        cls.compare_images(img1, img2)
        assert cls.is_different is True

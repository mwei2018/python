# -*- coding: utf-8 -*-
"""
@Author  : mason
@File    : imggroup.py
@Time    : 2019/6/28
@desc    : 9张图片合并成九宫格
"""

from PIL import Image, ImageDraw
import os

import re


def load_image_list(folder):
    images = []
    image_file_list = [
        os.path.join(folder, item)
        for item in os.listdir(folder)
        if os.path.isfile(os.path.join(folder, item))
        and os.path.join(folder, item).endswith(".jpg")
    ]

    img_num = len(image_file_list)
    if img_num >= 9:
        for f in image_file_list[:9]:
            image = Image.open(f)
            images.append(image)
        return images
    else:
        print("请重新选择文件夹")


def fill_background(image):
    width, height = image.size
    side = min(width, height)

    new_image = Image.new(image.mode, (side, side), color="white")
    return new_image


def get_images_area(bg_image, images):

    width, height = bg_image.size
    one_third_width = int(width / 3)  # small image width
    # 保存每一个小切图的区域
    box_list = []

    for x in range(3):
        for y in range(3):
            left = x * one_third_width
            top = y * one_third_width
            box = (left, top)
            box_list.append(box)
    return box_list


def group_image(bg, area, images):
    one_third_width = int(bg.size[0] / 3)
    for index, img in enumerate(images):
        img.thumbnail((one_third_width, one_third_width))
        draw = ImageDraw.Draw(img)
        draw.text((10, 10), str(index + 1))
        bg.paste(img, (area[index][0], area[index][1]))
    output_path = os.path.abspath(os.path.dirname(__file__))
    bg.save(f"{output_path}/group.jpg", "jpeg")


def main():
    input_path = input("请输入图片路径：\n")
    images = load_image_list(input_path)
    new_image = fill_background(images[0])
    area = get_images_area(new_image, images)
    group_image(new_image, area, images)


if __name__ == "__main__":
    main()

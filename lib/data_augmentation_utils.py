#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 11:59:22 2022

@author: christiedu
"""

import imageio
import imgaug as ia
import imgaug.augmenters as iaa


def hflip(img):    
    flip_hr=iaa.Fliplr(p=1.0)
    flip_hr_image= flip_hr.augment_image(img)
    return flip_hr_image

def vflip(img):
    flip_vr=iaa.Flipud(p=1.0)
    flip_vr_image= flip_vr.augment_image(img)
    return flip_vr_image

def rotate(img):
    rotate1=iaa.Affine(rotate=(-90, -90))
    rotate2=iaa.Affine(rotate=(-180, -180))
    rotate3=iaa.Affine(rotate=(-270, -270))

    rotated_image1=rotate1.augment_image(img)
    rotated_image2=rotate2.augment_image(img)
    rotated_image3=rotate3.augment_image(img)
    
    return rotated_image1, rotated_image2, rotated_image3

def distort(img):   
    aug = iaa.PerspectiveTransform(scale=(0.01, 0.15))
    distort_image1 = aug.augment_image(img)
    distort_image2 = aug.augment_image(img)
    return distort_image1, distort_image2

def crop(img):
    crop = iaa.Crop(percent=(0, 0.3)) # crop image
    crop_image=crop.augment_image(img)
    return crop_image

def brightness(img):
    contrast1=iaa.GammaContrast(gamma=(0.5, 1.0))
    contrast2=iaa.GammaContrast(gamma=(1.0, 2.0))
    lighter = contrast1.augment_image(img)
    darker = contrast2.augment_image(img)
    return lighter, darker

def color(img):
    aug = iaa.GammaContrast((0.5, 2.0), per_channel=True)
    color_img = aug.augment_image(img)
    return color_img


image = imageio.imread("../data/train_data/images/00001.png")
ia.imshow(image)

flip_hr = hflip(image)
ia.imshow(flip_hr)

flip_vr = vflip(image)
ia.imshow(flip_vr)

rotated1, rotated2, rotated3 = rotate(image)
ia.imshow(rotated1)
ia.imshow(rotated2)
ia.imshow(rotated3)

distorted1, distorted2 = distort(image)
ia.imshow(distorted1)
ia.imshow(distorted2)

cropped = crop(image)
ia.imshow(cropped)

light, dark = brightness(image)
ia.imshow(dark)
ia.imshow(light)

colored = color(image)
ia.imshow(colored)


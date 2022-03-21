#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 11:59:22 2022

@author: christiedu
"""

import imageio
import imgaug as ia
import imgaug.augmenters as iaa
import random


ANGLES = [-90, -180, -270]

def flip(img):     
    choice = random.randint(0,1)
    if choice == 0:
        flip_hr=iaa.Fliplr(p=1.0)
        flip_hr_image= flip_hr.augment_image(img)
        return flip_hr_image
    else:
        flip_vr=iaa.Flipud(p=1.0)
        flip_vr_image= flip_vr.augment_image(img)
        return flip_vr_image

def rotate(img):
    choice = random.randint(0,2)
    angle = ANGLES[choice]
    
    rotate1=iaa.Affine(rotate=(angle, angle))
    rotated_image1=rotate1.augment_image(img)
    
    return rotated_image1

def distort(img):   
    aug = iaa.PerspectiveTransform(scale=(0.01, 0.15))
    distort_image1 = aug.augment_image(img)
    return distort_image1

def crop(img):
    crop = iaa.Crop(percent=(0, 0.3)) # crop image
    crop_image=crop.augment_image(img)
    return crop_image

def brightness(img):
    contrast = iaa.GammaContrast(gamma=(0.5, 1.5))
    contrast_image = contrast.augment_image(img)
    return contrast_image

def color(img):
    aug = iaa.GammaContrast((0.5, 2.0), per_channel=True)
    color_img = aug.augment_image(img)
    return color_img

def augment_clean(image):
  flipped = flip(image)
  rotated = rotate(image)
  distorted = distort(image)
  contrasted = brightness(image)
  colored = color(image)

  return flipped, rotated, distorted, contrasted, colored


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 11:21:29 2022

@author: christiedu
"""

import numpy as np
import cv2
import sys

# assumes data is in data folder
img_path = sys.argv[1]
n_img = int(sys.argv[2])

root = '../data/'
img_folder = root + img_path + '/'

print('Beginning.........')

imgs = np.empty((n_img,32,32,3))
for i in range(n_img):
    if i % 1000 == 0:
      print('.', end='')
    img_fn = img_folder+f'test{i+1:05d}.png'
    imgs[i,:,:,:]=cv2.cvtColor(cv2.imread(img_fn),cv2.COLOR_BGR2RGB)

    
print("\nCompleted data loading.........")

np.save('../output/test_imgs.npy', imgs)

print("Saved data + Finished.........")
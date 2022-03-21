#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 18:40:16 2022

@author: christiedu
"""

import numpy as np
import cv2

from data_augmentation_utils import augment_clean

train_images = '../data/train_data/images/'
clean_images_labels = '../data/train_data/clean_labels.csv'
noisy_images_labels = '../data/train_data/noisy_labels.csv'

print('Beginning.........')

# load the images
n_img = 50000
n_noisy = 40000
n_clean_noisy = n_img - n_noisy
imgs = np.empty((n_img,32,32,3))
for i in range(n_img):
    if i % 1000 == 0:
      print('.', end='')
    img_fn = train_images+f'{i+1:05d}.png'
    imgs[i,:,:,:]=cv2.cvtColor(cv2.imread(img_fn),cv2.COLOR_BGR2RGB)
    
# load the labels
clean_labels = np.genfromtxt(clean_images_labels, delimiter=',', dtype="int8")
noisy_labels = np.genfromtxt(noisy_images_labels, delimiter=',', dtype="int8")
    
print("\nCompleted data loading.........")
    
clean_imgs = imgs[:10000]
noisy_imgs = imgs[10000:]

np.save('../output/clean_img.npy', clean_imgs)
np.save('../output/noisy_img.npy', noisy_imgs)

print('Saved clean and noisy npy files in output.........')

print('Creating augmented images.........')

AUG_COUNT = 5
n_clean_aug = AUG_COUNT*n_clean_noisy
clean_aug_imgs = np.empty((n_clean_aug,32,32,3))
for i in range(n_clean_noisy):
  if i % 1000 == 0:
    print('.', end="")

  img_name = f'{i+1:05d}'
  flipped, rotated, distorted, contrasted, colored = augment_clean(imgs[i]/255)

  # add to clean augmented array
  clean_aug_imgs[AUG_COUNT*i] = flipped*255
  clean_aug_imgs[AUG_COUNT*i + 1] = rotated*255
  clean_aug_imgs[AUG_COUNT*i + 2] = distorted*255
  clean_aug_imgs[AUG_COUNT*i + 3] = contrasted*255
  clean_aug_imgs[AUG_COUNT*i + 4] = colored*255
  
np.save('../output/aug_clean_img.npy', clean_aug_imgs)

print('\nSaved augmented npy files in output.........')

print('Creating new labels.........')

aug_labels = np.empty(n_clean_aug)

for i in range(n_clean_noisy):
  label = clean_labels[i]
  aug_labels[5*i] = label
  aug_labels[5*i + 1] = label
  aug_labels[5*i + 2] = label
  aug_labels[5*i + 3] = label
  aug_labels[5*i + 4] = label
  
combined_labels = np.concatenate((clean_labels, noisy_labels[10000:],
                                  aug_labels))

np.save('../output/combined_labels.npy', combined_labels)

print('Saved combined labels npy in output.........')

print('Complete.........')
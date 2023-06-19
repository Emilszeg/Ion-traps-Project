#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 17:01:25 2023

@author: tthyme
"""

import matplotlib.pyplot as plt

x = [18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
yfm = [7.5,8.02,8.57,9.14,9.74,10.4,11.1,16.3,40,53,71,92,118,138.4,164]
ynm = [7.44,8,8.53,9.05,9.66,10.3,10.9,11.7,12.7,14.4,22.1,43,66,88,110]
yfl =[6.26,6.72,7.18,7.64,8.18,8.74,9.47,38.5,67.7,97.7,128,159,188,220,250]
ynl =[6.41,6.86,7.29,7.77,8.31,8.86,9.5,10.3,11.3,13.4,25.6,54,83.2,114,144]

fig = plt.figure()
ax = fig.add_subplot(111)

ax.scatter(x, yfm, s=2, c='b', marker="s", label='Feedback Littman-Metcalf')
ax.scatter(x,ynm, s=2, c='r', marker="o", label='No feedback Littman-Metcalf')
ax.scatter(x, yfl, s=2, c='g', marker="s", label='Feedback Littrow')
ax.scatter(x,ynl, s=2, c='y', marker="o", label='No feedback Littrow')
ax.set_ylim([0, 260])
plt.title("Power output of a laser with and without optical feedback.")
plt.xlabel("Current in mA")
plt.ylabel("Power in µW")
plt.legend(loc='upper left')
plt.show()

#%%

plt.plot(x,yfm, c='b',label='Feedback Littman-Metcalf')
plt.plot(x,ynm, c='r',label='No feedback Littman-Metcalf')
plt.plot(x,yfl, c='g',label='Feedback Littrow')
plt.plot(x,ynl, c='y',label='No feedback Littrow')
plt.title("Power output of a laser with and without optical feedback.")
plt.xlabel("Current in mA")
plt.ylabel("Power in µW")
plt.legend(loc='upper left')
plt.show()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 14:34:12 2023

@author: tthyme
"""

import matplotlib.pyplot as plt

x = [15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
yf = [22.4,22.7,22.8,23.3,23.6,23.9,24.3,24.7,25.1,25.5,31.5,47,61.9,76,90.3,105]
yn = [22.4,22.7,23,23.4,23.7,24.1,24.4,24.9,25.1,25.8,26.3,27,28.7,37.9,55.8,73.8]
fig = plt.figure()
ax = fig.add_subplot(111)

ax.scatter(x, yf, s=2, c='b', marker="s", label='Feedback')
ax.scatter(x,yn, s=2, c='r', marker="o", label='No feedback')
ax.set_ylim([0, 130])
plt.title("Power output of a laser with and without optical feedback.")
plt.xlabel("Current in mA")
plt.ylabel("Power in µW")
plt.axvline(x=24,color='b',linestyle='dashed',linewidth=0.75, label="Lasing point feedback")
plt.axvline(x=27,color='r',linestyle='dashed',linewidth=0.70, label="Lasing point no feedback")
plt.legend(loc='upper left')
plt.show()
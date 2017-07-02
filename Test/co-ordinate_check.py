# -*- coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

img_org = cv2.imread('process_img.png',0)
edges_org = cv2.Canny(img_org,100,200)

#cv2.rectangle(img, (x1, y1), (x2, y2), (255,0,0), 2)
#cv2.rectangle(edges_org, (20, 35), (230, 210), (255,0,0), 2)
#cv2.rectangle(edges_org, (8, 240), (230, 430), (255,0,0), 2)
#cv2.rectangle(edges_org, (410, 195), (605, 20), (255,0,0), 2)
#cv2.rectangle(edges_org, (415, 230), (630, 410), (255,0,0), 2)

plt.imshow(edges_org,cmap = 'gray')
plt.title('Check by tracing Cursor'), plt.xticks([]), plt.yticks([])
plt.show()

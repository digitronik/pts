# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#    Platform        : PTS
#    Project Name    : Parking Assistant
#    Author          : Nikhil Dhandre
#    Start Date      : 01-07-2017
#    Last Modified   : 02-07-2017
#------------------------------------------------------------------------------
#------------------------Importing Libraries-----------------------------------
import cv2
import numpy as np
from matplotlib import pyplot as plt
from camera import *
#------------------------------------------------------------------------------


#--------------------------Canny Edge Algorithm--------------------------------
def auto_canny(image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(image)
    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)

    # return the edged image
    return edged
#------------------------------------------------------------------------------

#-------------------------Count fuction for pixel calculation------------------
def cal_count(edges,x1,y1,x2,y2):
    #global edges
    count=0

    for y in range(y1,y2):
        for x in range(x1,x2):
            if edges[y][x] != 0:
                #print "[",x,"]","[",y,"] =",edges[x][y]
                count+=1
    return count
#------------------------------------------------------------------------------


def main():
    #pass
    #capture_img()    # capturing img

    img = cv2.imread('2017-07-02-001321.jpg',0)     #import img
    edges=auto_canny(img)               #send for canny edges calculation
    height = np.size(img, 0)
    width = np.size(img, 1)
    #print height
    #print width

    #cv2.rectangle(edges, (20, 35), (230, 210), (255,0,0), 2)
    slot_1=cal_count(edges, 20, 35, 230, 210)

    #cv2.rectangle(edges, (8, 240), (230, 430), (255,0,0), 2)
    slot_2=cal_count(edges, 8, 240, 230, 430)

    #cv2.rectangle(edges_org, (410, 195), (605, 20), (255,0,0), 2)
    slot_3=cal_count(edges, 410, 195, 605, 20)

    #cv2.rectangle(edges_org, (415, 230), (630, 410), (255,0,0), 2)
    slot_4=cal_count(edges, 415, 230, 630, 410)

    print slot_1, slot_2, slot_3,slot_4


#----------------------------main----------------------------------------------

if __name__ == "__main__":
    main()


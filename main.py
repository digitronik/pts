# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#    Platform        : main.py
#    Project Name    : Parking System
#    Author          : Nikhil Dhandre
#    Start Date      : 01-07-2017
#    Last Modified   : 01-07-2017
#------------------------------------------------------------------------------

#-----------------------------import lib---------------------------------------
import telepot
import time
import cv2
import numpy as np

#------------------------------------------------------------------------------

#---------------------------Camera Image Take---------------------------------
def capture_img():
    camera_port = 1
    ramp_frames = 30
    camera = cv2.VideoCapture(camera_port)

    def get_image():
        retval, im = camera.read()
        return im

    print("Taking image...")
    camera_capture = get_image()

    file = "process_img.png"
    cv2.imwrite(file, camera_capture)
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

def solt_info():
    img = cv2.imread('2017-07-02-001321.jpg',0)     #import img
    edges=auto_canny(img)               #send for canny edges calculation
    #height = np.size(img, 0)
    #width = np.size(img, 1)

    #cv2.rectangle(edges, (20, 35), (230, 210), (255,0,0), 2)
    slot_1=cal_count(edges, 20, 35, 230, 210)

    #cv2.rectangle(edges, (8, 240), (230, 430), (255,0,0), 2)
    slot_2=cal_count(edges, 8, 240, 230, 430)

    #cv2.rectangle(edges_org, (410, 195), (605, 20), (255,0,0), 2)
    slot_3=cal_count(edges, 410, 195, 605, 20)

    #cv2.rectangle(edges_org, (415, 230), (630, 410), (255,0,0), 2)
    slot_4=cal_count(edges, 415, 230, 630, 410)

    slots = [slot_1,slot_2,slot_3,slot_4]

    for s in slots:
        if s > 50:
            slots[slots.index(s)] = "Not Available"
        else:
            slots[slots.index(s)] = "Available"
    return slots




#-----------------------send_slot info------------------------------------------
def send_txt(chat_id, msg):
    bot.sendMessage(chat_id, msg)

#-----------------------send_slot_photo----------------------------------------
def send_photo(chat_id, photo, caption=None):
    with open(photo, mode="r") as f:
        bot.sendPhoto(chat_id,f, caption)

#-------------------------input masg handle loop -------------------------------
def handle(msg):
    #print msg
    try:
        date = msg['date']
        usr_name = msg['from']['username']
        chat_id = msg['chat']['id']
        msg_id = msg['message_id']
        command = msg['text']
    except:
        print("Unexpected msg")
        pass
    else:
        print 'Got command: %s' % command

        if command == "photo":
            try:
                capture_img()
            except:
                print "fail to capture Image"
            else:
                send_photo(chat_id, "process_img.png")

        if command == "slots":
            try:
                capture_img()
                time.sleep(1)
                slots = solt_info()
            except:
                print("Fail to send slots info")
            else:
                msg = "Parking Slots : \n" +"Slot-1: "+slots[0]+"\n" + "Slot-2: "+slots[1]+"\n"+ "Slot-3: "+slots[2]+"\n"+ "Slot-4: "+slots[3]
                send_txt(chat_id, msg)

        if command == "available slots":
            try:
                capture_img()
                time.sleep(1)
                slots = solt_info()
            except:
                print("Fail to send slots info")
            else:
                msg = "Available Slots \n"

                for s_no, s in enumerate(slots, start=1):
                    count=0
                    if s == "Available":
                        msg +="slot: "+ str(s_no) +"\n"
                        count+=1
                if count == 0:
                    msg = "Parking Full"

                send_txt(chat_id, msg)
                        #commands(chat_id, msg_id, date, command, usr_name, first_name, last_name)









#-------------------------Digi-server-bot config -------------------------------
bot = telepot.Bot('415740423:AAHZ2rZluf2Nd7vR9hgvf3eoUQIWsIwqJLY')
bot.message_loop(handle)
print 'I am listening...'

while 1:
    time.sleep(1)
# -*- coding: utf-8 -*-
import cv2

def capture_img():
    camera_port = 0
    ramp_frames = 30
    camera = cv2.VideoCapture(camera_port)

    def get_image():
        retval, im = camera.read()
        return im

    print("Taking image...")
    camera_capture = get_image()

    file = "process_img.png"
    cv2.imwrite(file, camera_capture)

    #del(camera)
if __name__ == "__main__":
    capture_img()
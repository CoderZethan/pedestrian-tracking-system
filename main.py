#! /usr/bin/python3
import numpy as np
from detector import Detector
import cv2
import monitorThread

# syscamera = monitorThread.monitor(0) # 创建系统摄像头对象0
result = np.zeros ((540, 1920, 3), np.uint8)
if __name__ == '__main__':
    while True:
        usb1 = monitorThread.monitor(1)  # 创建外接摄像头对象1
        usb1.run()
        result[0:540, 0:960] = usb1.output_image_frame
        usb2 = monitorThread.monitor(0)  # 创建外接摄像头对象2
        usb2.run()
        result[0:540, 960:1920] = usb2.output_image_frame
        cv2.imshow('self.id',result)
        cv2.waitKey(1)
        print("一次循环结束") 
    cv2.destroyAllWindows()
              



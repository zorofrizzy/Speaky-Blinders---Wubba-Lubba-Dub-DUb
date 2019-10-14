from time import sleep
from picamera import PiCamera
import cv2
import numpy
import os
import subprocess


camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
# Camera warm-up time
sleep(2)
camera.capture('clipp.jpg')
camera.stop_preview()

                                                                                                                 
ama=cv2.imread("clipp.jpg")
grayConverted = cv2.cvtColor(ama, cv2.COLOR_BGR2GRAY)
binary = cv2.threshold(grayConverted, 200,255, cv2.THRESH_BINARY)[1]
#img_not = cv2.bitwise_not(binary)
cv2.imwrite("testconv.jpg", binary)

p = subprocess.Popen(["tesseract", "--tessdata-dir", "/usr/share/tesseract-ocr", "testconv.jpg", "zorotext", "-l", "eng", "-psm", "3"], stdout=subprocess.PIPE)
output, err = p.communicate()
print output

with open('zorotext.txt', 'r') as file:
    k = file.read().replace('\n', '')

     
os.system('echo "{0}" | festival --tts'.format(k)) 

print(k)

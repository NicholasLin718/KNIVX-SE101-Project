from picamera import PiCamera
from time import sleep
camera=PiCamera()
#rotate picture
camera.rotation=180
#camera resolution
camera.resolution=(200, 200)
#take picture
camera.start_preview()
sleep(5)
camera.capture('/home/pi/test1.jpg')
camera.stop_preview()
print("Picture taken")
#save picture to local computer 


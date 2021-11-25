import picamera
print("About to take picture")
with picamera.PiCamera() as camera:
	camera.resolution=(200,200)
	camera.capture("/home/pi/Picam/myimages/test.jpg")
print("Picture taken")

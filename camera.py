import picamera
import time
import dronekit
from pexif import JpegFile
from time import sleep

camera = picamera.PiCamera()

vehicle = dronekit.connect('/dev/ttyACM0', wait_ready=False, baud=115200)

#camera.start_preview()

f = open('image/image.txt', 'a')
i = 0

while True:
	latitude = vehicle.location.global_frame.lat
	longtitude = vehicle.location.global_frame.lon
	sleep(1)
	filename = '%s.jpg' % i
	camera.capture('image/'+filename)
	ef = JpegFile.fromFile('image/'+filename)
	ef.set_geo(float(latitude), float(longtitude))
	ef.writeFile('image/'+filename)
	str = '%s,%s\t'%(latitude, longtitude)
	f.write(str)
	f.write(filename)
	f.write('\n')
	print (latitude, longtitude)
	i+=1
f.close()

#camera.stop_preview()

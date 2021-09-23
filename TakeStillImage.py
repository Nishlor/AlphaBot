from picamera import PiCamera, Color
from time import sleep
from datetime import datetime

camera = PiCamera()
#camera.start_preview() #stream through the HDMI port
#sleep(5)

#write an annotation on the image
camera.annotate_background = Color('black')
camera.annotate_foreground = Color('white')
timeMark = datetime.today().strftime("20%y%b%d %H:%M:%S")
camera.annotate_text = timeMark

#camera properties
#camera.brightness = 90 # from 0 to 100, default 50
#camera.contrast = 0 # from -100 to 100, default 0

locationToStorePhoto = '/home/pi/ImagesCaptured/'
photoName = timeMark
#take a photo
camera.capture(locationToStorePhoto + 'stillImage' + photoName + '.jpg')

#record video
camera.framerate = 24
camera.start_recording(locationToStorePhoto + 'video' + photoName + '.h264')
sleep(15)
camera.stop_recording

#camera.stop_preview()

camera.close()

from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview(fullscreen=False,window=(60,-120,800,800))
sleep(20)

camera.stop_preview()

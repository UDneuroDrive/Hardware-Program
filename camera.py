from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (208, 160)
camera.framerate = 40
camera.sharpness = 0
camera.contrast = 0
camera.brightness = 50
camera.saturation = 0
camera.ISO = 0
camera.exposure_compensation = 0
camera.exposure_mode = 'auto'
camera.meter_mode = 'average'
camera.awb_mode = 'auto'
camera.image_effect = 'none'
camera.color_effects = None
camera.rotation = 0
camera.hflip = False
camera.vflip = False
# camera.crop = (0.0, 0.0, 1.0, 1.0)

for x in range(1000):
    if(x%10 == 0):
        print(str((x/1000.00)*100) + "%" )
    camera.capture('/home/pi/neuroDrive/images/' + str(x) + ".jpg", use_video_port = True)
    #Image processing here
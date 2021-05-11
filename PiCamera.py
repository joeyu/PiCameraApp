from gpiozero import Button
from picamera import PiCamera
import time
from datetime import datetime, timedelta
import io
import json

def load_config(config_file):
    """
    Args:
        config_file: file name.
    Returns:
        config object.
    """
    config = None
    with io.open(config_file, 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    return config

def shutter_pressed():
    """
    Callback function when shutter is pressed.
    """
    timestamp = datetime.today().strftime("%Y-%m-%d-%H-%M-%S")
    camera.capture('/home/pi/Pictures/%s.jpg' % timestamp)
    return
    
button_shutter = Button(26)
button_shutter.when_pressed = shutter_pressed

config = load_config('config.json')

with PiCamera() as camera:
    camera.resolution = config['camera']['resolution']
    print("camera.resolution = %s" % (camera.resolution, ) )
    camera.framerate = config['camera']['framerate']
    camera.start_preview()
    while True:
        shutter_pressed()
        #button.wait_for_press()
        time.sleep(5)

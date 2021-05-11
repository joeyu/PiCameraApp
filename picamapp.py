import logging
import time
from datetime import datetime, timedelta
from gpiozero import Button
from picamera import PiCamera
from picamconfig import Config

logging.basicConfig(level=logging.DEBUG)

_config_file = "config.json"

def browse_picture():
    return

def shutter_pressed():
    """
    Callback function when shutter is pressed.
    """
    timestamp = datetime.today().strftime("%Y-%m-%d-%H-%M-%S")
    camera.capture(f"{_config['picture_directory']}/{timestamp}.jpg")
    return
    
button_shutter = Button(26)
button_shutter.when_pressed = shutter_pressed

_config = Config(_config_file)

with PiCamera() as camera:
    camera.resolution = _config['camera']['resolution']
    logging.debug(f"camera.resolution = {camera.resolution!r}")
    camera.framerate = _config['camera']['framerate']
    camera.start_preview()
    while True:
        shutter_pressed()
        #button.wait_for_press()
        time.sleep(5)

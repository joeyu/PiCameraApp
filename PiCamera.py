import logging
import io
import json
import time
from datetime import datetime, timedelta
from gpiozero import Button
from picamera import PiCamera

logging.basicConfig(level=logging.DEBUG)

config_file = "config.json"

def load_config(config_file:str):
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

def save_config(config_file:str, config):
    """
    Save the config into a json file.
    """
    with open(config_file, 'w', encoding='utf-8') as f:
        f.write(json.dumps(config, ensure_ascii=False, indent=4))
        logging.info(f"Wrote file '{fp}'.")    

def shutter_pressed():
    """
    Callback function when shutter is pressed.
    """
    timestamp = datetime.today().strftime("%Y-%m-%d-%H-%M-%S")
    camera.capture(f"{config['picture_directory']}/{timestamp}.jpg")
    return
    
button_shutter = Button(26)
button_shutter.when_pressed = shutter_pressed

config = load_config(config_file)

with PiCamera() as camera:
    camera.resolution = config['camera']['resolution']
    logging.debug(f"camera.resolution = {camera.resolution!r}")
    camera.framerate = config['camera']['framerate']
    camera.start_preview()
    while True:
        shutter_pressed()
        #button.wait_for_press()
        time.sleep(5)

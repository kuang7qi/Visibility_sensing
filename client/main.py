import create_fog_image
import visibility
import publish
import time

on_pi = 0 # FOR RASPBERRY PI, SET IT TO 1

while(True):
    if(on_pi):
        from picamera import PiCamera
        camera = PiCamera()
        camera.capture('current_image.png')
    else:
        create_fog_image.foggy_image('road.jpg', 'fog.jpg', fog_weight=1) # Creating a foggy image
    
    current_image_taken = 'current_image.png'
    default_image_to_compare = 'to_compare.png' # Default image to compare
    # Get visibility
    current_visibility = visibility.get_visibility(current_image_taken, default_image_to_compare)
    current_visibility = str("%0.2f" % current_visibility)
    # Publish the message to the server
    publish.message(current_visibility)
    time.sleep(2) # Every 10 minutes


import keyboard
from time import sleep
import camera
import mlscript

while True:  # making a loop

    if keyboard.is_pressed('Space'):  # if key 'q' is pressed 
        print('You Pressed A Key!') 
        camera.takePhoto()
        mlscript.predict('/') 

        sleep(1)
    if keyboard.is_pressed('Esc'):
        print('Done')
        break

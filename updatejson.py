import keyboard  # using module keyboard
import time
import json


path = 'data.json'
with open(path, 'r') as f:
    data = json.load(f)

while True:  
    if keyboard.is_pressed('l'):  # if key 'q' is pressed 
        print("Letter predicted: L")

        data["input"] += 'l'
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)    
        time.sleep(1)
    if keyboard.is_pressed('a'):  # if key 'q' is pressed 
        print("Letter predicted: A")

        data["input"] += 'a'
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)    
        time.sleep(1)
    if keyboard.is_pressed('t'):  # if key 'q' is pressed 
        print("Letter predicted: T")

        data["input"] += 't'
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)    
        time.sleep(1)

    if keyboard.is_pressed('e'):  # if key 'q' is pressed 
        print("Letter predicted: E")
        data["input"] += 'e'
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)    
        time.sleep(1)
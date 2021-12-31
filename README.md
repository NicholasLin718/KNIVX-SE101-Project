# 🤲 Ephphatha - ASL Translator

In the world of silence, it is challenging to learn written English without knowing the sounds of words and letters. A recent study shows that on average, a deaf high school senior is likely to read at the level of a nine-year-old. We designed this project as a solution to tackle this challenge: an ASL translator built from a Raspberry Pi that recognizes ASL hand signals in an image and translates the signals into written English.

# 💻 How We Built It 

This project was split into two major sections, the hardware and the software, connected through the main computing center of the Raspberry Pi. 

The camera used in this implementation was a Pi Camera, which was connected directly to the Raspberry Pi. Using a Python script, photos were taken using key presses and then saved in the internal storage of the Raspberry Pi. Practically, this was used in order to take pictures of each of the ASL hand signs, saving them so they could later be accessed by software. 

The Raspberry Pi was connected via both wifi and SSH to local machines for exchange of files, and information. This was later done with Git to allow for collaboration and to employ version control. A monitor and related peripherals, such as a keyboard and mouse, were connected for display purposes to show the web application along with a preview of the camera outputs before the photo is taken.

The software section consisted of three basic steps, the image processing, machine learning, and the display of the outputs. The image processing is partially done with the code for the camera, where the image size was set, but the rest is implemented through a Python script on the Raspberry Pi. The Python Imaging Library was used to standardize the pixel values of each image in order to compare them to those in the dataset for machine learning. In practice, this could be equated to fixing the contrast and brightness values, such as through lightening an image. 

After each image is standardized and turned into the proper Tensor data type, it is passed to our machine learning model for prediction. This model was trained using a Resnet neural network using Pytorch on a virtual machine with an online ASL alphabet dataset consisting of 3000 images of each of the letters of the alphabet along with symbols for space and delete. This model, along with the prediction algorithm is run locally on the Pi and returns the output into a JSON file. Also running on the Pi is our Flask web application which periodically reads the JSON file, and displays the output in sentences. 

In practice, as the app is run, the camera is started up, and upon keypresses, images are taken of different ASL signs and returned to a folder. The Raspberry Pi runs the image processing and machine learning functions on this to output a letter into a JSON file. This file is then read in live time and its output is printed into our Flask application.

# ➡️ Future Improvements

A potential improvement to the product would be translating hand signals for words rather than letters to improve efficiency and viability. In order to do this, we would have to train the machine learning model to recognize signals paired with movements, thereby allowing the model to translate hand signals for words. Also, the dataset to train the machine learning model did not include a variety of backgrounds, skin tones, and lightings. As aforementioned, it means that the improvements to this product will require a new dataset that includes word signals in different backgrounds and etc.

# Learn More

 This project was developed by 5 first year Software Engineering students from the University of Waterloo: Kristy Lau, Nicholas Lin, Ivan Hu, Varshaa Maxwell, and Xin Huey Wong. 
 
 [Watch Demo](https://youtu.be/Kypr42PMlr0)

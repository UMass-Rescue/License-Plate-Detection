# License Plate Detection

## Motivation
1. Rescue Lab works with Federal Agents to rescue children from sexual abuse and internet-based victimization,
2. As a part of the investigation recognizing a car from its license plate has proved to be really helpful,
3. Currently Federal Agents manually look through videos and images to find a license plate. This requires a lot of human resources which can be used elsewhere during a time-sensitive investigation,
4. Automating this process of identifying license plates can help speed up an investigation while allowing the Federal Agents to engage with other tasks. 

## Technical Approach (Machine Learning)
1. Extract image frames from the video, 
2. Find all contours in the image frame,
3. Find the bounding rectangle of every contour,
4. Compare and validate the sides ratio and area of every bounding rectangle with an average license plate,
5. Apply image segmentation in the image inside the validated contour to find characters in it, 
6. Recognize characters using a Neural Network OCR.

## Instructions/Setup
1. Clone the repository using 
```
git clone https://github.com/UMass-Rescue/License-Plate-Detection
```
2. Download your own or the test video available at https://drive.google.com/open?id=1jd8WVKHYXfisMO390easOdPkZahonRNd 
3. Run the main.py file using
```
python3 main.py
```
4. Go to the local server that the Flask website is hosted on. On Macs it will most likely be: http://127.0.0.1:5000/
5. Click on 'Choose File' and upload the test video by clicking 'Get Plates'. Note: the video can now be found in the static/files directory
6. After about 5 minutes the website will return License Plate Numbers with a timestamp corresponding to the time they were identified
7. Link to my Google Colab for License Plate Detection for images: https://colab.research.google.com/drive/1hPK7hzUhKYIfh1jMF8VB39ngpNN-38l_?usp=sharing

## Implementation (Completed, On-going, Future Plans)
### Completed
1. License Identification Model from Images,
2. License Identification Model from Videos,
3. Flask Web Application for both FrontEnd and BackEnd.

### On-going
1. ReactJS Web Application for FrontEnd,
2. Integrating License Identification Model from Images with the FrontEnd,
3. Containerize the Models using Docker.

### Future Plans
1. Improve the accuracy of the License Detection/Indentification Models,
2. Take a Number Plate as an Input and try identifying it in Images/Videos.


## Dependencies:
<pre>
opencv-python 3.4.2<br>
numpy 1.17.2<br>
skimage 0.16.2<br>
tensorflow 1.15.0<br>
imutils 0.5.3</pre>

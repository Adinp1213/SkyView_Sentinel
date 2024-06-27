from django.shortcuts import render
import ultralytics
from ultralytics import YOLO
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
from PIL import Image
model = YOLO('home/best.pt')

# Create your views here.
def index(request):
    return render(request,'index2.html')

def start_detection(request):
    return render(request,'upload_image.html')

def get_results(request):
    if request.method == 'POST':
        image = request.FILES['image']
        image = Image.open(image)
        
        #img = cv2.imdecode(np.fromstring(img.read(), np.uint8), cv2.IMREAD_COLOR)
        prediction = model.predict(image, imgsz=512)
        
        predicted_image = prediction[0].plot()
        plt.ioff()
        plt.imshow(predicted_image)
        plt.savefig('media/predicted_image.jpeg')
        # predicted_image_pil = Image.fromarray(np.uint8(predicted_image))
        # predicted_image_pil.show()
    return render(request,'get_results.html')

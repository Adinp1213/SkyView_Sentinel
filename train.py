import torch
print(torch.__version__)
import ultralytics
from ultralytics import YOLO
model = YOLO("yolo8x_adam.pt")  
results = model.train(data='D:/X_View_Refreshed_Project/military_xview.yaml', epochs=100, imgsz=640)
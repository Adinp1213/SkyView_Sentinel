# SkyView Sentinel

A proposed solution for military-based overhead satellite imagery object detection.

## Project Workflow
<p align="center">
  <img src="https://github.com/user-attachments/assets/2024ec31-5a9d-444f-a03e-8d208c4a7e51" alt="Gantt Chart" width="700">
</p>

## Project Overview
The project starts with initial research on the problem statement, followed by dataset preprocessing. Next, deep models are trained and evaluated using the preprocessed dataset, and the results are thoroughly analyzed. Finally, a website application is developed to enable users to obtain detailed detections from real-time satellite images.

<p align="center">
  <img src="https://github.com/user-attachments/assets/6163f4d8-ee46-4d58-a873-80753caef222" alt="Project Overview" width="900">
</p>

## Model Used
YOLOv8


## Detected Objects Results
<p align="center">
  <img src="https://github.com/user-attachments/assets/419e4d22-d6d1-494b-9e94-7d990db55a7c" alt="Results website" width="250">
  <img src="https://github.com/user-attachments/assets/d44bacc8-487d-4bfa-8bc9-d2d77d7d3ceb" alt="Results website" width="250">
  <img src="https://github.com/user-attachments/assets/9745c763-7025-4aca-9d60-4a8ad0e0e209" alt="Results website" width="250">
</p>

## mAP50 Table

| Classes                         | Images | Instances | mAP50 |
|---------------------------------|--------|-----------|-------|
| Small Aircraft                  | 1229   | 367       | 0.718 |
| Passenger/Cargo Plane           | 1229   | 320       | 0.703 |
| Helicopter                      | 1229   | 80        | 0.621 |
| Fixed-wing Aircraft             | 1229   | 28        | 0.205 |
| Tank Car                        | 1229   | 18        | 0.004 |
| Truck Tractor w/ Box Trailer    | 1229   | 2090      | 0.239 |
| Military Vessel                 | 1229   | 393       | 0.265 |
| Aircraft Hangar                 | 1229   | 82        | 0.004 |
| Tower                           | 1229   | 66        | 0.078 |
| Overall                         | 1229   | 3444      | 0.315 |

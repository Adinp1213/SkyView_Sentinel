import os
from PIL import Image

def get_image_dimensions(image_path):
    with Image.open(image_path) as img:
        return img.size

def normalize_coordinates(label_file_path, image_path):
    image_width, image_height = get_image_dimensions(image_path)

    with open(label_file_path, 'r') as file:
        lines = file.readlines()

    normalized_lines = []
    for line in lines:
        class_id, x1, y1, x2, y2 = map(float, line.split())
        x_center = (x1 + x2) / 2
        y_center = (y1 + y2) / 2
        width = x2 - x1 + 1
        height = y2 - y1 + 1

        # Normalize coordinates
        normalized_x_center = x_center / image_width
        normalized_y_center = y_center / image_height
        normalized_width = width / image_width
        normalized_height = height / image_height

        # Ensure the normalized values are within the bounds [0, 1]
        normalized_x_center = max(0, min(1, normalized_x_center))
        normalized_y_center = max(0, min(1, normalized_y_center))
        normalized_width = max(0, min(1, normalized_width))
        normalized_height = max(0, min(1, normalized_height))

        normalized_line = f"{int(class_id)} {normalized_x_center:.6f} {normalized_y_center:.6f} {normalized_width:.6f} {normalized_height:.6f}\n"

        normalized_lines.append(normalized_line)

    with open(label_file_path, 'w') as file:
        file.writelines(normalized_lines)

# Specify the path to the folder containing image and label files
images_folder = "D:/X_View_Refreshed_Project/YOLO_Format_Dataset/Experiment_Dataset/Images"
labels_folder = "D:/X_View_Refreshed_Project/YOLO_Format_Dataset/Experiment_Dataset/Labels"

# Iterate over label files in the folder
for filename in os.listdir(labels_folder):
    if filename.endswith(".txt"):
        label_file_path = os.path.join(labels_folder, filename)
        image_file_path = os.path.join(images_folder, filename.replace(".txt", ".tif"))

        # Check if the image file exists
        if os.path.exists(image_file_path):
            # Normalize the coordinates in the label file using image dimensions
            normalize_coordinates(label_file_path, image_file_path)
            print(f"Normalized coordinates in {filename}")
        else:
            print(f"Image file not found for {filename}. Deleting label file.")
            os.remove(label_file_path)

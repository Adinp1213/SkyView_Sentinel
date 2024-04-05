import os

folder_path = "D:/X_View_Refreshed_Project/YOLO_Format_Dataset/OG_Dataset_Backup/Labels"

# Iterate over files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".tif.txt"):
        # Build the new filename
        new_filename = os.path.join(folder_path, filename.replace(".tif.txt", ".txt"))

        # Rename the file
        os.rename(os.path.join(folder_path, filename), new_filename)
        print(f"Renamed: {filename} -> {new_filename}")

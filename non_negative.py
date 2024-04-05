import os

folder_path = "D:/X_View_Refreshed_Project/YOLO_Format_Dataset/Experiment_Dataset/Labels" # Replace with the actual path to your folder

def update_annotation_file(file_path):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Process each line and change negative values to positive
    for i in range(len(lines)):
        parts = lines[i].split()
        # Assuming the x and y coordinates are the 2nd and 3rd values in each line
        for j in range(1, 5):  # Check the 2nd to 5th values for coordinates
            coordinate = float(parts[j])
            # Change negative values to positive
            if coordinate < 0:
                parts[j] = str(0)

        # Update the line
        lines[i] = ' '.join(parts)

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.writelines(line + '\n' for line in lines)

# Recursively update annotation files in the folder
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(".txt"):
            file_path = os.path.join(root, file)
            update_annotation_file(file_path)

print("Done updating annotation files.")

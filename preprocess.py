import json
import pandas as pd
from tqdm import tqdm

# Function to convert GeoJSON to YOLO format
def geojson_to_yolo(geojson_path, output_folder, class_map_dict):
    with open(geojson_path, 'r') as infile:
        data = json.load(infile)

    feature_list = data['features']
    COLUMNS = ['IMAGE_ID', 'TYPE_ID', 'XMIN', 'YMIN', 'XMAX', 'YMAX', 'LONG', 'LAT']

    # Convert GeoJSON data to DataFrame
    data = []
    for feature in tqdm(feature_list):
        properties = feature['properties']
        img_id = properties['image_id']
        type_id = properties['type_id']
        bbox = properties['bounds_imcoords'].split(",")
        geometry = feature['geometry']
        coords = geometry['coordinates'][0]
        long = coords[0][0] / 2  + coords[2][0] / 2
        lat = coords[0][1] / 2  + coords[1][1] / 2
        one_row = [img_id, type_id, bbox[0], bbox[1], bbox[2], bbox[3], long, lat]
        data.append(one_row)

    # Create DataFrame
    df = pd.DataFrame(data, columns=COLUMNS)
    df[['XMIN', 'YMIN', 'XMAX', 'YMAX']] = df[['XMIN', 'YMIN', 'XMAX', 'YMAX']].apply(pd.to_numeric)

    # Remove specific TYPE_IDs
    df = df[(df.TYPE_ID != 75) & (df.TYPE_ID != 82)]

    # Map TYPE_ID using the provided class mapping
    df['TYPE_ID'] = df['TYPE_ID'].map(class_map_dict)

    print(df)
    # Convert DataFrame to YOLO format and save label files
    for img_id, group in df.groupby('IMAGE_ID'):
        output_file = f"{output_folder}/{img_id}.txt"
        with open(output_file, 'w') as outfile:
            for _, row in group.iterrows():
                line = f"{row['TYPE_ID']} {row['XMIN']} {row['YMIN']} {row['XMAX']} {row['YMAX']}\n"
                outfile.write(line)

if __name__ == "__main__":
    geojson_path = "D:/train_labels/xView_train.geojson"
    output_folder = "D:/train_labels/labels"
    
    # Your old-to-new class mapping
    old_to_new_mapping = {
        11: 0, 12: 1, 13: 2, 15: 3, 17: 4, 18: 5, 19: 6, 20: 7, 21: 8, 23: 9,
        24: 10, 25: 11, 26: 12, 27: 13, 28: 14, 29: 15, 32: 16, 33: 17, 34: 18, 35: 19,
        36: 20, 37: 21, 38: 22, 40: 23, 41: 24, 42: 25, 44: 26, 45: 27, 47: 28, 49: 29,
        50: 30, 51: 31, 52: 32, 53: 33, 54: 34, 55: 35, 56: 36, 57: 37, 59: 38, 60: 39,
        61: 40, 62: 41, 63: 42, 64: 43, 65: 44, 66: 45, 71: 46, 72: 47, 73: 48, 74: 49,
        76: 50, 77: 51, 79: 52, 83: 53, 84: 54, 86: 55, 89: 56, 91: 57, 93: 58, 94: 59
    }

    geojson_to_yolo(geojson_path, output_folder, old_to_new_mapping)

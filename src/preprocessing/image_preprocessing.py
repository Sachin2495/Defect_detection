import os
import pandas as pd
from PIL import Image

def check_image_validity(image_path):
    try:
        img = Image.open(image_path)
        img.verify()
        return True
    except (IOError, SyntaxError):
        return False

def preprocess_images(image_dir, defect_csv, output_csv):
    df = pd.read_csv(defect_csv)
    
    valid_images = []
    for index, row in df.iterrows():
        img_path = os.path.join(image_dir, row['ImageID'])
        if os.path.exists(img_path) and check_image_validity(img_path):
            valid_images.append(row)
    
    processed_df = pd.DataFrame(valid_images)
    processed_df.to_csv(output_csv, index=False)
    print(f"Saved cleaned dataset to {output_csv}")

# Paths
image_dir = 'traiautomated-vision-system/data/notebooks/train_images'
input_csv = 'automated-vision-system/data/notebooks/defect_and_no_defect.csv'
output_csv = 'cleaned_defect_data.csv'

preprocess_images(image_dir, input_csv, output_csv)

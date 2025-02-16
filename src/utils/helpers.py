def load_image(file_path):
    from PIL import Image
    try:
        image = Image.open(file_path)
        return image
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def save_results(results, file_path):
    import json
    try:
        with open(file_path, 'w') as f:
            json.dump(results, f)
    except Exception as e:
        print(f"Error saving results: {e}")
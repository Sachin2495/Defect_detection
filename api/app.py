from flask import Flask, request, jsonify
from PIL import Image
import io
from detection.defect_detection import load_model, predict

app = Flask(__name__)

# Load model
model = load_model('../models/defect_detection_model.pth')

@app.route('/predict', methods=['POST'])
def predict_defect():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    image = Image.open(io.BytesIO(file.read()))
    result = predict(model, image)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)

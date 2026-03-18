import json
import os
from src.vector_store import search_similar
from model.predict import predict_crop

# Load crop info JSON
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
json_path = os.path.join(BASE_DIR, "data", "crop_info.json")

with open(json_path, "r") as f:
    crop_info = json.load(f)


def generate_response(user_input_values):
    
    # 1. ML Prediction
    predicted_crop = predict_crop(user_input_values)

    # 2. Vector Search (similar conditions)
    similar_results = search_similar(user_input_values)

    # 3. Explanation from JSON
    explanation = crop_info.get(predicted_crop, "No data available")

    # 4. Format response
    response = f"""
🌱 Recommended Crop: {predicted_crop}

📊 Reason:
{explanation}

🔍 Similar Conditions Found:
"""

    for i, row in similar_results.iterrows():
        response += f"\n- Crop: {row['label']} (Temp: {row['temperature']}, Rainfall: {row['rainfall']})"

    return response
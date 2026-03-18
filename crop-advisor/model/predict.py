import pickle
import os
import numpy as np

# Get correct path to model file
BASE_DIR = os.path.dirname(__file__)
model_path = os.path.join(BASE_DIR, "crop_model.pkl")

# Load trained model once
with open(model_path, "rb") as f:
    model = pickle.load(f)


def predict_crop(input_data):
    """
    input_data: list of 7 values
    [N, P, K, temperature, humidity, ph, rainfall]
    """

    # Convert to numpy array and reshape
    input_array = np.array(input_data).reshape(1, -1)

    # Predict
    prediction = model.predict(input_array)

    return prediction[0]
import pandas as pd
import numpy as np
import os
from sklearn.metrics.pairwise import cosine_similarity

# Get correct path to dataset (no matter where you run from)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(BASE_DIR, "data", "crop_data.csv")

# Load dataset
df = pd.read_csv(file_path)

# Prepare feature vectors
def prepare_vectors():
    X = df.drop("label", axis=1)
    return X.values

# Store vectors
vectors = prepare_vectors()

# Dummy store function (for consistency with pipeline)
def store_data():
    print("✅ Data ready for vector search")

# Search similar data
def search_similar(query_input):
    query = np.array(query_input).reshape(1, -1)

    similarities = cosine_similarity(query, vectors)

    # Get top 3 similar results
    top_indices = similarities[0].argsort()[-3:][::-1]

    results = df.iloc[top_indices]

    return results[["N", "P", "K", "temperature", "humidity", "ph", "rainfall", "label"]]
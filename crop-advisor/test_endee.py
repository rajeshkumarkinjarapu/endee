from src.vector_store import store_data, search_similar

store_data()

# Example input (same format as dataset)
query = [90, 40, 40, 25, 80, 6.5, 200]

results = search_similar(query)

print("\n🔍 Similar Results:")
for i, row in results.iterrows():
    print("\n--- Result ---")
    print(f"N: {row['N']}, P: {row['P']}, K: {row['K']}")
    print(f"Temp: {row['temperature']}, Humidity: {row['humidity']}")
    print(f"pH: {row['ph']}, Rainfall: {row['rainfall']}")
    print(f"Recommended Crop: {row['label']}")
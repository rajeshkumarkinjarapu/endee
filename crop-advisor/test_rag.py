from src.rag_pipeline import generate_response

# Example input
input_data = [90, 40, 40, 25, 80, 6.5, 200]

result = generate_response(input_data)

print(result)
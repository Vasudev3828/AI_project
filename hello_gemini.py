from google import genai
from google.genai.errors import APIError

client = genai.Client()
question = input("Ask: ")

models_to_try = [
    "gemini-4-hydrogen",
    "gemini-3.5-flash-lite",
    "gemini-3.7-flash",
    "gemini-3.6-flash",
    "gemini-3.8-flash",
]

for model_name in models_to_try:
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=question,
        )
        print(f"\n[{model_name}]\n{response.text}")
        break
    except APIError as e:
        print(f"{model_name} unavailable ({e.code}), trying next...")

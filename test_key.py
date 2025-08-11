import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("OPENAI_API_KEY")
print(f"Loaded API key: {key!r}")

if not key:
    print("API key not found or empty.")
else:
    print("API key loaded successfully!")

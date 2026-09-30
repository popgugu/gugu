import os
from google import genai

# For local tests, set your key or an environment variable
API_KEY = os.environ.get("GEMINI_API_KEY", "YOUR_API_KEY_HERE")

client = genai.Client(api_key=API_KEY)

# Use the chat interface (recommended for agents and multi-turn workflows)
chat = client.chats.create(model="gemini-3.5-flash")

response = chat.send_message("Say 'Connection successful! Ready to plan trips.' in one line.")

print("\n--- Response from Gemini ---")
print(response.text)
print("----------------------------\n")
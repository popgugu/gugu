import os
from google import genai
from google.genai import types

# For local terminal use, set your key or an environment variable
API_KEY = os.environ.get("GEMINI_API_KEY", "YOUR_API_KEY_HERE")

# 1. Read system instructions from prompt.txt
with open("prompt.txt", "r", encoding="utf-8") as f:
    system_instruction_text = f.read()

# 2. Initialize Gemini Client
client = genai.Client(api_key=API_KEY)

# 3. Create chat session with instructions and low temperature for precision
chat = client.chats.create(
    model="gemini-3.5-flash",
    config=types.GenerateContentConfig(
        system_instruction=system_instruction_text,
        temperature=0.2,
    ),
)

print("=" * 60)
print("✈️ Travel Agent AI Online (Type 'exit' to quit)")
print("=" * 60)

# 4. Interactive chat loop in the console
while True:
    user_input = input("\nYou: ")
    if user_input.strip().lower() in ["exit", "quit"]:
        print("Ending session.")
        break
    if not user_input.strip():
        continue

    response = chat.send_message(user_input)
    print(f"\n{response.text}")
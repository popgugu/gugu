import os
import streamlit as st
from google import genai
from google.genai import types
from google.genai import errors

# Page setup
st.set_page_config(page_title="Travel Agent AI", page_icon="✈️", layout="centered")
st.title("✈️ Travel Agent AI")
st.caption("Star Group · CIST 205 Vacation Planner")

# Read API key safely from Streamlit Secrets
API_KEY = st.secrets.get("GEMINI_API_KEY", "")

# 1. Read system instructions from prompt.txt in the root folder
prompt_path = os.path.join(os.path.dirname(__file__), "..", "prompt.txt")
try:
    with open(prompt_path, "r", encoding="utf-8") as f:
        system_instruction_text = f.read()
except FileNotFoundError:
    system_instruction_text = "You are Travel Agent AI, an expert travel planning assistant."

# 2. Keep chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. Display existing conversation history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 4. Handle new user input
if prompt := st.chat_input("Where would you like to go or what is your budget?"):
    # Display and record user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Reconstruct the conversation history for the model
    contents = []
    for msg in st.session_state.messages:
        role = "user" if msg["role"] == "user" else "model"
        contents.append(types.Content(
            role=role,
            parts=[types.Part.from_text(text=msg["content"])]
        ))

    client = genai.Client(api_key=API_KEY)
    config = types.GenerateContentConfig(
        system_instruction=system_instruction_text,
        temperature=0.2,
    )

    with st.chat_message("assistant"):
        with st.spinner("Planning your trip..."):
            models_to_try = ["gemini-3.5-flash", "gemini-3.5-flash-lite"]
            response_text = None
            last_error = ""

            for m in models_to_try:
                try:
                    res = client.models.generate_content(
                        model=m,
                        contents=contents,
                        config=config
                    )
                    response_text = res.text
                    break
                except errors.APIError as e:
                    last_error = str(e)
                    continue

            if response_text:
                st.markdown(response_text)
                st.session_state.messages.append({"role": "assistant", "content": response_text})
            else:
                st.error(f"Could not reach Gemini. Error details: {last_error}")
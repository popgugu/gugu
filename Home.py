import streamlit as st

st.set_page_config(page_title="AI Project Hub", page_icon="🧭", layout="wide")

st.title("🧭 AI Project Hub")
st.write("Unified workspace for agent prototypes and analytical tools. Select a tool from the sidebar to launch:")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("✈️️ Travel Agent AI")
    st.write("8-stage travel planner with itinerary generation, budget tracking, and real-time mapping.")

with col2:
    st.subheader("💰 Retirement Planner")
    st.write("Milestone projection engine and asset allocation scenario modeler.")

with col3:
    st.subheader("🎮 Game Lab")
    st.write("Synergy analysis, hero drafting, and game mechanics sandbox.")
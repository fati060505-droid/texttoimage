import streamlit as st
from PIL import Image
import io


st.set_page_config(
    page_title="AI Image Generator",
    page_icon="🎨",
    layout="centered"
)


st.title("🎨 AI Image Generator")

st.write(
    "Enter a text prompt and generate an image using AI."
)


# Text input
prompt = st.text_area(
    "Enter your prompt",
    placeholder="Example: A beautiful futuristic city at night"
)


# Generate button
if st.button("Generate Image"):

    if prompt.strip() == "":
        st.warning("Please enter a prompt.")

    else:
        st.info(
            f"Your prompt is: {prompt}"
        )

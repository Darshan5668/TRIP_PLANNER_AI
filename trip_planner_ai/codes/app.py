import streamlit as st
import os
from manager import run_pipeline_from_streamlit

st.set_page_config(page_title="AI Trip Planner", layout="centered")

st.title("✈️ AI Trip Planner")
st.write("Plan trips using OCR, Vision, and AI")

# ---------- USER INPUT ----------
user_text = st.text_area(
    "📝 Describe your travel request",
    placeholder="I need a 5 day trip plan for London"
)

# ---------- OCR ----------
st.subheader("📄 Travel Document (Optional)")
ocr_enabled = st.checkbox("I have a travel document / ticket")

document_type = None
document_path = None

if ocr_enabled:
    document_type = st.selectbox(
        "Document type",
        ["ticket", "travel document", "hotel menu"]
    )

    uploaded_file = st.file_uploader(
        "Upload document image",
        type=["png", "jpg", "jpeg", "webp"]
    )

    if uploaded_file:
        document_path = f"/tmp/{uploaded_file.name}"
        with open(document_path, "wb") as f:
            f.write(uploaded_file.read())

# ---------- VISION ----------
st.subheader("🖼️ Place Image (Optional)")
vision_enabled = st.checkbox("I have an image of the place")

image_path = None
if vision_enabled:
    image = st.file_uploader(
        "Upload place image",
        type=["png", "jpg", "jpeg", "webp"]
    )
    if image:
        image_path = f"/tmp/{image.name}"
        with open(image_path, "wb") as f:
            f.write(image.read())

# ---------- RUN ----------
if st.button("🚀 Generate Trip Plan"):
    if not user_text.strip():
        st.error("Please enter a travel request.")
    else:
        with st.spinner("Planning your trip..."):
            output = run_pipeline_from_streamlit(
                user_text=user_text,
                ocr_enabled=ocr_enabled,
                document_type=document_type,
                document_path=document_path,
                vision_enabled=vision_enabled,
                image_path=image_path,
            )

        st.success("Trip plan generated!")
        st.markdown("### 🗺️ Your Trip Plan")
        st.write(output)

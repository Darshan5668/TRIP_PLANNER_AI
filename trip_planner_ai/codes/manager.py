import json
import os

from dotenv import load_dotenv
load_dotenv()  

from ocr_tool import run_ocr_chain
from vision_tool import run_vision_chain
from trip_plan_tool import run_trip_planner



def run_pipeline_from_streamlit(
    user_text,
    ocr_enabled,
    document_type=None,
    document_path=None,
    vision_enabled=False,
    image_path=None,
):
    tool_decision = {
        "ocr": ocr_enabled,
        "vision": vision_enabled,
        "trip_planner": True,
        "inputs": {
            "text": user_text,
            "document_type": document_type,
            "document_path": document_path,
            "image_path": image_path,
        },
    }

    return run_pipeline(tool_decision)



def get_tool_decision():
    user_text = input("📝 Describe your travel request: ").strip()

    # OCR decision
    has_document = input("📄 Do you have any travel documents or tickets? (yes/no): ").strip().lower()
    ocr_tool = False
    document_type = None
    document_path = None

    if has_document == "yes":
        document_type = input(
            "📂 What type of document is it? (travel document / travel ticket / hotel menu): "
        ).strip().lower()
        document_path = input("📁 Enter the document file path: ").strip()

        if os.path.exists(document_path):
            ocr_tool = True
        else:
            print("⚠️ Document not found. OCR skipped.")

    # Vision decision
    has_image = input("🖼️ Do you have any images of the place? (yes/no): ").strip().lower()
    vision_tool = False
    image_path = None

    if has_image == "yes":
        image_path = input("📁 Enter the image file path: ").strip()
        if os.path.exists(image_path):
            vision_tool = True
        else:
            print("⚠️ Image not found. Vision skipped.")

    trip_planner_tool = bool(user_text) or ocr_tool or vision_tool

    return {
        "ocr": ocr_tool,
        "vision": vision_tool,
        "trip_planner": trip_planner_tool,
        "inputs": {
            "text": user_text,
            "document_type": document_type,
            "document_path": document_path,
            "image_path": image_path
        }
    }


def run_pipeline(tool_decision):
    ocr_output = None
    vision_output = None

    print("\n🔧 PIPELINE STARTED\n")

    if tool_decision["ocr"]:
        print("🧾 OCR enabled → Running OCR chain")
        ocr_output = run_ocr_chain(
            tool_decision["inputs"]["document_path"],
            tool_decision["inputs"]["document_type"]
        )

    if tool_decision["vision"]:
        print("🖼️ Vision enabled → Running Vision chain")
        vision_output = run_vision_chain(
            tool_decision["inputs"]["image_path"]
        )

    print("✈️ Running Trip Planner\n")

    final_output = run_trip_planner(
        user_text=tool_decision["inputs"]["text"],
        ocr_data=ocr_output,
        vision_data=vision_output
    )

    return final_output   # 🔥 THIS LINE IS THE KEY


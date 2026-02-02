from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq


def run_trip_planner(user_text, ocr_data=None, vision_data=None):
    prompt = PromptTemplate.from_template(
        """
You are an expert travel planner.

User request:
{user_text}

OCR data:
{ocr_data}

Vision data:
{vision_data}

Create a detailed day-by-day itinerary.
"""
    )

    llm = ChatGroq(model="llama-3.1-8b-instant")

    chain = prompt | llm

    result = chain.invoke(
        {
            "user_text": user_text,
            "ocr_data": ocr_data or "None",
            "vision_data": vision_data or "None",
        }
    )

    return result.content

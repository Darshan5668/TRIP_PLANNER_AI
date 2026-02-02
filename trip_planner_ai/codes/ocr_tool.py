import json
import pytesseract
from PIL import Image

from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq


def run_ocr_chain(document_path, document_type):
    raw_text = pytesseract.image_to_string(Image.open(document_path))

    prompt = PromptTemplate.from_template(
        """
Extract important structured travel information from the OCR text.
Return ONLY valid JSON.

OCR Text:
{ocr_text}

JSON format:
{{
  "document_type": "{document_type}",
  "dates": [],
  "locations": [],
  "summary": ""
}}
"""
    )

    llm = ChatGroq(model="llama-3.1-8b-instant")

    chain = prompt | llm

    result = chain.invoke(
        {
            "ocr_text": raw_text,
            "document_type": document_type
        }
    )

    output = result.content

    with open("ocr_output.json", "w") as f:
        f.write(output)

    return json.loads(output)

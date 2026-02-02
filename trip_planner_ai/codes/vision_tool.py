import json
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

MODEL = "llama-3.1-8b-instant"

def run_vision_chain(image_path):
    prompt = PromptTemplate.from_template(
        """
You are a vision reasoning model.

Based on the image path, infer the city and landmarks.
Return ONLY valid JSON.

Image path:
{image_path}

JSON format:
{{
  "city": "",
  "landmarks": [],
  "notes": ""
}}
"""
    )

    llm = ChatGroq(model=MODEL)

    chain = prompt | llm

    result = chain.invoke({"image_path": image_path})

    output = result.content

    with open("vision_output.json", "w") as f:
        f.write(output)

    return json.loads(output)

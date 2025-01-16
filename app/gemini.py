import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content

def configure_gemini(api_key):
    genai.configure(api_key=api_key)
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_schema": content.Schema(
            type=content.Type.OBJECT,
            required=["note", "category", "amount"],
            properties={
                "note": content.Schema(type=content.Type.STRING),
                "category": content.Schema(type=content.Type.STRING),
                "amount": content.Schema(type=content.Type.NUMBER),
            },
        ),
        "response_mime_type": "application/json",
    }
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )
    return model

def upload_to_gemini(path, mime_type=None):
    return genai.upload_file(path, mime_type=mime_type)

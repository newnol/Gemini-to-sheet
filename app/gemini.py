import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content

def upload_to_gemini(path, mime_type=None):
  """Uploads the given file to Gemini.

  See https://ai.google.dev/gemini-api/docs/prompting_with_media
  """
  file = genai.upload_file(path, mime_type=mime_type)
  print(f"Uploaded file '{file.display_name}' as: {file.uri}")
  return file

def configure_gemini(api_key, mode="chat"):
    genai.configure(api_key=api_key)

    if mode == "chat":
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
    elif mode == "analysis":
        generation_config = {
            "temperature": 1,        # Giảm sáng tạo, tăng tính logic
            "top_p": 0.85,
            "top_k": 50,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",  # Trả về văn bản thường
        }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    return model

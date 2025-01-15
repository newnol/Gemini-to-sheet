import requests
import os
from dotenv import load_dotenv
import google.generativeai as genai
import json
import base64
from google.ai.generativelanguage_v1beta.types import content

# Đọc ảnh và chuyển sang base64
def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_string

def upload_to_gemini(path, mime_type=None):
  """Uploads the given file to Gemini.

  See https://ai.google.dev/gemini-api/docs/prompting_with_media
  """
  file = genai.upload_file(path, mime_type=mime_type)
  print(f"Uploaded file '{file.display_name}' as: {file.uri}")
  return file

# Load environment variables
load_dotenv('key.env')

# Thêm id của Google Sheets vào dữ liệu
SHEET_ID = os.getenv('SHEET_ID')

# Cấu hình API key cho Gemini
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# Tạo mô hình với cấu hình
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_schema": content.Schema(
    type = content.Type.OBJECT,
    enum = [],
    required = ["note", "category", "amount"],
    properties = {
      "note": content.Schema(
        type = content.Type.STRING,
      ),
      "category": content.Schema(
        type = content.Type.STRING,
      ),
      "amount": content.Schema(
        type = content.Type.NUMBER,
      ),
    },
  ),
  "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Tạo session chat với dữ liệu mẫu
chat_session = model.start_chat(
    history=[
        {"role": "user", "parts": ["nay tôi đổ xăng 10k\n"]},
        {"role": "model", "parts": ["{\"amount\": 10000, \"category\": \"gas\", \"note\": \"refuel\"}"]},
        {"role": "user", "parts": ["nay ăn sáng 5k\n"]},
        {"role": "model", "parts": ["{\"amount\": 5000, \"category\": \"breakfast\", \"note\": \"morning meal\"}"]},
        {"role": "user", "parts": ["uống trà đá vỉa hè 80k\n"]},
        {"role": "model", "parts": ["{\"amount\": 80000, \"category\": \"drinks\", \"note\": \"street tea\"}"]},
    ]
)

files = [
  upload_to_gemini("test.jpg", mime_type="image/jpg"),
]


image_path = "test.jpg"

# Gửi câu hỏi mới để lấy dữ liệu chi tiêu
encoded_image = encode_image_to_base64(image_path)
response = chat_session.send_message(files[0])


# In kết quả phản hồi từ Gemini
print("Phản hồi từ Gemini:", response.text)

# Xử lý dữ liệu JSON trả về
try:
    # Loại bỏ ký tự không cần thiết nếu có
    json_str = response.text.strip("```").strip()
    data = json.loads(json_str)
    data['SHEET_ID'] = SHEET_ID
    print("Dữ liệu JSON:", data)
except json.JSONDecodeError:
    print("Lỗi: Phản hồi không đúng định dạng JSON.")
    data = None

# Gửi dữ liệu lên Google Sheets qua Google Apps Script nếu dữ liệu hợp lệ
if data:
    url = 'https://script.google.com/macros/s/AKfycbzrmQAPgc1BOlX4544KOHQ_shRn4SGYECXR-_6LObZe-NXtHnJ0AELn-Eag_guYTDsacg/exec'
    
    try:
        responseData = requests.post(url, json=data)
        if responseData.status_code == 200:
            print("Dữ liệu đã được gửi thành công:", responseData.text)
        else:
            print("Lỗi khi gửi dữ liệu:", responseData.status_code, responseData.text)
    except requests.RequestException as e:
        print("Lỗi kết nối:", e)
else:
    print("Không có dữ liệu hợp lệ để gửi.")

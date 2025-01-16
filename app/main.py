import json
from config import SHEET_ID, GEMINI_API_KEY
from gemini import configure_gemini, upload_to_gemini
from google_sheets import send_to_google_sheets
from gui import setup_gui
import tkinter as tk
from tkinter import filedialog, messagebox
import os

model = configure_gemini(GEMINI_API_KEY)
chat_session = model.start_chat(
    history=[
        {"role": "user", "parts": ["nay tôi đổ xăng 10k\n"]},
        {"role": "model", "parts": ["{\"amount\": 10000, \"category\": \"gas\", \"note\": \"refuel\"}"]},
        # Add more history if necessary
    ]
)

def process_message():
    user_msg = entry.get()
    display_area.insert(tk.END, f"You: {user_msg}\n")
    entry.delete(0, tk.END)

    response = chat_session.send_message(user_msg)
    try:
        data = json.loads(response.text.strip("`"))
        display_area.insert(tk.END, f"Bot: {data}\n")
        send_to_google_sheets(data, SHEET_ID)
    except json.JSONDecodeError:
        display_area.insert(tk.END, "Bot: Invalid JSON response.\n")

def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
    if file_path:
        ext = os.path.splitext(file_path)[1]
        file = upload_to_gemini(file_path, mime_type=f"image/{ext[1:]}")
        response = chat_session.send_message(file)
        try:
            data = json.loads(response.text.strip(""))
            display_area.insert(tk.END, f"Bot (Image): {data}\n")
            send_to_google_sheets(data, SHEET_ID)
        except json.JSONDecodeError:
            display_area.insert(tk.END, "Bot: Invalid JSON response from image.\n")

# Initialize GUI
root, display_area, entry = setup_gui(process_message, upload_image)
root.mainloop()

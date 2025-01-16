import tkinter as tk
import json
import threading
from config import SHEET_ID, GEMINI_API_KEY
from gemini import configure_gemini
from google_sheets import get_sheet_data, send_to_google_sheets
from gui import setup_gui

# ⚡ Mặc định là chế độ chat
model = configure_gemini(GEMINI_API_KEY, mode="chat")
chat_session = model.start_chat(history=[])

def show_spinner(message="🔄 Đang xử lý..."):
    spinner_label.config(text=message)
    spinner_label.update()

def hide_spinner():
    spinner_label.config(text="")
    spinner_label.update()

def process_message():
    user_msg = entry.get().strip()
    if not user_msg:
        return

    display_area.configure(state='normal')
    display_area.insert(tk.END, f"🧑‍💻 Bạn: {user_msg}\n")
    display_area.configure(state='disabled')
    entry.delete(0, tk.END)

    threading.Thread(target=bot_response, args=(user_msg,)).start()

def bot_response(user_msg):
    show_spinner("🤖 Đang trả lời...")
    response = chat_session.send_message(user_msg)
    try:
        data = json.loads(response.text.strip("`"))
        hide_spinner()
        display_area.configure(state='normal')
        display_area.insert(tk.END, f"🤖 Bot: {data}\n")
        display_area.configure(state='disabled')
        send_to_google_sheets(data, SHEET_ID)
    except json.JSONDecodeError:
        hide_spinner()
        display_area.insert(tk.END, "🤖 Bot: Lỗi dữ liệu.\n")

def analyze_data():
    global model, chat_session

    # 🔄 Chuyển sang chế độ phân tích
    model = configure_gemini(GEMINI_API_KEY, mode="analysis")
    chat_session = model.start_chat(history=[])

    show_spinner("📊 Đang phân tích dữ liệu...")
    threading.Thread(target=analyze_data_thread).start()

def analyze_data_thread():
    data = get_sheet_data(SHEET_ID)
    if data:
        # Gửi dữ liệu cho Gemini phân tích
        prompt = f"Phân tích dữ liệu chi tiêu sau và đưa ra nhận xét chi tiết:\n{json.dumps(data, indent=2)}"
        response = chat_session.send_message(prompt)
        hide_spinner()
        display_area.configure(state='normal')
        display_area.insert(tk.END, f"📊 Kết quả phân tích:\n{response.text}\n")
        display_area.configure(state='disabled')
    else:
        hide_spinner()
        display_area.insert(tk.END, "❌ Không lấy được dữ liệu từ Google Sheets.\n")

# 🚀 Khởi động GUI
root, display_area, entry, spinner_label = setup_gui(process_message, None, analyze_data)
root.mainloop()

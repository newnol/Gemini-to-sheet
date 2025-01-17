import json
import threading
from datetime import datetime
from tkinter import filedialog, messagebox
import customtkinter as ctk
from config import SHEET_ID, GEMINI_API_KEY
from gemini import configure_gemini 
from google_sheets import get_sheet_data, send_to_google_sheets
from gui import setup_gui

# Cấu hình Gemini mặc định
model = configure_gemini(GEMINI_API_KEY, mode="chat")
chat_session = model.start_chat(history=[])

def show_spinner(message="🔄 Đang xử lý..."):
    spinner_label.configure(text=message)
    spinner_label.update()

def hide_spinner():
    spinner_label.configure(text="")
    spinner_label.update()

def send_bot_message(message):
    display_area.configure(state='normal')
    display_area.insert("end", f"🤖 Bot: {message}\n\n")
    display_area.configure(state='disabled')

def process_message():
    user_msg = entry.get().strip()
    if not user_msg:
        send_bot_message("⚠️ Bạn chưa nhập nội dung.")
        return

    display_area.configure(state='normal')
    display_area.insert("end", f"🧑‍💻 Bạn: {user_msg}\n\n")
    display_area.configure(state='disabled')
    entry.delete(0, "end")

    threading.Thread(target=bot_response, args=(user_msg,)).start()

def bot_response(user_msg):
    show_spinner("🤖 Đang trả lời...")
    response = chat_session.send_message(user_msg)
    try:
        data = json.loads(response.text.strip("`"))
        hide_spinner()
        send_bot_message(f"{data}")
        send_to_google_sheets(data, SHEET_ID)
        send_bot_message("✅ Dữ liệu đã được lưu vào Google Sheets.")
    except json.JSONDecodeError:
        hide_spinner()
        send_bot_message("❌ Bot không hiểu yêu cầu của bạn. Vui lòng thử lại.")

def analyze_data():
    show_spinner("📊 Đang phân tích dữ liệu...")
    threading.Thread(target=analyze_data_thread).start()

def analyze_data_thread():
    data = get_sheet_data(SHEET_ID)
    if data:
        response = chat_session.send_message(f"Phân tích dữ liệu sau:\n{json.dumps(data)}")
        hide_spinner()
        send_bot_message(f"📊 Kết quả phân tích:\n{response.text}")
    else:
        hide_spinner()
        send_bot_message("❌ Không lấy được dữ liệu từ Google Sheets.")
def upload_image():
    """Handle image upload and processing"""
    try:
        file_path = filedialog.askopenfilename(
            title="Chọn ảnh",
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.webp")
            ]
        )
        
        if not file_path:
            return
        
        file = file_path.split("/")[-1]

        show_spinner("📤 Đang tải ảnh lên...")
        image_button.configure(text=f"📸 Ảnh: {file_path.split('/')[-1]}")
        
        # TODO: Add image processing logic here
        hide_spinner()
        send_bot_message(f"✅ Đã chọn ảnh: {file[0]}")
        
    except Exception as e:
        hide_spinner()
        send_bot_message(f"❌ Lỗi khi tải ảnh: {str(e)}")
        image_button.configure(text="📸 Chọn ảnh")


# Update main section to include image_button
if __name__ == "__main__":
    root, display_area_widget, entry_widget, spinner_label_widget, image_btn = setup_gui(
        process_message=process_message,
        upload_image=upload_image, 
        analyze_data=analyze_data
    )
    
    display_area = display_area_widget
    entry = entry_widget
    spinner_label = spinner_label_widget
    image_button = image_btn
    
    root.mainloop()
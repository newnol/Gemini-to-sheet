import customtkinter as ctk
from tkinter import filedialog, scrolledtext
from tkhtmlview import HTMLLabel  # Thư viện hỗ trợ Markdown
import markdown

def setup_gui(process_message, upload_image, analyze_data):
    ctk.set_appearance_mode("Light")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("💸 Expense Tracker with Gemini AI")
    root.geometry("900x700")

    # Header
    header = ctk.CTkLabel(root, text="Expense Tracker 💰", font=("Helvetica", 26, "bold"))
    header.pack(pady=20)

    # Khu vực hiển thị chat (Khung chat với Markdown)
    chat_frame = ctk.CTkFrame(root)
    chat_frame.pack(pady=10)

    display_area = scrolledtext.ScrolledText(chat_frame, width=100, height=25, font=("Helvetica", 12), state='disabled')
    display_area.pack(pady=10)

    # Create image button
    image_button = ctk.CTkButton(root, text="📷 Tải Ảnh", width=150, command=upload_image)
    image_button.pack(pady=5)
    
    # Create analyze button
    analyze_button = ctk.CTkButton(root, text="📊 Phân Tích Dữ Liệu", width=150, command=analyze_data)
    analyze_button.pack(pady=5)

    # Khung nhập liệu
    entry_frame = ctk.CTkFrame(root)
    entry_frame.pack(pady=10)

    entry = ctk.CTkEntry(entry_frame, width=600, font=("Helvetica", 12))
    entry.pack(side="left", padx=10, pady=10)

    send_button = ctk.CTkButton(entry_frame, text="📨 Gửi", width=80, command=process_message)
    send_button.pack(side="left", padx=5)

    

    spinner_label = ctk.CTkLabel(root, text="", font=("Helvetica", 10))
    spinner_label.pack(pady=5)

    def enter_pressed(event):
        process_message()

    entry.bind("<Return>", enter_pressed)

    return root, display_area, entry, spinner_label, image_button
    
def send_markdown_message(display_area, markdown_text):
    html_content = markdown.markdown(markdown_text)
    display_area.configure(state='normal')
    display_area.insert('end', html_content + "\n\n")
    display_area.configure(state='disabled')
    display_area.yview('end')

# Ví dụ sử dụng:
# send_markdown_message(display_area, "## 📊 Kết quả phân tích\n- **Chi tiêu ăn uống:** 60%\n- **Di chuyển:** 25%\n- **Mua sắm:** 15%")

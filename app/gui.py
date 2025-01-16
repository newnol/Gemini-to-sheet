import customtkinter as ctk
from tkinter import filedialog

def setup_gui(process_message, upload_image, analyze_data):
    ctk.set_appearance_mode("Light")  # Light / Dark / System
    ctk.set_default_color_theme("blue")  # green, dark-blue, blue

    root = ctk.CTk()
    root.title("💸 Expense Tracker with Gemini AI")
    root.geometry("900x700")  # 📏 Mở rộng chiều ngang

    # Header
    header = ctk.CTkLabel(root, text="Expense Tracker 💰", font=("Helvetica", 26, "bold"))
    header.pack(pady=20)

    # Khu vực hiển thị chat (Mở rộng ngang)
    display_area = ctk.CTkTextbox(root, width=850, height=450, font=("Helvetica", 12))
    display_area.pack(pady=10)
    display_area.configure(state='disabled')

    # Khung nhập liệu
    entry_frame = ctk.CTkFrame(root)
    entry_frame.pack(pady=10)

    entry = ctk.CTkEntry(entry_frame, width=600, font=("Helvetica", 12))
    entry.pack(side="left", padx=10, pady=10)

    send_button = ctk.CTkButton(entry_frame, text="📨 Gửi", width=80, command=process_message)
    send_button.pack(side="left", padx=5)

    upload_button = ctk.CTkButton(root, text="📷 Tải Ảnh", width=150, command=upload_image)
    upload_button.pack(pady=5)

    analyze_button = ctk.CTkButton(root, text="📊 Phân Tích Dữ Liệu", width=150, command=analyze_data)
    analyze_button.pack(pady=5)

    spinner_label = ctk.CTkLabel(root, text="", font=("Helvetica", 10))
    spinner_label.pack(pady=5)

    # Nhấn Enter để gửi
    def enter_pressed(event):
        process_message()

    entry.bind("<Return>", enter_pressed)

    return root, display_area, entry, spinner_label

import tkinter as tk
from tkinter import scrolledtext, filedialog

def setup_gui(process_message, upload_image, analyze_data):
    root = tk.Tk()
    root.title("💸 Expense Tracker with Gemini AI")
    root.geometry("500x650")
    root.configure(bg="#f0f0f0")

    header = tk.Label(root, text="Expense Tracker 💰", font=("Helvetica", 18, "bold"), bg="#4CAF50", fg="white", pady=10)
    header.pack(fill=tk.X)

    display_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=25, font=("Helvetica", 10))
    display_area.pack(padx=10, pady=10)
    display_area.configure(state='disabled')

    entry_frame = tk.Frame(root, bg="#f0f0f0")
    entry_frame.pack(padx=10, pady=5, fill=tk.X)

    entry = tk.Entry(entry_frame, width=40, font=("Helvetica", 12))
    entry.pack(side=tk.LEFT, padx=(0, 10), fill=tk.X, expand=True)

    send_button = tk.Button(entry_frame, text="📨 Gửi", width=8, bg="#4CAF50", fg="white", command=process_message)
    send_button.pack(side=tk.LEFT)

    analyze_button = tk.Button(root, text="📊 Phân Tích Dữ Liệu", width=20, bg="#FF9800", fg="white", command=analyze_data)
    analyze_button.pack(pady=5)

    spinner_label = tk.Label(root, text="", font=("Helvetica", 10, "italic"), fg="gray", bg="#f0f0f0")
    spinner_label.pack()

    def enter_pressed(event):
        process_message()

    entry.bind("<Return>", enter_pressed)

    return root, display_area, entry, spinner_label

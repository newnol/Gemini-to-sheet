import tkinter as tk
from tkinter import scrolledtext, filedialog
import json

def setup_gui(process_message, upload_image):
    root = tk.Tk()
    root.title("Expense Tracker with Gemini")

    display_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
    display_area.pack(padx=10, pady=10)

    entry_frame = tk.Frame(root)
    entry_frame.pack(padx=10, pady=5)

    entry = tk.Entry(entry_frame, width=45)
    entry.grid(row=0, column=0, padx=5)

    send_button = tk.Button(entry_frame, text="Send", command=process_message)
    send_button.grid(row=0, column=1, padx=5)

    upload_button = tk.Button(root, text="Upload Image", command=upload_image)
    upload_button.pack(pady=5)

    return root, display_area, entry

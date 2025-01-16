
---

# 📊 Expense Tracker with Gemini

### Ứng dụng ghi chép chi tiêu cá nhân thông minh tích hợp **Gemini AI** và **Google Sheets**.

---

## 🌟 Tính Năng

✅ **Ghi chép chi tiêu nhanh chóng** bằng văn bản hoặc hình ảnh.  
✅ **Phân loại tự động** các khoản chi tiêu (ăn uống, xăng xe, mua sắm, v.v.).  
✅ **Lưu trữ dữ liệu an toàn** trên **Google Sheets**.  
✅ **Giao diện trực quan** với **Tkinter**.  


## 🛠 Công Nghệ Sử Dụng

- **Python 3.x** 🐍  
- **Tkinter** – Tạo giao diện người dùng.  
- **Google Generative AI (Gemini API)** – Xử lý dữ liệu đầu vào.  
- **Google Sheets API** – Lưu trữ dữ liệu.  
- **Requests** – Gửi dữ liệu qua API.  
- **Python-dotenv** – Quản lý biến môi trường.  

---

## 🚀 Hướng Dẫn Cài Đặt

### 1️⃣ Clone Project

```bash
git clone https://github.com/newnol/gemini-to-sheet.git
cd gemini-to-sheet
```

### 2️⃣ Tạo Môi Trường Ảo

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ Cài Đặt Thư Viện

```bash
pip install -r requirements.txt
```

### 4️⃣ Thiết Lập Biến Môi Trường

Tạo file `.env`:

```env
GEMINI_API_KEY=your_gemini_api_key
SHEET_ID=your_google_sheet_id
```

### 5️⃣ Chạy Ứng Dụng

```bash
python app/main.py
```

---

## 🎮 Cách Sử Dụng

1. **Nhập nội dung chi tiêu** vào ô văn bản.  
   _Ví dụ:_ `Nay ăn sáng 25k`  
2. **Nhấn "Send"** để gửi.  
3. **Nhấn "Upload Image"** để tải ảnh hóa đơn hoặc ảnh liên quan.  
4. Dữ liệu sẽ **phân loại và lưu vào Google Sheets**.

---

## 📂 Cấu Trúc Dự Án

```
expense_tracker/
├── app/
│   ├── config.py          # Quản lý biến môi trường
│   ├── gemini.py          # Tích hợp API Gemini
│   ├── google_sheets.py   # Gửi dữ liệu lên Google Sheets
│   ├── gui.py             # Giao diện Tkinter
│   └── main.py            # Điểm khởi động ứng dụng
│
├── tests/                 # Thư mục kiểm thử
│   ├── test_gemini.py
│   └── test_google_sheets.py
│
├── .env                   # Biến môi trường (KHÔNG commit)
├── .gitignore             # File/thư mục không đẩy lên Git
├── README.md              # File mô tả dự án
└── requirements.txt       # Danh sách thư viện cần cài
```

---

## ❓ Câu Hỏi Thường Gặp

### 1. **Làm sao để lấy API Key của Gemini?**  
- Đăng ký tại [Google Cloud Console](https://console.cloud.google.com/).  
- Tạo API Key và dán vào file `.env`.

### 2. **Dữ liệu lưu ở đâu?**  
- Dữ liệu được lưu trực tiếp lên **Google Sheets** theo `SHEET_ID`.

### 3. **Có hỗ trợ đa ngôn ngữ không?**  
- Hiện tại ứng dụng hỗ trợ **Tiếng Việt**. Có thể mở rộng thêm ngôn ngữ khác.

---

## 📈 Kế Hoạch Phát Triển

- [ ] **Báo cáo thống kê chi tiêu hàng tuần/tháng**.  
- [ ] **Tích hợp chatbot trực tuyến**.  
- [ ] **Phiên bản di động (Android/iOS)**.  

---

## 🤝 Đóng Góp

1. Fork repository.  
2. Tạo nhánh mới: `git checkout -b feature-name`.  
3. Commit thay đổi: `git commit -m "Add feature"`.  
4. Push nhánh: `git push origin feature-name`.  
5. Tạo **Pull Request**.

---

## 💼 Tác Giả

- **👤 Tên:** [Your Name]  
- **🌐 Website:** [newnol.io.com](https://newnol.io.vn)  
- **📧 Email:** tantai@newnol.io.vn  

---

## 📜 Giấy Phép

Dự án được cấp phép theo [MIT License](LICENSE).

---

## ⭐️ Nếu Thấy Hay, Hãy Ủng Hộ Dự Án!

```bash
⭐️ Star • 🍴 Fork • 🐞 Report Issue
```

---

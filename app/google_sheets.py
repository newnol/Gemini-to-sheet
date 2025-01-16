import requests
from tkinter import messagebox

def send_to_google_sheets(data, sheet_id):
    url = 'https://script.google.com/macros/s/AKfycbwrnLikw6-OvK4mj7VCPqukDuiPK3ucZPQNtYYDkm2XoaSeo0g9FLhJaco3Ajuy_qn2Gg/exec'
    data['SHEET_ID'] = sheet_id
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            messagebox.showinfo("Success", "Data sent successfully!")
        else:
            messagebox.showerror("Error", f"Failed to send data: {response.text}")
    except requests.RequestException as e:
        messagebox.showerror("Connection Error", str(e))
        
def get_sheet_data(sheet_id, gid=0):
    url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}'
    response = requests.get(url)
    if response.status_code == 200:
        f = StringIO(response.text)
        reader = csv.DictReader(f)
        data = list(reader)
        return data
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return None
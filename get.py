import os
import requests
import csv
import json
from io import StringIO

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

# Example usage
SHEET_ID = '1DQ38MOhoeAVbU0IMRcjooihYjiWlSCNcoL2jOcgCWdw'
sheet_data = get_sheet_data(SHEET_ID)
print("Dữ liệu từ Google Sheets:", sheet_data)

    # Ghi dữ liệu vào file JSON
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(sheet_data, f, ensure_ascii=False, indent=4)
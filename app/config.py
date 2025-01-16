import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv('key.env')

SHEET_ID = os.getenv('SHEET_ID')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

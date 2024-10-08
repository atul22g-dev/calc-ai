from dotenv import load_dotenv
import os
load_dotenv()

ENV = os.getenv("ENV", "dev")

if ENV == 'production':
    SERVER_URL = '0.0.0.0'
    PORT = '8900'
else:
    SERVER_URL = 'localhost'
    PORT = '8900'

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
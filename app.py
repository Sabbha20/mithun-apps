from dotenv import load_dotenv
from taipy.gui import Gui

import os
import google.generativeai as genai

# Load env variables
load_dotenv()
# Set up API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# Initializing our model
model = genai.GenerativeModel("gemini-pro")


# Defining function for our response
def get_gemini_response(query):
    resp = model.generate_content(query)
    return resp.text

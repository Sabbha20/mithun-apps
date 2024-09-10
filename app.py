from dotenv import load_dotenv
from taipy.gui import Gui, notify #, State

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

# Function to handle user input and update the response
def btn_submit(state):
    state.response = get_gemini_response(state.query)
    notify(state, "success", "Response generated!")

# Our Taipy gui
page = """
# Gemini LLM Application

Enter your prompt:
<|{query}|input|>

<|Submit|button|on_action=btn_submit|>

Response:
<|{response}|>


"""

# def on_init(state: State):
#     state.query = ""
#     state.response = ""

if __name__ == "__main__":
    query = ""
    response = ""
    Gui(page).run(debug=True, port=8000, title="Q&A App")



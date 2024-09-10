from dotenv import load_dotenv
from taipy.gui import Gui, notify, Html , State

import markdown
from markupsafe import Markup

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
    try:
        resp = model.generate_content(query)
        return resp.text
    except Exception as e:
        print(f"Error in get_gemini_response: {e}")
        return f"An error occurred: {str(e)}"

# Function to handle user input and update the response
def btn_submit(state):
    print("Button clicked!")  # Debug print
    print(f"Query: {state.query}")  # Debug print
    response = get_gemini_response(state.query)
    print(f"Response: {response}")  # Debug print
    
    # Convert Markdown to HTML
    html_response = markdown.markdown(response)
    
    # Use Markup to mark the HTML as safe
    state.response = Markup(html_response)
    
    state.debug_response = f"Debug: {response[:100]}..."  # Add a debug response
    notify(state, "success", "Response generated!")


# Our Taipy gui
page = """
<|container|
<|part|class_name=card mt-5 p-4|
# Gemini LLM Application

<|{query}|input|class_name=form-control mb-3|label=Enter your prompt here...|>


<|Submit|button|on_action=btn_submit|class_name=btn btn-primary mb-3|>

<|part|class_name=card mt-3 p-3|
### Response:

<|{response}|>

|>
|>
|>
"""

# ### Debug Response:
# <|{debug_response}|>

# ### Query Echo:
# <|{query}|>
if __name__ == "__main__":
    query = ""
    response = ""
    debug_response = "Debug: Initial debug response"
    gui = Gui(page)
    gui.run(debug=True, port=5002, title="Q&A App", use_reloader=True)



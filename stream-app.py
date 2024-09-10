from dotenv import load_dotenv

import streamlit as st
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


# Streamlit app begin
st.set_page_config(page_title="Q&A App")
st.title("Gemini AI Model")

input = st.text_input("Input :", key="input")
submit = st.button("Ask the question")

if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)


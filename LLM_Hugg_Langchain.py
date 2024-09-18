from dotenv import load_dotenv

import streamlit as st
import os
from langchain_google_genai import ChatGoogleGenerativeAI


# Load env variables
load_dotenv()

#Function to return the response
def load_answer(question):
    llm = ChatGoogleGenerativeAI(model="gemini-pro")

    answer=llm.invoke(question)
    return answer.content


#App UI starts here
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("LangChain Demo")


#Gets the user input
def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text


user_input=get_text()
response = load_answer(user_input)

submit = st.button('Generate')  

#If generate button is clicked
if submit:

    st.subheader("Answer:")

    st.write(response)

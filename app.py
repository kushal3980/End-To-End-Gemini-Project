from dotenv import load_dotenv
load_dotenv() ### loading env variable

import streamlit as st
import os 
import google.generativeai as genai

genai.configure(api_key="AIzaSyB7EoZgkQycREL3fCXXXXXX")

# function to load gemini pro model and get response
model=genai.GenerativeModel('gemini-1.5-flash')
# model=genai.GenerativeModel('gemini-pro')

def get_gimini_response(question):
    response=model.generate_content(question)
    return response.text


# initializing the streamlit app

st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application by Kushal")
input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

# when the submit is clicked
if submit:
    response=get_gimini_response(input)
    st.subheader("the response is")
    st.write(response)

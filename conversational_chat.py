# from dotenv import load_dotenv
# load_dotenv()

# import streamlit as st
# import os
# import google.generativeai as genai

# genai.configure(api_key="AIzaSyB7EoZgkQycREL3fCZ6jSf3oA8EEFaTgzE")

# # function to load gemini pro model 
# model=genai.GenerativeModel('gemini-1.5-flash')
# chat=model.start_chat(history=[])

# def get_gimini_response(question):
#     response=chat.send_message(question,stream=True)
#     return response

# # initializing the streamlit app
# st.set_page_config(page_title="Q&A Demo")
# st.header("Gemini LLM Application")

# # Initialize session state for chat history if it doesn't exist
# if 'chat_history' not in st.session_state:
#     st.session_state['chat_history'] = []

# input=st.text_input("Input: ",key="input")
# submit=st.button("Ask the question")

# if submit and input:
#     response=get_gimini_response(input)
#     #add user query and response to session chat history
#     st.session_state['chat_history'].append(("You",input))
#     st.subheader("The Response is")
#     for chunk in response:
#         st.write(chunk.text)
#         st.session_state['chat_history'].append(("Bot", chunk.text))
# st.subheader("The Chat History is")
    
# for role, text in st.session_state['chat_history']:
#     st.write(f"{role}: {text}")
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

# Configure the API key from environment variables
api_key = "AIzaSyB7EoZgkQycREL3fCZ6jSf3oA8EEFaTgzE"
if not api_key:
    st.error("API key not found. Please set the GOOGLE_API_KEY environment variable.")
else:
    genai.configure(api_key=api_key)

    # Function to load the gemini pro model
    model = genai.GenerativeModel('gemini-1.5-flash')
    chat = model.start_chat(history=[])

    def get_gimini_response(question):
        response = chat.send_message(question, stream=True)
        return response

    # Initializing the Streamlit app
    st.set_page_config(page_title="Q&A Demo", layout="wide")
    st.markdown(
        """
        <style>
        .main {
            background-color: black;
        }
        .stTextInput input {
            width: 100%;
            padding: 10px;
            box-sizing: border-box;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 24px;
            border: none;
            cursor: pointer;
        }
        .stMarkdown p {
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 10px;
        }
        .stMarkdown p.user {
            background-color: blue;
            text-align: right;
        }
        .stMarkdown p.bot {
            background-color: darkblue;
            text-align: left;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("Gemini LLM Application")

    # Initialize session state for chat history if it doesn't exist
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    with st.sidebar:
        st.subheader("Ask a Question")
        input = st.text_input("Input: ", key="input")
        submit = st.button("Ask the question")

    if submit and input:
        with st.spinner("Getting response..."):
            try:
                response = get_gimini_response(input)
                st.session_state['chat_history'].append(("You", input))
                for chunk in response:
                    st.session_state['chat_history'].append(("Bot", chunk.text))
            except Exception as e:
                st.error(f"Error: {e}")

    st.subheader("Chat History")
    for role, text in st.session_state['chat_history']:
        if role == "You":
            st.markdown(f"<p class='user'><b>{role}:</b> {text}</p>", unsafe_allow_html=True)
        else:
            st.markdown(f"<p class='bot'><b>{role}:</b> {text}</p>", unsafe_allow_html=True)



import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai

##streamlit framework

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##Function
model=genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])

def get_gemini_response(question):
    response=chat.send_message(question,stream=True)
    return response

##initialize streamlit app
st.set_page_config(page_title="Chat Bot")

st.header("Gemini LLM Application")

##Intialize session state for chat history if it doesn't exist

if'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]

input=st.text_input("Input:",key="input")
submit=st.button("Ask the question")

if submit and input:
    response=get_gemini_response(input)
    ##add user query and response to session chat history
    st.session_state['chat_history'].append(("You",input))
    st.subheader("Result:")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot",chunk.text))
st.subheader("History")

for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")
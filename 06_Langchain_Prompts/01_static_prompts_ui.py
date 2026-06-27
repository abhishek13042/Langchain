from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


import streamlit as st
load_dotenv()
model=ChatOpenAI(model="")
#This is a static promtps for us 
st.header("Research Tool")
user_input=st.text_input("Enter your prompt")

if st.button("Summarize"):
    result= model.invoke(user_input)
    st.write("Some random text") 

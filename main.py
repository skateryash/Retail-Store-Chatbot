import streamlit as st
from langchain_helper import get_few_shot_db_chain

st.title("Yash Collection T Shirts: Database Q&A 👕")

question = st.text_input("Question: ")

if question:
    chain = get_few_shot_db_chain()
    response = chain.invoke(question)

    st.header("Answer")
    st.write(response['result'])

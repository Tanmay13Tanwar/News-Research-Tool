import streamlit as st
from helper import process

st.title("News Research Tool 📈")
st.sidebar.title("News Article URL")

url = st.sidebar.text_input("URL")

#process_url_clicked = st.sidebar.button("Process URL")

main_placeholder = st.empty()
query = main_placeholder.text_input("Question: ")
if query:

    result = process(url,query)
    st.header("Answer")
    st.write(result)    

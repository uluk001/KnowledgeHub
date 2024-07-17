import streamlit as st
from utils import get_wikipedia_info, get_openai_info

st.title("Information Finder")
st.write("Enter a word to get information from Wikipedia and OpenAI API")

word = st.text_input("Enter a word")

if word:
    st.subheader("Wikipedia Information")
    with st.spinner("Fetching information..."):
        st.write(get_wikipedia_info(word))

    st.subheader("OpenAI Information")
    with st.spinner("Fetching information..."):
        st.write(get_openai_info(word))

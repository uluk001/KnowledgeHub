import streamlit as st
from utils import get_wikipedia_info, get_openai_info

st.title("Information Finder")
st.write("Enter a word to get information from Wikipedia and OpenAI API")

word = st.text_input("Enter a word")

if word:
    wiki_info, variants = get_wikipedia_info(word)

    if variants:
        st.subheader("Wikipedia Information")
        st.write(f"{word} may refer to:")
        selected_variant = st.selectbox("Select an option", variants)

        if selected_variant:
            selected_wiki_info, _ = get_wikipedia_info(selected_variant)
            st.subheader(f"Wikipedia Information about {selected_variant}")
            st.write(selected_wiki_info)

            with st.spinner("Fetching information from OpenAI API..."):
                selected_openai_info = get_openai_info(selected_variant)
            st.subheader(f"OpenAI API Information about {selected_variant}")
            st.write(selected_openai_info)
    else:
        st.subheader("Wikipedia Information")
        st.write(wiki_info)

        with st.spinner("Fetching information from OpenAI API..."):
            openai_info = get_openai_info(word)
        st.subheader("OpenAI API Information")
        st.write(openai_info)

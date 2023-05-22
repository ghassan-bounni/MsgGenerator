import streamlit as st
from components import form
from utils import generate_letter

if "page" not in st.session_state:
    st.session_state.page = 1


if st.session_state.page == 1:
    st.title("Generate Letter")

    prompt, word_count = form()

    if prompt:
        res = generate_letter(prompt, word_count)
        st.session_state.res = res
        st.session_state.page = 2
        st.experimental_rerun()

if st.session_state.page == 2:
    st.title("Letter")
    st.write(st.session_state.res)
    if st.button("Back"):
        st.session_state.page = 1
        st.experimental_rerun()

import streamlit as st
from components import form
from utils import generate_letter

st.set_page_config(page_title="Letter Generator", page_icon="✉️")

st.markdown("""
<style>
footer {visibility : hidden;}
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = 1


if st.session_state.page == 1:
    st.title("Generate Letter")

    prompt = form()

    if prompt:
        res = generate_letter(prompt)
        st.session_state.res = res
        st.session_state.page = 2
        st.experimental_rerun()

if st.session_state.page == 2:
    st.title("Letter")
    st.write(st.session_state.res)
    if st.button("Back"):
        st.session_state.page = 1
        st.experimental_rerun()

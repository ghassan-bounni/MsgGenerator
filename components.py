import streamlit as st
import constants as c


def form():
    with st.form("my-form"):
        occasion = st.selectbox("What is the occasion of the message?", c.occasion)
        target = st.selectbox("Who is the recipient?", c.target)
        relation = st.selectbox("Who is the sender?", c.relation)
        tone = st.selectbox("What the tone of the message?", c.tone)
        word_count = st.selectbox("Message Length", [70, 100, 170, 200])
        # optional selection
        nickname = st.text_input("Do you want to include nickname in the message? If yes, what is it?")
        father_to = st.text_input("He is a father to?")
        profession = st.text_input("What is his profession?")
        hobbies = st.text_input("What are some of his hobbies?")

        if st.form_submit_button("Generate"):
            prompt = f"write a {tone} message for {occasion} to my {target}, " \
                     f"I'm his {relation}"

            if nickname:
                prompt += f", his nickname is {nickname}"

            if father_to:
                prompt += f", a father to {father_to}"

            if profession:
                prompt += f", he is a {profession}"

            if hobbies:
                prompt += f", and he likes {hobbies}"

            prompt += f", Please keep the message concise, with a maximum of {word_count} words."

            return prompt, word_count
        else:
            return None, None
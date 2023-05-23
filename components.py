import streamlit as st


def form():
    with st.form("my-form"):
        sender = st.text_input("Who is it from? :red[*]", placeholder="your name, your nickname, etc.")
        target = st.text_input("Who is it for? (add your relation to this person, use a nickname if you want) "
                               ":red[*]",
                               placeholder="lil' bits my best friend, my baby boo, my mom , my boyfriend Johnny, "
                                           "etc.")
        occasion = st.text_input("What is the occasion? :red[*]",
                                 placeholder="birthday, anniversary, Father's Day, etc.")
        tone = st.text_input("What is the tone of the letter? :red[*]", placeholder="funny, serious, etc.")
        # optional selection
        memory = st.text_input("What is your favorite memory with this person? (optional, "
                               "don't start with my favorite memory is)",
                               placeholder="skydiving, summer camp, fishing trip, etc.")

        descriptive_words = st.text_input("What words best describe the recipient of this letter?  "
                                          "(optional, comma separated)",
                                          placeholder="kind, funny, smart, etc.")

        if st.form_submit_button("Generate"):

            if sender == "" or target == "" or occasion == "" or tone == "":
                st.error("Please fill in all required fields")
                return None

            prompt = f"write a {tone} message for {occasion} to {target}, " \

            if memory != "":
                prompt += f", my favorite memory of this person is {memory}"

            if descriptive_words != "":
                prompt += f", I think he is {descriptive_words}"

            prompt += f", Please keep the message concise, between 140 and 200 words. my name is {sender}."

            return prompt,
        else:
            return None

import openai
import streamlit as st

openai.api_key = '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'

def summarize(prompt):
    augmented_prompt = f"summarize this text: {prompt}"
    try:
        st.session_state["summary"] = openai.Completion.create(
            model="text-davinci-003",
            prompt=augmented_prompt,
            temperature=.5,
            max_tokens=1000,
        )["choices"][0]["text"]
    except:
        st.write('There was an error =(')
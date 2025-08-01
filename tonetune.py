import streamlit as st
import openai

client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("ToneTune AI - Tone Changer")

text_input = st.text_area("Enter your message:", height=200)
tone = st.selectbox("Select the tone you want:", [
    "Friendly", "Professional", "Empathetic", "Apologetic", "Assertive", "Romantic", "Neutral"
])

if st.button("Rewrite Tone"):
    if not text_input:
        st.warning("Please enter a message to rewrite.")
    else:
        prompt = f"""You are a tone coach. Rewrite the following message in a more {tone} tone:\nMessage: "{text_input}"\nNew version:"""
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            temperature=0.7,
            max_tokens=200
        )
        st.success(response.choices[0].text.strip())


import streamlit as st
import openai

# Use Streamlit's session state to store a list of rewritten messages
if "rewrites" not in st.session_state:
    st.session_state.rewrites = []

# This creates a connection to the OpenAI service using your secret API key
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
        # The prompt that tells the AI what to do
        prompt = f"""You are a tone coach. Rewrite the following message in a more {tone} tone:\nMessage: "{text_input}"\nNew version:"""
        
        # This is the new, correct way to send the request to the AI
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            temperature=0.7,
            max_tokens=200
        )
        
        # This gets the rewritten text from the AI's response
        rewritten_text = response.choices[0].text.strip()
        
        # Display the rewritten text
        st.success(rewritten_text)
        
        # Add the rewritten text to our list in the temporary memory
        st.session_state.rewrites.append(rewritten_text)

# This section of code runs every time the app reloads
# It displays the saved rewrites
st.markdown("---")
st.subheader("Saved Rewrites")
for i, rewrite in enumerate(st.session_state.rewrites):
    st.write(f"{i+1}. {rewrite}")

import streamlit as st
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Title and description
st.title("🤖 Gemini Chat App")
st.write("Chat with Google's Gemini AI model")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


CLIENT = genai.Client()
MODEL = "gemini-2.5-flash"
PROMPT = """"""

# Input for user message
user_input = st.text_input("Enter your message:", key="user_message")

# Button to send message
if st.button("Send") and user_input:
    with st.spinner("Getting response..."):
        try:
            # Generate response from Gemini
            response = CLIENT.models.generate_content(
                model=MODEL,
                contents=user_input
            )
            
            # Display user message
            st.write("**You:**", user_input)
            
            # Display AI response
            st.write("**Gemini:**", response.text)
            
        except Exception as e:
            st.error(f"Error: {str(e)}")
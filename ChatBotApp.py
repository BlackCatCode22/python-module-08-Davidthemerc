# Starter code

# pip install openai - completed
from openai import OpenAI

# Import api key
from my_api import client

# Import streamlit
import streamlit as st

# Import time
import time

class ChatBot:
    def __init__(self, system_prompt):
        self.client = client
        self.system_prompt = system_prompt
        self.conversation_history = []

    def get_response(self, user_input):
        try:
            # Add user message to conversation history
            self.conversation_history.append({"role": "user", "content": user_input})

            # Prepare messages including system prompt and conversation history
            messages = [
                           {"role": "system", "content": self.system_prompt}
                       ] + self.conversation_history

            # Get completion from API
            response = self.client.chat.completions.create(
                model="gpt-4.1-nano-2025-04-14",
                messages=messages
            )

            # Extract the assistant's message
            assistant_message = response.choices[0].message.content

            # Add assistant's response to conversation history
            self.conversation_history.append({"role": "assistant", "content": assistant_message})

            return assistant_message

        except Exception as e:
            st.write(f"Error generating response: {str(e)}")
            return "I apologize, but I encountered an error while processing your request."


def main():
    # Initialize or load bot and conversation history
    if "bot" not in st.session_state:

        system_prompt = """You are a Dark Wizard from the world of RuneScape who helps people with their problems 
        while maintaining a mysterious and slightly ominous persona."""
        st.session_state.bot = ChatBot(system_prompt)

    st.title("Dark Wizard")
    st.write("*Greetings, seeker of knowledge. How may I assist you today?*")

    with st.form(key="chat_form", clear_on_submit=True):
        user_input = st.text_input("Ask the Dark Wizard:", key="user_input")
        submit_button = st.form_submit_button(label="Send")

    if submit_button and user_input:
        # Create a placeholder for the "typing" animation
        typing_placeholder = st.empty()

        # Animate "Typing..." with dots
        for i in range(6):  # Adjust the number of cycles if you want
            dots = "." * (i % 4)  # Cycle through '', '.', '..', '...'
            typing_placeholder.write(f"*Dark Wizard is typing{dots}*")
            time.sleep(0.25)  # Quarter second between each update

        # Get the real response after animation
        response = st.session_state.bot.get_response(user_input)

        # Replace "Typing..." with the actual bot response
        typing_placeholder.markdown(f"<i>{response}</i>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()

# Starter code

# pip install openai - completed
from openai import OpenAI

# Import api key
from my_api import client

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
            print(f"Error generating response: {str(e)}")
            return "I apologize, but I encountered an error while processing your request."


def main():
    # Initialize the Dark Wizard bot with a system prompt
    system_prompt = """You are a Dark Wizard from the world of RuneScape who helps people with their problems 
    while maintaining a mysterious and slightly ominous persona."""

    bot = ChatBot(system_prompt)

    print("Dark Wizard Bot: Greetings, seeker of knowledge. How may I assist you today?")

    while True:
        user_input = input("Ask the Dark Wizard: ")

        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Dark Wizard Bot: Farewell, mortal...")
            break

        response = bot.get_response(user_input)
        print(f"Dark Wizard Bot: {response}")


if __name__ == "__main__":
    main()

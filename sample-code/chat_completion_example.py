"""
Chat Completion Example with OpenAI
This script demonstrates how to create an interactive chat session with OpenAI's API.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ChatSession:
    def __init__(self):
        """Initialize a new chat session with an empty message history."""
        self.messages = [
            {"role": "system", "content": "You are a helpful AI assistant."}
        ]
    
    def add_message(self, role, content):
        """
        Add a message to the chat history.
        
        Args:
            role (str): Either 'user' or 'assistant'
            content (str): The message content
        """
        self.messages.append({"role": role, "content": content})
    
    def get_response(self):
        """
        Get a response from the OpenAI API based on the chat history.
        
        Returns:
            str: The assistant's response
        """
        try:
            response = client.chat.completions.create(
                model="gpt-4.1-nano-2025-04-14",
                messages=self.messages,
                temperature=0.7,
                max_tokens=150
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"

def main():
    # Create a new chat session
    chat = ChatSession()
    
    # Example conversation
    print("Starting chat session (type 'quit' to exit)")
    print("-" * 50)
    
    while True:
        # Get user input
        user_input = input("\nYou: ")
        
        # Check if user wants to quit
        if user_input.lower() == 'quit':
            break
        
        # Add user message to chat history
        chat.add_message("user", user_input)
        
        # Get and print assistant's response
        response = chat.get_response()
        print(f"\nAssistant: {response}")
        
        # Add assistant's response to chat history
        chat.add_message("assistant", response)

if __name__ == "__main__":
    main() 
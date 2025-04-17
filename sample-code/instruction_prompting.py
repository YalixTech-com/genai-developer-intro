"""
Instruction Prompting Example with OpenAI
This script demonstrates instruction prompting using OpenAI's API.
Instruction prompting gives the model a clear, direct instruction to perform a specific task.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def instruction_prompt(prompt_instruction):
    """
    Send an instruction prompt to OpenAI's API and get a response.
    Args:
        prompt_instruction (str): The instruction for the model.
    Returns:
        str: The model's response.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt_instruction}
            ],
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("Example: Instruction Prompting")
    instruction = "Summarize the following text in one sentence: Artificial intelligence is a branch of computer science that aims to create machines capable of intelligent behavior."
    response = instruction_prompt(instruction)
    print(f"Instruction: {instruction}")
    print(f"Model's Response: {response}\n")

if __name__ == "__main__":
    main()
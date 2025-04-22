"""
Simple Prompting Example with OpenAI
This script demonstrates basic prompt engineering concepts using OpenAI's API.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def basic_prompt(prompt_text):
    """
    Send a simple prompt to OpenAI's API and get a response.
    
    Args:
        prompt_text (str): The prompt to send to the model
        
    Returns:
        str: The model's response
    """
    try:
        response = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4.1-nano-2025-04-14"),
            messages=[
                {"role": "user", "content": prompt_text}
            ],
            temperature=float(os.getenv("OPENAI_TEMPERATURE", 0.7)),
            max_tokens=int(os.getenv("OPENAI_MAX_TOKENS", 150)),
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    # Example 1: Simple question
    print("Example 1: Simple Question")
    response = basic_prompt("What is artificial intelligence?")
    print(f"Response: {response}\n")
    
    # Example 2: Role-based prompt
    print("Example 2: Role-based Prompt")
    response = basic_prompt("You are a helpful AI assistant. Explain quantum computing in simple terms.")
    print(f"Response: {response}\n")
    
    # Example 3: Structured prompt
    print("Example 3: Structured Prompt")
    response = basic_prompt("""Please provide a brief explanation of machine learning, including:
    1. Definition
    2. Key concepts
    3. Common applications""")
    print(f"Response: {response}\n")

if __name__ == "__main__":
    main()
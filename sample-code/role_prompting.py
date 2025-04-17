"""
Role Prompting Example with OpenAI
This script demonstrates role-based prompting using OpenAI's API.
Role prompting assigns a specific persona or role to the model to guide its responses.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def role_prompt(prompt_with_role):
    """
    Send a role-based prompt to OpenAI's API and get a response.
    Args:
        prompt_with_role (str): The prompt assigning a role to the model.
    Returns:
        str: The model's response.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt_with_role}
            ],
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("Example: Role-Based Prompting")
    prompt = "You are a professional chef. Explain how to make a perfect omelette."
    response = role_prompt(prompt)
    print(f"Prompt: {prompt}")
    print(f"Model's Response: {response}\n")

if __name__ == "__main__":
    main()
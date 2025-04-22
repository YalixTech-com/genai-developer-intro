"""
Demonstration Prompting Example with OpenAI
This script demonstrates demonstration-based prompting using OpenAI's API.
Demonstration prompting provides the model with explicit demonstrations of how to perform a task before asking it to complete a similar task.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def demonstration_prompt(prompt_with_demonstrations):
    """
    Send a demonstration-based prompt to OpenAI's API and get a response.
    Args:
        prompt_with_demonstrations (str): The prompt including demonstrations and the final query.
    Returns:
        str: The model's response.
    """
    try:
        response = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
            messages=[
                {"role": "user", "content": prompt_with_demonstrations}
            ],
            temperature=float(os.getenv("OPENAI_TEMPERATURE", 0.7)),
            max_tokens=int(os.getenv("OPENAI_MAX_TOKENS", 150))
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("Example: Demonstration-Based Prompting")
    demonstrations = """
    Input: 2 + 2
    Output: 4
    
    Input: 5 + 7
    Output: 12
    """
    query = "Input: 8 + 6\nOutput:"
    prompt = f"{demonstrations}\n{query}"
    response = demonstration_prompt(prompt)
    print(f"Prompt: {prompt}")
    print(f"Model's Response: {response}\n")

if __name__ == "__main__":
    main()
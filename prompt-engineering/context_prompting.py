"""
Context Prompting Example with OpenAI
This script demonstrates context-based prompting using OpenAI's API.
Context prompting provides relevant background or situational information to guide the model's response.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def context_prompt(prompt_with_context):
    """
    Send a context-based prompt to OpenAI's API and get a response.
    Args:
        prompt_with_context (str): The prompt including context information.
    Returns:
        str: The model's response.
    """
    try:
        response = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
            messages=[
                {"role": "user", "content": prompt_with_context}
            ],
            temperature=float(os.getenv("OPENAI_TEMPERATURE", 0.7)),
            max_tokens=int(os.getenv("OPENAI_MAX_TOKENS", 150))
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("Example: Context-Based Prompting")
    context = "You are helping a student prepare for a biology exam."
    question = "Explain the process of photosynthesis."
    prompt = f"{context}\n{question}"
    response = context_prompt(prompt)
    print(f"Prompt: {prompt}")
    print(f"Model's Response: {response}\n")

if __name__ == "__main__":
    main()
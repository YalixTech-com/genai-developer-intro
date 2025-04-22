"""
Contrastive Prompting Example with OpenAI
This script demonstrates contrastive prompting using OpenAI's API.
Contrastive prompting provides multiple options or examples and asks the model to compare or choose between them.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def contrastive_prompt(prompt_with_options):
    """
    Send a contrastive prompt to OpenAI's API and get a response.
    Args:
        prompt_with_options (str): The prompt presenting options for comparison.
    Returns:
        str: The model's response.
    """
    try:
        response = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
            messages=[
                {"role": "user", "content": prompt_with_options}
            ],
            temperature=float(os.getenv("OPENAI_TEMPERATURE", 0.7)),
            max_tokens=int(os.getenv("OPENAI_MAX_TOKENS", 150))
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("Example: Contrastive Prompting")
    prompt = "Compare the following two explanations for why the sky is blue and say which is more accurate and why.\nExplanation 1: The sky is blue because the ocean reflects its color.\nExplanation 2: The sky is blue because molecules in the air scatter blue light from the sun more than they scatter red light."
    response = contrastive_prompt(prompt)
    print(f"Prompt: {prompt}")
    print(f"Model's Response: {response}\n")

if __name__ == "__main__":
    main()
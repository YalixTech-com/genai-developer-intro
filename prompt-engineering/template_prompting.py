"""
Template Prompting Example with OpenAI
This script demonstrates template-based prompting using OpenAI's API.
Template prompting uses a reusable prompt structure with placeholders for dynamic content.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def template_prompt(prompt_template, **kwargs):
    """
    Send a template-based prompt to OpenAI's API and get a response.
    Args:
        prompt_template (str): The prompt template with placeholders.
        **kwargs: Values to fill in the template.
    Returns:
        str: The model's response.
    """
    prompt_filled = prompt_template.format(**kwargs)
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt_filled}
            ],
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("Example: Template-Based Prompting")
    template = "Translate the following {source_language} sentence to {target_language}: {sentence}"
    response = template_prompt(template, source_language="English", target_language="Spanish", sentence="How are you?")
    print(f"Prompt Template: {template}")
    print(f"Model's Response: {response}\n")

if __name__ == "__main__":
    main()
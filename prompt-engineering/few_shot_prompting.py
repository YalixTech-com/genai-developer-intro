"""
Few-Shot Prompting Example with OpenAI
This script demonstrates few-shot prompting using OpenAI's API.
Few-shot prompting provides the model with a small number of examples
(shots) of the desired task format or output before asking the actual question.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def few_shot_prompt(prompt_with_examples):
    """
    Send a few-shot prompt to OpenAI's API and get a response.
    
    Args:
        prompt_with_examples (str): The prompt including examples and the final query.
        
    Returns:
        str: The model's response.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt_with_examples}
            ],
            temperature=0.7,
            max_tokens=150,
            stop=["\n\n"] # Often helpful to stop generation after the answer
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    # Example: Simple English to French translation with examples
    print("Example: Few-Shot English to French Translation")
    
    # Provide a few examples (shots) in the prompt
    examples = """
    English: sea otter
    French: loutre de mer
    
    English: peppermint
    French: menthe poivrée
    
    English: plush girafe
    French: girafe en peluche
    """
    
    word_to_translate = "cheese"
    prompt = f"{examples}\nEnglish: {word_to_translate}\nFrench:"
    
    response = few_shot_prompt(prompt)
    print(f"English: {word_to_translate}")
    print(f"French Translation: {response}\n")

if __name__ == "__main__":
    main()
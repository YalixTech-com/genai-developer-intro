"""
Chain-of-Thought Prompting Example with OpenAI
This script demonstrates chain-of-thought (CoT) prompting using OpenAI's API.
CoT prompting encourages the model to reason step by step before answering.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chain_of_thought_prompt(prompt_with_cot):
    """
    Send a chain-of-thought prompt to OpenAI's API and get a response.
    Args:
        prompt_with_cot (str): The prompt including a request for step-by-step reasoning.
    Returns:
        str: The model's response.
    """
    try:
        response = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
            messages=[
                {"role": "user", "content": prompt_with_cot}
            ],
            temperature=float(os.getenv("OPENAI_TEMPERATURE", 0.7)),
            max_tokens=int(os.getenv("OPENAI_MAX_TOKENS", 200))
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("Example: Chain-of-Thought Reasoning")
    question = "If there are 3 cars and each car has 4 wheels, how many wheels are there in total?"
    prompt = f"{question}\nLet's think step by step."
    response = chain_of_thought_prompt(prompt)
    print(f"Question: {question}")
    print(f"Model's Reasoning and Answer: {response}\n")

if __name__ == "__main__":
    main()
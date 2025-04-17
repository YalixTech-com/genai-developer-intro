"""
Retrieval-Augmented Prompting Example with OpenAI
This script demonstrates retrieval-augmented prompting using OpenAI's API.
Retrieval-augmented prompting supplements the prompt with relevant external information to improve the model's response.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def retrieval_augmented_prompt(prompt_with_context):
    """
    Send a retrieval-augmented prompt to OpenAI's API and get a response.
    Args:
        prompt_with_context (str): The prompt including retrieved context and the query.
    Returns:
        str: The model's response.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt_with_context}
            ],
            temperature=0.7,
            max_tokens=200
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("Example: Retrieval-Augmented Prompting")
    retrieved_context = "Wikipedia: The mitochondrion is the powerhouse of the cell."
    question = "What is the function of mitochondria in a cell?"
    prompt = f"{retrieved_context}\nQuestion: {question}"
    response = retrieval_augmented_prompt(prompt)
    print(f"Prompt: {prompt}")
    print(f"Model's Response: {response}\n")

if __name__ == "__main__":
    main()
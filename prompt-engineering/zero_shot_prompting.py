"""
Zero-Shot Prompting Example with OpenAI
This script demonstrates zero-shot prompting using OpenAI's API.
Zero-shot prompting means the model is asked to perform a task
without any prior examples of how to do it.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def zero_shot_prompt(prompt_text):
    """
    Send a zero-shot prompt to OpenAI's API and get a response.
    
    Args:
        prompt_text (str): The prompt describing the task.
        
    Returns:
        str: The model's response.
    """
    try:
        response = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
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
    # Example: Sentiment analysis without examples
    print("Example: Zero-Shot Sentiment Analysis")
    text_to_analyze = "I absolutely loved the movie! It was fantastic."
    prompt = f"Classify the sentiment of the following text: '{text_to_analyze}'\nSentiment:"
    response = zero_shot_prompt(prompt)
    print(f"Text: {text_to_analyze}")
    print(f"Response: {response}\n")
    
    text_to_analyze_2 = "The weather today is quite gloomy and dull."
    prompt_2 = f"Classify the sentiment of the following text: '{text_to_analyze_2}'\nSentiment:"
    response_2 = zero_shot_prompt(prompt_2)
    print(f"Text: {text_to_analyze_2}")
    print(f"Response: {response_2}\n")

if __name__ == "__main__":
    main()
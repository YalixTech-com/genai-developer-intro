"""
Basic LangChain Example
This script demonstrates how to create a simple chain using LangChain.
"""

import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load environment variables from .env file
load_dotenv()

def create_summary_chain():
    """
    Create a LangChain that generates summaries of text.
    
    Returns:
        LLMChain: A chain that can generate summaries
    """
    # Create a prompt template
    template = """
    Please provide a concise summary of the following text:
    
    {text}
    
    Summary:
    """
    
    prompt = PromptTemplate(
        input_variables=["text"],
        template=template
    )
    
    # Initialize the language model
    llm = OpenAI(
        temperature=0.7,
        model_name="gpt-3.5-turbo"
    )
    
    # Create the chain
    chain = LLMChain(llm=llm, prompt=prompt)
    
    return chain

def main():
    # Create the summary chain
    summary_chain = create_summary_chain()
    
    # Example text to summarize
    text = """
    Artificial Intelligence (AI) is the simulation of human intelligence by machines.
    It encompasses machine learning, natural language processing, and robotics.
    AI systems can learn from experience, adjust to new inputs, and perform human-like tasks.
    """
    
    # Generate summary
    print("Original Text:")
    print(text)
    print("\nGenerating summary...")
    
    result = summary_chain.run(text=text)
    print("\nSummary:")
    print(result)

if __name__ == "__main__":
    main() 
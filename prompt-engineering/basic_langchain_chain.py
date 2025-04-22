"""
Basic LangChain Example
This script demonstrates how to create a simple chain using LangChain 0.3.
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# Load environment variables from .env file
load_dotenv()

def create_summary_chain():
    """
    Create a LangChain that generates summaries of text.
    
    Returns:
        A chain that can generate summaries
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
    llm = ChatOpenAI(
        temperature=float(os.getenv("OPENAI_TEMPERATURE", 0.7)),
        model=os.getenv("OPENAI_MODEL", "gpt-4.1-nano-2025-04-14")
    )
    
    # Create the chain using the new LCEL (LangChain Expression Language)
    chain = (
        {"text": RunnablePassthrough()} 
        | prompt 
        | llm 
        | StrOutputParser()
    )
    
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
    
    # Updated invocation method
    result = summary_chain.invoke(text)
    print("\nSummary:")
    print(result)

if __name__ == "__main__":
    main()
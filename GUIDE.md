# Getting Started with Generative AI: A Beginner's Guide

Welcome to the world of Generative AI! This guide will help you understand the basics and get you started with practical examples.

## Table of Contents
1. [Introduction to Generative AI](#introduction-to-generative-ai)
2. [Understanding Large Language Models (LLMs)](#understanding-large-language-models-llms)
3. [Getting Started with OpenAI](#getting-started-with-openai)
4. [Setting Up Your Environment](#setting-up-your-environment)
5. [Sample Code Walkthrough](#sample-code-walkthrough)
6. [Next Steps](#next-steps)

## Introduction to Generative AI

Generative AI refers to artificial intelligence systems that can create new content, such as text, images, or code. Unlike traditional AI that focuses on classification or prediction, generative AI can produce original outputs based on its training data.

### Key Concepts:
- **Generative Models**: AI models that can create new content
- **Large Language Models (LLMs)**: AI models trained on vast amounts of text data
- **Prompt Engineering**: The art of crafting effective inputs to get desired outputs
- **Fine-tuning**: Customizing pre-trained models for specific tasks

## Understanding Large Language Models (LLMs)

LLMs are the foundation of modern generative AI. They work by:
1. Processing input text (prompts)
2. Understanding context and patterns
3. Generating relevant responses

### Popular LLMs:
- GPT (OpenAI)
- Claude (Anthropic)
- LLaMA (Meta)
- Gemini (Google)

## Getting Started with OpenAI

To use the sample code in this repository:

1. Create an OpenAI account at https://platform.openai.com
2. Generate an API key
3. Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

## Setting Up Your Environment

Before running the sample code, you'll need to set up a Python virtual environment:

1. **Create a virtual environment**:
   ```
   # On Windows
   python -m venv venv
   
   # On macOS/Linux
   python3 -m venv venv
   ```

2. **Activate the virtual environment**:
   ```
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Run the sample code**:
   ```
   # Run the simple prompting example
   python simple_prompting.py
   
   # Run the chat completion example
   python chat_completion_example.py
   
   # Run the LangChain example
   python basic_langchain_chain.py
   ```

## Sample Code Walkthrough

This repository includes three example scripts:

1. **simple_prompting.py**: Basic prompt examples
2. **chat_completion_example.py**: Interactive chat session
3. **basic_langchain_chain.py**: Simple LangChain implementation

Try running each example to understand different ways to interact with LLMs.

## Next Steps

Ready to dive deeper? Here are some suggested next steps:

1. **Learn More About Prompt Engineering**
   - Study different prompt patterns
   - Experiment with temperature and other parameters
   - Practice with different types of tasks

2. **Explore Advanced Tools**
   - LangChain for building complex applications
   - Vector databases for semantic search
   - Fine-tuning for custom models

3. **Join the Community**
   - Follow AI research papers
   - Participate in AI forums
   - Share your experiments and learnings

## Additional Resources

- [OpenAI Documentation](https://platform.openai.com/docs)
- [LangChain Documentation](https://python.langchain.com/docs)
- [Prompt Engineering Guide](https://www.promptingguide.ai)

Remember: The field of AI is rapidly evolving. Stay curious and keep learning! 
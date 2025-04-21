# Prompt Engineering Examples

This directory contains various examples demonstrating different prompt engineering techniques using OpenAI's GPT models. Each example showcases a specific prompting strategy that can be used to improve the quality and reliability of AI responses.

## 🎯 Examples Overview

1. **Basic Prompting**
   - `simple_prompting.py` - Basic examples of text completion
   - `chat_completion_example.py` - Interactive chat completion examples

2. **Advanced Prompting Techniques**
   - `zero_shot_prompting.py` - Zero-shot learning without examples
   - `few_shot_prompting.py` - Few-shot learning with examples
   - `chain_of_thought_prompting.py` - Step-by-step reasoning
   - `role_prompting.py` - Role-based prompting
   - `context_prompting.py` - Context-aware prompting
   - `instruction_prompting.py` - Clear instruction-based prompting
   - `template_prompting.py` - Template-based prompting
   - `contrastive_prompting.py` - Comparing different scenarios
   - `demonstration_prompting.py` - Learning from demonstrations
   - `retrieval_augmented_prompting.py` - Using external knowledge

3. **Framework Examples**
   - `basic_langchain_chain.py` - Introduction to LangChain

## 🚀 Getting Started

### Prerequisites

1. **Install Python**
   - Download Python from [python.org](https://www.python.org/downloads/)
   - Choose Python 3.8 or higher
   - During installation, check "Add Python to PATH"

2. **Verify Python Installation**
   ```bash
   python --version
   pip --version
   ```

### Setting Up Virtual Environment

#### Windows
```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
.\venv\Scripts\activate

# Verify activation (should show path to venv)
where python
```

#### Linux/Mac
```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Verify activation (should show path to venv)
which python
```

### Installing Dependencies

1. **Navigate to Prompt Engineering Directory**
   ```bash
   cd /path/to/genai-developer-intro/prompt-engineering
   ```

2. **Install Requirements**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify Installation**
   ```bash
   pip list
   ```

### Setting Up OpenAI API Key

1. **Create .env File**
   - The `.env` file is already in the prompt-engineering directory
   - Update the OpenAI API key in the `.env` file:
     ```
     OPENAI_API_KEY=your-key-here
     ```

2. **Get API Key**
   - Visit [OpenAI Platform](https://platform.openai.com/)
   - Create an account or sign in
   - Navigate to API Keys section
   - Create a new API key
   - Copy and paste into your `.env` file

### Running Examples

1. **Ensure You're in the Correct Directory**
   ```bash
   # You should be in the prompt-engineering directory
   pwd  # Should show path ending in /prompt-engineering
   ```

2. **Run Any Example**
   ```bash
   # Basic example
   python simple_prompting.py

   # Advanced example
   python few_shot_prompting.py

   # Framework example
   python basic_langchain_chain.py
   ```

3. **Troubleshooting**
   - If you get module not found errors, ensure you're in the virtual environment
   - If you get API errors, verify your API key in the `.env` file
   - For other issues, check the error message and ensure all dependencies are installed

## 📚 Example Descriptions

### Basic Examples
- **Simple Prompting**: Basic text completion examples
- **Chat Completion**: Interactive chat examples with the model

### Advanced Techniques
- **Zero-Shot Prompting**: Get responses without providing examples
- **Few-Shot Prompting**: Improve responses by providing examples
- **Chain of Thought**: Guide the model through step-by-step reasoning
- **Role Prompting**: Assign specific roles to the model
- **Context Prompting**: Provide relevant context for better responses
- **Instruction Prompting**: Use clear, specific instructions
- **Template Prompting**: Use structured templates for consistent outputs
- **Contrastive Prompting**: Compare different scenarios for better understanding
- **Demonstration Prompting**: Show examples of desired behavior
- **Retrieval Augmented**: Combine external knowledge with prompts

### Framework Examples
- **LangChain Basics**: Introduction to using LangChain for prompt engineering

## 💡 Best Practices

1. **Be Specific**: Clear and specific prompts yield better results
2. **Provide Context**: Include relevant context when needed
3. **Use Examples**: Include examples for complex tasks
4. **Iterate**: Test and refine your prompts
5. **Consider Constraints**: Be aware of token limits and model capabilities

## 🔍 Tips for Each Technique

### Zero-Shot Prompting
- Use clear, specific instructions
- Break down complex tasks
- Include necessary context

### Few-Shot Prompting
- Choose diverse, representative examples
- Maintain consistent format
- Include both input and expected output

### Chain of Thought
- Guide through logical steps
- Ask for explanations
- Break down complex problems

### Role Prompting
- Define clear role boundaries
- Specify expertise level
- Include relevant context

## 🤝 Contributing

Feel free to contribute new examples or improvements to existing ones. Please ensure your code follows the project's style and includes appropriate documentation.

## 📝 License

This project is licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License (CC BY-NC-ND 4.0). 
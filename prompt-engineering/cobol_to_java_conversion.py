"""
COBOL to Java Program Conversion
This script demonstrates COBOL to Java conversion using OpenAI's API.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def read_file(file_path):
    """
    Read the contents of a file.
    
    Args:
        file_path (str): Path to the file to read
        
    Returns:
        str: Contents of the file
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"

def write_file(file_path, content):
    """
    Write content to a file.
    
    Args:
        file_path (str): Path to the file to write
        content (str): Content to write to the file
    """
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except Exception as e:
        print(f"Error writing file: {str(e)}")

def convert_cobol_to_java(cobol_code):
    """
    Convert COBOL code to Java using OpenAI's API.
    
    Args:
        cobol_code (str): The COBOL code to convert
        
    Returns:
        str: The converted Java code
    """
    try:
        system_prompt = """You are an expert COBOL to Java conversion specialist with deep knowledge of both languages.
        Your task is to convert COBOL code to Java while following these strict guidelines:
        1. Follow Java naming conventions (camelCase for variables, PascalCase for classes)
        2. Use proper Java data types that match COBOL data types
        3. Include proper Java package declaration
        4. Add comprehensive JavaDoc comments
        5. Follow Java best practices and design patterns
        6. Ensure the code is compilable without any errors
        7. Include proper error handling
        8. Use appropriate Java collections and data structures
        9. Follow SOLID principles
        10. Include proper access modifiers
        11. Use proper Java logging instead of DISPLAY statements
        12. Convert COBOL file operations to appropriate Java I/O operations
        13. Handle COBOL numeric data types appropriately in Java
        14. Convert COBOL PERFORM statements to appropriate Java loops
        15. Ensure thread safety where applicable
        
        Return only the Java code without any additional explanations or markdown formatting.
        The code should be immediately compilable and runnable."""
        
        user_prompt = f"""Convert the following COBOL code to Java while strictly following the guidelines above.
        Ensure the converted code is production-ready and follows all Java standards.
        
        COBOL Code:
        {cobol_code}
        """
        
        response = client.chat.completions.create(
            model="gpt-4.1-nano-2025-04-14",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3,  # Lower temperature for more consistent output
            max_tokens=2000  # Increased tokens for more complex conversions
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    # Read the COBOL file
    cobol_code = read_file("sample.cbl")
    if cobol_code.startswith("Error"):
        print(cobol_code)
        return
    
    # Convert COBOL to Java
    print("Converting COBOL to Java...")
    java_code = convert_cobol_to_java(cobol_code)
    
    # Save the Java code to a file
    write_file("java_ai.java", java_code)
    print("Conversion complete. Java code saved to java_ai.java")

if __name__ == "__main__":
    main() 
# CrewAI JSON Processing Project

This project demonstrates how to use CrewAI to process and verify JSON data using AI agents. The project uses CrewAI's built-in LLM handling to connect to OpenAI's models.

## Project Structure

```
crew-ai/
├── data/
│   ├── source1.json         # First source JSON file (flat structure)
│   ├── source2.json         # Second source JSON file (nested structure)
│   └── target_schema.json   # Schema for the output JSON
├── main.py                  # Main script with CrewAI implementation
├── requirements.txt         # Project dependencies
├── .env                     # Environment variables (API keys, model settings)
└── README.md                # Project documentation
```

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
   - Create a `.env` file in the project root directory
   - Add the following variables to the file:
     ```
     OPENAI_API_KEY=your-openai-api-key-here
     OPENAI_MODEL=gpt-4o-mini-2024-07-18
     OPENAI_TEMPERATURE=0.2
     ```
   - Replace `your-openai-api-key-here` with your actual OpenAI API key
   - Optionally, change the model name or temperature as needed

## Usage

Run the main script:
```bash
python main.py
```

The script will:
1. Process data from both source JSON files
2. Combine them according to the target schema
3. Verify the integrity of the processed data
4. Output the verification results

## Agents

1. **Data Processor Agent**
   - Combines data from both source files
   - Follows the target schema
   - Ensures data integrity

2. **Verification Agent**
   - Verifies all data exists in source files
   - Checks schema compliance
   - Ensures no generated data was added
   - Provides detailed verification report

## Output

The processed data will be saved as `processed_output.json` in the data directory, and the verification results will be printed to the console. 
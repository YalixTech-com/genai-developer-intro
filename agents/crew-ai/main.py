import json
from crewai import Agent, Task, Crew, LLM
from crewai_tools import FileReadTool, FileWriterTool
from typing import Dict, List
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class JSONProcessor:
    def __init__(self):
        self.source1_path = "data/source1.json"
        self.source2_path = "data/source2.json"
        self.schema_path = "data/target_schema.json"
        self.output_path = "data/processed_output.json"
        self.verification_report_path = "data/verification_report.json"

        # Initialize the LLM using CrewAI's LLM class
        self.llm = LLM(
            model=os.getenv("OPENAI_MODEL"),
            temperature=float(os.getenv("OPENAI_TEMPERATURE")),
            api_key=os.getenv("OPENAI_API_KEY")
        )
        
    def create_tools(self):
        # Create a single file read tool that can be used for all files
        file_read_tool = FileReadTool()
        
        # Create a single file write tool for the output file
        file_write_tool = FileWriterTool()
        
        return [
            file_read_tool,
            file_write_tool
        ]

    def create_agents(self):
        # Get the tools
        tools = self.create_tools()
        
        # Data Processor Agent
        processor_agent = Agent(
            role='Data Processor',
            goal='Process and combine data from two JSON sources into a new format',
            backstory="""You are an expert data processor specialized in combining and transforming 
            JSON data while maintaining data integrity and following specific schemas. You are efficient
            and avoid redundant operations.""",
            tools=tools,
            llm=self.llm,
            verbose=True
        )

        # Verification Agent
        verification_agent = Agent(
            role='Data Verifier',
            goal='Verify the integrity and accuracy of processed JSON data',
            backstory="""You are a meticulous data verifier who ensures all processed data 
            matches the source data and follows the specified schema. You are efficient and
            avoid redundant operations.""",
            tools=tools,
            llm=self.llm,
            verbose=True
        )

        return processor_agent, verification_agent

    def create_tasks(self, processor_agent, verification_agent):
        # Task 1: Process JSON Data
        process_task = Task(
            description=f"""Read and process data from {self.source1_path} and {self.source2_path}.
            Combine them according to the schema in {self.schema_path}.
            Save the result as {self.output_path}.
            Ensure all data comes from the source files only.
            
            IMPORTANT: Complete this task in a single pass. Do not repeat steps or make redundant calls.
            Read each file only once and process all the data at once.
            
            When using tools, follow this format:
            Thought: Think about what to do next
            Action: The name of the tool to use (e.g., "Read a file's content" or "File Writer Tool")
            Action Input: {{"file_path": "path/to/file"}} for read tools or {{"filename": "filename", "content": "content"}} for write tools
            
            After reading all files, process the data and write the output file in a single step.
            """,
            agent=processor_agent,
            expected_output="A JSON file containing the combined data from both source files, following the target schema."
        )

        # Task 2: Verify Processed Data
        verify_task = Task(
            description=f"""Verify the {self.output_path} file:
            1. Read the processed output file at {self.output_path}
            2. Read the first source file at {self.source1_path}
            3. Read the second source file at {self.source2_path}
            4. Read the target schema at {self.schema_path}
            5. Verify the data integrity and schema compliance
            6. Write the verification report in json format to {self.verification_report_path}
            
            IMPORTANT: Complete this task in a single pass. Do not repeat steps or make redundant calls.
            Read each file only once and perform all verification at once.
            
            When using tools, follow this format:
            Thought: Think about what to do next
            Action: The name of the tool to use (e.g., "Read a file's content" or "File Writer Tool")
            Action Input: {{"file_path": "path/to/file"}} for read tools or {{"filename": "filename", "content": "content"}} for write tools
            
            After reading all files, perform the verification and return the report in a single step.
            """,
            agent=verification_agent,
            expected_output="A detailed verification report confirming that the processed data is valid, complete, and follows the target schema."
        )

        return [process_task, verify_task]

    def run(self):
        # Create agents
        processor_agent, verification_agent = self.create_agents()
        
        # Create tasks
        tasks = self.create_tasks(processor_agent, verification_agent)
        
        # Create and run the crew
        crew = Crew(
            agents=[processor_agent, verification_agent],
            tasks=tasks,
            verbose=True
        )
        
        result = crew.kickoff()
        return result

if __name__ == "__main__":
    processor = JSONProcessor()
    result = processor.run()
    print("\nFinal Result:")
    print(result) 
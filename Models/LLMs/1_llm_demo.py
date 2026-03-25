from langchain_openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo", temperature=0.9)
response = llm("What year did the first man land on the moon?")
print(response)
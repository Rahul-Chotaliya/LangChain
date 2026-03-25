from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


llm = ChatAnthropic(model="claude-2", temperature=0.9)
response = llm.invoke("What year did the first  man land on the moon?")
print(response.content)
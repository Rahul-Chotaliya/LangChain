from langchain_google_genai import ChatGoogleGenAI
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

llm = ChatGoogleGenAI(model="gemini-1.5-pro", temperature=0.9)
response = llm.invoke("What year did the first man land on the moon?")
print(response.content)
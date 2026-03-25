from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()


embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=1024)
response = embeddings("What year did the first man land on the moon?")
print(response)


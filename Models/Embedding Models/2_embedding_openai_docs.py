from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()


embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=1024)

documnets = [
    "The first man landed on the moon in 1969.",
    "The first man to walk on the moon was Neil Armstrong."
]

response = embeddings.embed_documents(documnets)
print(response)
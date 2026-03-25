from langchain_huggingface import HuggingFaceHub,HuggingFaceEndpoint
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

llm = HuggingFaceEndpoint(model = "google/flan-t5-xl", task="text2text-generation", temperature=0.9)

model = HuggingFaceHub(llm=llm)
response = model.invoke("What year did the first man land on the moon?")
print(response.content)
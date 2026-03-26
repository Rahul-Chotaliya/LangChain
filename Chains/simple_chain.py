from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.7)

prompt = PromptTemplate(
    template="What are the latest news about {topic}?",
    input_variables=["topic"]
)

chain = prompt | model 

result = chain.invoke({"topic":"Hardik Pandya"})

print(result.content)
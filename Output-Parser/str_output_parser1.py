from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.7)

template1 = PromptTemplate(
    template= "Write a detailed report on {topic}",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template = "Write a 3 line summary with dot points on following text. \n {text}",
    input_variables=["text"]   
)

parser = StrOutputParser()

chain  = template1 | model | parser | template2 | model | parser

result = chain.invoke({"topic":"Virat Kohli"})

print(result)
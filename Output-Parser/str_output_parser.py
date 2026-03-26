from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.7)

template1 = PromptTemplate(
    template= "Write a detailed report on {topic}",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template = "Write a 5 line summary with dot points on following text. \n {text}",
    input_variables=["text"]   
)

prompt1 = template1.invoke({"topic":"Virat Kohli"})

result = model.invoke(prompt1)
print(result,">>>>>>>>>>>>>>>>")
prompt2 = template2.invoke({"text": result})

result2 = model.invoke(prompt2)
print(result2)
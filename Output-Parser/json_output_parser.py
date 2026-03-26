from langchain_google_genai import GoogleGenerativeAI
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()


model = GoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.7)

parser = JsonOutputParser()

template = PromptTemplate(
    template= "Write a 3 dot points detailed report on {topic}. \n {format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({"topic":"Virat Kohli"})

print(result)
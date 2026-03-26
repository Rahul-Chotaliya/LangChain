from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()


model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.7)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="What are the latest news about {topic}?",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="give me 3 word from the following {text}?",
    input_variables=["text"]
)

chain  = prompt1 | model | parser | prompt2 | model | parser


result = chain.invoke({"topic":"Hardik Pandya"})

print(result)

chain.get_graph().print_ascii()
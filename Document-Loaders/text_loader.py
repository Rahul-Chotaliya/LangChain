from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-pro", temperature=0.7)

prompt = PromptTemplate(
    template="Summarize the following text:\n\n{text}",
    input_variables=["text"],
)

parser = StrOutputParser()

loader = TextLoader(file_path="Document-Loaders/cricket.txt",encoding="utf-8")

docs = loader.load()

print(docs[0].page_content)

print(len(docs))
print(docs[0].metadata)

chain = model | prompt | parser

result = chain(docs[0].page_content)
print(result)
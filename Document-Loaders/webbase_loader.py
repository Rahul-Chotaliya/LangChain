from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-pro", temperature=0.7)

prompt = PromptTemplate(
    template = "answer the following question based on the given context:\n\nContext: {context}\n\nQuestion: {question}",
    input_variables=["context", "question"],
)

parser = StrOutputParser()
url = 'https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7x4hn-a/p/itmdc5308fa78421'
loader = WebBaseLoader(url)

docs = loader.load()

print(docs[0].page_content)
print(docs[0].metadata)

chain = model | prompt | parser

result = chain({"context": docs[0].page_content, "question": "What is the price of the product?"})
print(result)   
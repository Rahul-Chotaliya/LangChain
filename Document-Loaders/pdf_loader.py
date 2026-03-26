from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(file_path="Document-Loaders/dl-curriculum.pdf")

docs = loader.load()

print(docs[0].page_content)
print(docs[1].metadata)
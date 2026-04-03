from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

loader = DirectoryLoader(
    path="Document-Loaders/books",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()
# DIFF BET load() and lazy_load() is that load() will load all documents into memory at once, while lazy_load() will load documents one at a time as needed. This can be more efficient for large collections of documents, as it avoids loading everything into memory at once.

for document in docs:
    print(document.metadata)
from langchain_huggingface import HuggingFaceEndpointEmbeddings

embedding = HuggingFaceEndpointEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2", dimensions=384)

documents = [
    "The first man landed on the moon in 1969.",
    "The first man to walk on the moon was Neil Armstrong."
]

response = embedding.embed_documents(documents)
print(response)
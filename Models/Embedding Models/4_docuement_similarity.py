from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load environment variables from .env file
load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=1024)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = "Who is the best Indian cricketer?"

doc_embeddings = embeddings.embed_documents(documents)
query_embedding = embeddings(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]

index, score = np.argmax(scores), np.max(scores)

print("query:", query)
print("most similar document:", documents[index])
print("similarity score:", score)
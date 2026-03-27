# Models 🤖

Comprehensive guide to LLMs, Chat Models, and Embedding Models in LangChain - the core intelligence behind your applications.

## 🎯 Overview

Models are the AI engines that power LangChain. There are three main types:

1. **LLMs** - Simple text input → text output (older, simpler)
2. **Chat Models** - Message history aware (modern, conversational)
3. **Embeddings** - Text → vectors (semantic understanding)

---

## 📂 Folder Structure

```
Models/
├── Chat Models/        # Conversational AI (recommended)
├── LLMs/              # Legacy LLMs (still useful)
└── Embedding Models/  # Vector representations
```

---

# 💬 Chat Models

Modern language models designed for conversation. Each response is aware of previous messages.

## Files Overview

### 1. **1_chatmodel_openai.py**
**Provider:** OpenAI (GPT-3.5, GPT-4)

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)
response = llm.invoke("What year did the first man land on the moon?")
print(response.content)
```

**Pros:**
- Very capable models
- Good at reasoning
- Reliable API

**Cons:**
- Costs money (most expensive)
- Rate limits
- Requires API key

**Best For:**
- Production applications
- Complex reasoning
- High-quality outputs

**Pricing Tiers:**
- GPT-3.5: Cheapest, good for basic tasks
- GPT-4: Most powerful, higher cost

---

### 2. **2_chatmodel_anthropic.py**
**Provider:** Anthropic (Claude 2, Claude 3)

```python
from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(model="claude-2", temperature=0.9)
response = llm.invoke("What year did the first man land on the moon?")
print(response.content)
```

**Pros:**
- Great at long-form writing
- Good at analysis
- Thoughtful responses

**Cons:**
- Slower responses
- Higher cost than GPT-3.5
- Requires API key

**Best For:**
- Writing and analysis
- Long documents
- Creative tasks

**Models Available:**
- Claude 2: Balanced, reliable
- Claude 3: Newest, most capable

---

### 3. **2_chatmodel_google.py**
**Provider:** Google Gemini (free tier available!)

```python
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.9)
response = llm.invoke("What year did the first man land on the moon?")
print(response.content)
```

**Pros:**
- Free tier available (generous limits)
- Fast responses
- Multimodal (can handle images)
- Good quality

**Cons:**
- Newer (less proven)
- Rate limits on free tier
- Requires Google API key

**Best For:**
- Learning and experimentation
- Multimodal tasks
- Budget-conscious projects

**Models Available:**
- Gemini 1.5 Pro: Latest, most capable
- Gemini 2.0 Flash: Faster, newer

---

### 4. **4_chatmodel_hf_api.py**
**Provider:** HuggingFace (via API)

```python
from langchain_huggingface import HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    model="google/flan-t5-xl",
    task="text2text-generation",
    temperature=0.9
)
response = llm.invoke("What year did the first man land on the moon?")
```

**Pros:**
- Variety of models
- Can use open-source models
- Affordable

**Cons:**
- Variable quality
- Requires HF token
- API-based (may have limits)

**Best For:**
- Specific use-case models
- Cost optimization
- Using open-source models

---

### 5. **5_chatmodel_hf_local.py**
**Provider:** HuggingFace (Local)

```python
from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace

llm = HuggingFacePipeline(
    model="google/flan-t5-xl",
    task="text2text-generation",
    pipeline_kwargs={"temperature": 0.9, "max_new_tokens": 100}
)
model = ChatHuggingFace(llm=llm)
response = model.invoke("What year did the first man land on the moon?")
```

**Pros:**
- No API calls (privacy!)
- No costs
- Works offline
- Full control

**Cons:**
- Requires local resources
- Models are smaller/less capable
- Setup complexity

**Best For:**
- Privacy-sensitive applications
- Offline usage
- Development without internet
- Cost-free inference

---

## 🔄 Chat Models Comparison

| Model | Provider | Cost | Speed | Quality | Best For |
|-------|----------|------|-------|---------|----------|
| GPT-3.5 | OpenAI | $$ | Medium | High | Production |
| GPT-4 | OpenAI | $$$ | Slow | Very High | Complex tasks |
| Claude 2 | Anthropic | $$ | Medium | High | Writing |
| Gemini 1.5 | Google | $ | Fast | High | Learning |
| Flan-T5 | HF | Free | Fast | Medium | Budget |

---

# 🧠 LLMs (Legacy)

Older, simpler interface. Still useful but Chat Models are recommended.

### **1_llm_demo.py**

```python
from langchain_openai import OpenAI

llm = OpenAI(model="gpt-3.5-turbo", temperature=0.9)
response = llm("What year did the first man land on the moon?")
print(response)  # Returns string directly
```

**Differences from Chat Models:**
- Takes string, returns string
- No message history
- Simpler but less powerful
- Not recommended for new projects

---

# 🧮 Embedding Models

Convert text into vectors for semantic understanding and similarity search.

## Concept

An embedding is a numerical representation of text:
```
Text: "cats are fluffy animals"
    ↓
Embedding: [0.2, 0.5, -0.1, 0.8, ...]  (list of numbers)
```

**Why embeddings?**
- Enable semantic search
- Find similar documents
- Cluster related content
- Power recommendation systems

## Files Overview

### 1. **1_embedding_openai_query.py**
**Purpose:** Embed a query string

```python
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=1024)
response = embeddings("What year did the first man land on the moon?")
print(response)  # [0.001, -0.045, 0.123, ...]
```

**Use Case:** Create embedding for a search query

---

### 2. **2_embedding_openai_docs.py**
**Purpose:** Embed a list of documents

```python
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=1024)

documents = [
    "The first man landed on the moon in 1969.",
    "The first man to walk on the moon was Neil Armstrong."
]

response = embeddings.embed_documents(documents)
print(response)  # List of embeddings [[...], [...]]
```

**Use Case:** Embed multiple documents for comparison

---

### 3. **3_embedding_hf_local.py**
**Purpose:** Local HuggingFace embeddings

```python
from langchain_huggingface import HuggingFaceEndpointEmbeddings

embedding = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
    dimensions=384
)

documents = [...]
response = embedding.embed_documents(documents)
```

**Pros:**
- No API calls
- Private
- Free
- Good quality

---

### 4. **4_document_similarity.py**
**Purpose:** Find similar documents

```python
from langchain_openai import OpenAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

documents = [
    "Virat Kohli is an Indian cricketer",
    "MS Dhoni is a former Indian captain",
    "Sachin Tendulkar is the God of Cricket",
    # ...
]

query = "Who is the best Indian cricketer?"

# Embed documents and query
doc_embeddings = embeddings.embed_documents(documents)
query_embedding = embeddings(query)

# Calculate similarity
scores = cosine_similarity([query_embedding], doc_embeddings)[0]

# Find most similar
index = np.argmax(scores)
print(f"Most similar: {documents[index]}")
print(f"Similarity score: {scores[index]}")
```

**Output:**
```
Most similar: Virat Kohli is an Indian cricketer
Similarity score: 0.85
```

---

## 📊 Embedding Models Comparison

| Model | Provider | Dimensions | Cost | Speed | Quality |
|-------|----------|-----------|------|-------|---------|
| text-embedding-3-small | OpenAI | 1536 | $$ | Fast | High |
| text-embedding-3-large | OpenAI | 3072 | $$$ | Medium | Very High |
| all-MiniLM-L6-v2 | HF | 384 | Free | Very Fast | Medium |
| all-mpnet-base-v2 | HF | 768 | Free | Fast | High |

---

## 🎯 Embedding Use Cases

### 1. Semantic Search
```python
# Find documents similar to query
query_embedding = embeddings(query)
doc_scores = cosine_similarity([query_embedding], doc_embeddings)
```

### 2. Document Clustering
```python
# Group similar documents together
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=5)
clusters = kmeans.fit_predict(doc_embeddings)
```

### 3. Duplicate Detection
```python
# Find identical/similar documents
scores = cosine_similarity(doc_embeddings)
```

### 4. Recommendation Systems
```python
# Find related items
user_embedding = embeddings(user_profile)
item_similarities = cosine_similarity([user_embedding], item_embeddings)
```

---

## 🚀 Complete Workflow Example

```python
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# 1. Create embeddings for documents
embeddings_model = OpenAIEmbeddings()
documents = ["...", "...", "..."]
doc_embeddings = embeddings_model.embed_documents(documents)

# 2. Find similar documents to query
query = "What is machine learning?"
query_embedding = embeddings_model(query)
scores = cosine_similarity([query_embedding], doc_embeddings)[0]
top_doc_idx = np.argmax(scores)
similar_doc = documents[top_doc_idx]

# 3. Generate response using similar document
chat_model = ChatOpenAI(temperature=0.7)
prompt = PromptTemplate(
    template="Answer based on: {doc}\nQuestion: {query}",
    input_variables=["doc", "query"]
)
chain = prompt | chat_model | StrOutputParser()
response = chain.invoke({"doc": similar_doc, "query": query})
```

---

## 💡 Best Practices

1. **Choose Right Model for Task:**
   - Simple questions → GPT-3.5 or Gemini
   - Complex reasoning → GPT-4
   - Local/private → HuggingFace local
   - Budget → Google Gemini free

2. **Temperature Settings:**
   - 0.0 - Deterministic (facts, math)
   - 0.3-0.7 - Balanced (most tasks)
   - 0.9+ - Creative (writing, brainstorming)

3. **For Embeddings:**
   - Use same model for all embeddings
   - Match embedding dimensions
   - Cache embeddings if reusing

4. **Cost Optimization:**
   - Use cheaper models when appropriate
   - Cache repeated queries
   - Monitor token usage
   - Consider local models for high-volume

5. **Error Handling:**
```python
from tenacity import retry
from tenacity import stop_after_attempt

@retry(stop=stop_after_attempt(3))
def call_model(prompt):
    return model.invoke(prompt)
```

---

## 🔗 Related Topics

- **Prompts/** - Craft better prompts for models
- **Chains/** - Combine models with other components
- **Output-Parser/** - Handle model responses
- **Text-Splitter/** - Process documents before embedding

---

## 📚 Quick Reference

### Initialize Different Models

```python
# OpenAI Chat
from langchain_openai import ChatOpenAI
model = ChatOpenAI(model="gpt-3.5-turbo")

# Google Gemini
from langchain_google_genai import ChatGoogleGenerativeAI
model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# Anthropic Claude
from langchain_anthropic import ChatAnthropic
model = ChatAnthropic(model="claude-2")

# HuggingFace
from langchain_huggingface import HuggingFaceEndpoint
model = HuggingFaceEndpoint(model="google/flan-t5-xl")

# OpenAI Embeddings
from langchain_openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()
```

---

**Ready to choose your model and start building? Start with 1_chatmodel_google.py to use the free tier! 🚀**

# 🎓 LangChain Learning Path & Quick Guide

A structured guide to master LangChain in progressive steps with clear milestones.

---

## 📋 Learning Timeline

### **Week 1: Foundation (Basics)**
**Goal:** Understand core LangChain concepts

#### Day 1-2: Setup & First Program
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Create `.env` file with API keys
- [ ] Run: `python Prompts/prompt_template.py`
- **Concept:** Prompts are templates with variables

#### Day 3-4: Messages & Models
- [ ] Study: [Prompts/README.md](./Prompts/README.md)
- [ ] Run: `python Prompts/message.py`
- [ ] Run: `python Models/Chat\ Models/1_chatmodel_google.py`
- **Concept:** Models process messages and return responses

#### Day 5-7: Your First Chain
- [ ] Study: [Chains/README.md](./Chains/README.md)
- [ ] Run: `python Chains/simple_chain.py`
- [ ] Create your own simple chain (5 min exercise)
- **Concept:** Chains = Prompt → Model → Parser (pipe operator |)

**Checkpoint:** You can create a simple prompt-model chain

---

### **Week 2: Core Workflows (Intermediate)**
**Goal:** Build multi-step applications

#### Day 8-9: Sequential Chains
- [ ] Study: Sequential chain in [Chains/README.md](./Chains/README.md)
- [ ] Run: `python Chains/sequential_chain.py`
- [ ] Modify to create 3-step chain
- **Concept:** Output of one step becomes input to next

#### Day 10-11: Parsing Outputs
- [ ] Study: [Output-Parser/README.md](./Output-Parser/README.md)
- [ ] Run: `python Output-Parser/str_output_parser.py`
- [ ] Run: `python Output-Parser/json_output_parser.py`
- **Concept:** Parse LLM responses into strings, JSON, Pydantic objects

#### Day 12-14: Loading Real Data
- [ ] Study: [Document-Loaders/README.md](./Document-Loaders/README.md)
- [ ] Run: `python Document-Loaders/text_loader.py`
- [ ] Run: `python Document-Loaders/pdf_loader.py`
- [ ] Create chain that loads and processes a text file
- **Concept:** Load documents from various sources

**Checkpoint:** You can process real documents with chains

---

### **Week 3: Advanced Patterns (Advanced)**
**Goal:** Build sophisticated workflows

#### Day 15-16: Parallel Chains
- [ ] Study: Parallel chain in [Chains/README.md](./Chains/README.md)
- [ ] Run: `python Chains/parallel_chain.py`
- [ ] Create parallel comparison chain
- **Concept:** Run multiple chains simultaneously

#### Day 17-18: Conditional Logic
- [ ] Study: Conditional chain in [Chains/README.md](./Chains/README.md)
- [ ] Run: `python Chains/conditional_chain.py`
- [ ] Create branching workflow
- **Concept:** Route to different paths based on conditions

#### Day 19-21: Text Splitting & Embeddings
- [ ] Study: [Text-Splitter/README.md](./Text-Splitter/README.md)
- [ ] Run: `python Text-Splitter/legth_based.py`
- [ ] Run: `python Models/Embedding\ Models/4_docuement_similarity.py`
- [ ] Create semantic search pipeline
- **Concept:** Split documents, create embeddings, find similar documents

**Checkpoint:** You can build RAG-ready pipelines

---

### **Week 4: Production & Advanced (Expert)**
**Goal:** Build production-ready applications

#### Day 22-23: Runnables
- [ ] Study: [Runnables/README.md](./Runnables/README.md)
- [ ] Run: `python Runnables/runnable_lambda.py`
- [ ] Run: `python Runnables/runnable_branch.py`
- **Concept:** Advanced runnable patterns for complex workflows

#### Day 24: Structured Output
- [ ] Study: [Strctured-Output/README.md](./Strctured-Output/README.md)
- [ ] Run: `python Strctured-Output/pydentic_demo.py`
- [ ] Run: `python Strctured-Output/with_structured_output_pydantic.py`
- **Concept:** Enforce schemas on LLM outputs with validation

#### Day 25-26: Multiple LLM Providers
- [ ] Try OpenAI: `python Models/Chat\ Models/1_chatmodel_openai.py`
- [ ] Try Anthropic: `python Models/Chat\ Models/2_chatmodel_anthropic.py`
- [ ] Try HuggingFace: `python Models/Chat\ Models/4_chatmodel_hf_api.py`
- **Concept:** LangChain abstracts multiple providers

#### Day 27-28: MCP & Integration
- [ ] Study: [MCP-Client/README.md](./MCP-Client/README.md)
- [ ] Run: `python MCP-Client/client1.py` (if servers available)
- [ ] Build custom integration
- **Concept:** Connect external tools and services

**Checkpoint:** You can build production-ready applications!

---

## 🎯 Quick Start Paths

### Path A: "I want to build a Chatbot"
1. **Prompts/** - Learn prompt templates
2. **Models/Chat Models/** - Initialize chat model
3. **Prompts/chatbot.py** - Study the chatbot
4. **Modify:** Make your own chatbot with conversation history
5. **Optional:** Add Prompts/temperature.py for personality tuning

### Path B: "I want to build a RAG System"
1. **Document-Loaders/** - Load documents
2. **Text-Splitter/** - Split into chunks
3. **Models/Embedding Models/** - Create embeddings
4. **Models/Embedding Models/4_docuement_similarity.py** - Semantic search
5. **Chains/** - Build retrieval chain

### Path C: "I want to understand Advanced Chains"
1. **Chains/simple_chain.py** - Foundation
2. **Chains/sequential_chain.py** - Multiple steps
3. **Chains/parallel_chain.py** - Concurrent execution
4. **Chains/conditional_chain.py** - Smart routing
5. **Runnables/** - Advanced patterns

### Path D: "I want to extract structured data"
1. **Output-Parser/json_output_parser.py** - JSON format
2. **Output-Parser/pydantic_output_parser.py** - Validation
3. **Strctured-Output/with_structured_output_pydantic.py** - Schema enforcement

---

## 📚 Topic Dependency Map

```
START HERE
    ↓
Prompts (Foundation) ← Required for everything
    ↓
Models (Core Intelligence) ← Required for everything
    ↓
    ├─→ Output-Parser (Parse responses)
    │       ↓
    │   Chains (Workflows)
    │       ├─→ Simple chains
    │       ├─→ Sequential chains
    │       ├─→ Parallel chains
    │       └─→ Conditional chains
    │
    ├─→ Document-Loaders (Load data)
    │       ↓
    │   Text-Splitter (Chunk data)
    │       ↓
    │   Models/Embedding (Vector search)
    │       ↓
    │   Semantic Search (RAG)
    │
    ├─→ Strctured-Output (Validate outputs)
    │
    ├─→ Runnables (Advanced patterns)
    │
    └─→ MCP-Client (External tools)
```

---

## 🚀 Project Ideas by Level

### Beginner Projects
1. **Smart Q&A Bot** - Answer questions about a topic
2. **Text Summarizer** - Summarize any text
3. **Sentiment Analyzer** - Classify text sentiment
4. **Code Explainer** - Explain code snippets

### Intermediate Projects
1. **Document Q&A** - Ask questions about PDF
2. **Multi-turn Chatbot** - Remember conversation history
3. **Email Classifier** - Route emails to categories
4. **Content Generator** - Create content from prompts

### Advanced Projects
1. **RAG System** - Semantic search + QA
2. **Multi-Agent System** - Agents collaborate
3. **Custom Tool Integration** - Connect external APIs
4. **Production Chatbot** - Full-featured with UI

---

## ⚡ 5-Minute Quick Start

### Option 1: Simple Q&A
```python
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.7)
prompt = PromptTemplate(
    template="Explain {topic} in simple terms",
    input_variables=["topic"]
)

chain = prompt | model
result = chain.invoke({"topic": "machine learning"})
print(result.content)
```

### Option 2: Load and Summarize Text
```python
from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

loader = TextLoader("file.txt")
docs = loader.load()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")
prompt = PromptTemplate(
    template="Summarize:\n{text}",
    input_variables=["text"]
)

chain = prompt | model
result = chain.invoke({"text": docs[0].page_content})
print(result.content)
```

### Option 3: Extract Structured Data
```python
from pydantic import BaseModel, Field
from typing import List
from langchain_google_genai import ChatGoogleGenerativeAI

class Review(BaseModel):
    rating: int = Field(ge=1, le=5)
    pros: List[str]
    cons: List[str]

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")
structured = model.with_structured_output(Review)

result = structured.invoke("Great product but too expensive...")
print(result.rating, result.pros, result.cons)
```

---

## 🔍 Debugging Checklist

When something doesn't work:

- [ ] **Api Key Issue?** Check `.env` file
- [ ] **Import Error?** Reinstall: `pip install -r requirements.txt`
- [ ] **Network Error?** Check internet connection
- [ ] **API Limits?** Wait or check rate limits
- [ ] **Output Format Wrong?** Check output parser
- [ ] **Chain Logic Broken?** Use `.get_graph().print_ascii()`
- [ ] **Model Response Bad?** Improve prompt
- [ ] **Token Limit?** Reduce input size or split document

---

## 💡 Pro Tips

1. **Always Start Simple**
   - Get basic prompt working first
   - Add complexity gradually

2. **Test Components Independently**
   - Test prompt alone
   - Test model alone
   - Then chain together

3. **Use Print Statements**
   - Print intermediate results
   - Verify data flow

4. **Read Error Messages**
   - They're usually very helpful
   - Follow suggestions

5. **Check Documentation**
   - Official: https://python.langchain.com/
   - GitHub: https://github.com/langchain-ai/langchain

6. **Start with Google Gemini**
   - Free tier available
   - Good quality
   - Easy to switch providers later

---

## 🛠️ Common Patterns

### Pattern 1: Prompt → Model → Parse
```python
prompt = PromptTemplate(template="...", input_variables=["var"])
model = ChatGoogleGenerativeAI(...)
parser = StrOutputParser()
chain = prompt | model | parser
result = chain.invoke({...})
```

### Pattern 2: Load → Split → Embed → Search
```python
loader = TextLoader(file)
docs = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=500)
chunks = splitter.split_documents(docs)
embeddings = OpenAIEmbeddings()
embedded = embeddings.embed_documents([c.page_content for c in chunks])
# Now search...
```

### Pattern 3: Sequential Steps
```python
chain = (
    step1_prompt | model | parser |
    step2_prompt | model | parser |
    step3_prompt | model | parser
)
```

### Pattern 4: Parallel Processing
```python
parallel = RunnableParallel({
    "analysis_a": chain_a,
    "analysis_b": chain_b
})
result = parallel.invoke(input)
# Result has both analyses
```

---

## 📊 Model Selection Guide

**Question:** What model should I use?

- **Learning & Experimentation** → Google Gemini (free)
- **Production & Quality** → OpenAI GPT-4
- **Writing & Analysis** → Anthropic Claude
- **Budget-Conscious** → Google Gemini or HuggingFace
- **Privacy Critical** → HuggingFace Local
- **Speed Critical** → Gemini Flash

---

## 🎓 Mastery Checklist

After completing this learning path, you should be able to:

### Foundation
- [ ] Create prompt templates with variables
- [ ] Initialize different LLM providers
- [ ] Understand message types and roles
- [ ] Handle API keys and environment variables

### Chains
- [ ] Build simple chains
- [ ] Chain multiple operations sequentially
- [ ] Run operations in parallel
- [ ] Route based on conditions

### Data Processing
- [ ] Load documents (PDF, CSV, text, web)
- [ ] Split documents intelligently
- [ ] Create embeddings
- [ ] Perform semantic search

### Output Handling
- [ ] Parse LLM output to strings
- [ ] Parse to JSON format
- [ ] Validate with Pydantic
- [ ] Enforce schemas

### Advanced
- [ ] Use Runnables effectively
- [ ] Build complex workflows
- [ ] Integrate external tools (MCP)
- [ ] Build production applications

---

## 🚀 Next Steps After This Course

1. **Build a Project** - Apply what you learned
2. **Read Official Docs** - Deeper understanding
3. **Explore Ecosystem** - Vector DBs, agents, etc.
4. **Join Community** - Discord, forums, GitHub
5. **Stay Updated** - LangChain evolves quickly

---

## 📞 Getting Help

1. **Official Documentation:** https://python.langchain.com/
2. **GitHub Issues:** https://github.com/langchain-ai/langchain
3. **Discord Community:** https://discord.gg/6adMQxSpJS
4. **Stack Overflow:** Tag with `langchain`
5. **GitHub Discussions:** langchain repository

---

## 🎉 Congratulations!

You now have a complete learning path for LangChain mastery. Start with Week 1 and progress through each week. Each folder has a detailed README with theory and examples.

**Remember:** The best way to learn is by doing. Run the examples, modify them, and experiment!

---

**Happy Learning! 🚀**

*Last Updated: 2024 | For the latest updates, check the official documentation*

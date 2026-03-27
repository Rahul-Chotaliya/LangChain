# LangChain Complete Learning Guide 🚀

A comprehensive learning repository covering all essential LangChain concepts, from basic chains to advanced workflows with multiple LLM providers.

## 📚 Table of Contents

1. [Overview](#overview)
2. [Project Structure](#project-structure)
3. [Prerequisites](#prerequisites)
4. [Installation & Setup](#installation--setup)
5. [Learning Path](#learning-path)
6. [Folder Guide](#folder-guide)
7. [Key Concepts](#key-concepts)
8. [Getting Started](#getting-started)

---

## 🎯 Overview

This repository is designed to teach **LangChain** from scratch through practical, well-organized examples. It covers:

- **LLM Integrations** - Connect with OpenAI, Google Gemini, Anthropic, HuggingFace
- **Prompt Engineering** - Template creation, message handling, dynamic prompts
- **Chains** - Sequential, parallel, and conditional workflows
- **Document Processing** - Load and parse PDFs, CSV, text files, web content
- **Output Parsing** - Extract structured data from LLM responses
- **Text Splitting** - Smart document chunking for RAG systems
- **Embeddings** - Create vector representations for semantic search
- **Model Context Protocol (MCP)** - Advanced tool integration

---

## 📂 Project Structure

```
LangChain/
├── Chains/                    # Chain implementations (simple, sequential, parallel, conditional)
├── Document-Loaders/         # Load documents from various sources (PDF, CSV, Web, Text)
├── Models/                    # LLM, Chat Models, and Embedding Models
│   ├── Chat Models/          # Integration with OpenAI, Anthropic, Google, HuggingFace
│   ├── LLMs/                 # Large Language Model basics
│   └── Embedding Models/     # Vector embeddings and similarity search
├── Output-Parser/            # Parse LLM outputs (String, JSON, Pydantic)
├── Prompts/                  # Prompt templates, messages, and chatbots
├── Runnables/                # Advanced runnable patterns (Lambda, Branch, Parallel)
├── Strctured-Output/         # Structured output schemas (Pydantic, TypedDict, JSON)
├── Text-Splitter/            # Text chunking strategies for documents
├── MCP-Client/               # Model Context Protocol integration
└── requirements.txt          # Project dependencies

```

---

## 🔧 Prerequisites

- **Python 3.9+**
- **pip** or **conda** for package management
- **API Keys** for LLM providers (optional based on which providers you use)
- **Basic Python knowledge** - Variables, functions, async concepts

### API Keys Required (Optional)

Depending on which models you want to use:
- **OpenAI** - https://platform.openai.com/api-keys
- **Google Gemini** - https://aistudio.google.com/app/apikey
- **Anthropic (Claude)** - https://console.anthropic.com/
- **HuggingFace** - https://huggingface.co/settings/tokens

---

## 📦 Installation & Setup

### 1. Clone/Download the Repository
```bash
cd "your-path/LangChain"
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables
Create a `.env` file in the root directory:
```env
# OpenAI
OPENAI_API_KEY=your_openai_key_here

# Google Gemini
GOOGLE_API_KEY=your_google_key_here

# Anthropic
ANTHROPIC_API_KEY=your_anthropic_key_here

# HuggingFace
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here
```

---

## 🎓 Learning Path

### Level 1: Foundation (Start Here)
1. **Prompts/** - Learn basic prompt templates
   - `prompt_template.py` - Basic templates
   - `message.py` - Message types
   - `chhat_prompt_template.py` - Chat templates

2. **Models/Chat Models/** - Connect to LLMs
   - `1_chatmodel_openai.py` - OpenAI basics
   - `2_chatmodel_google.py` - Google Gemini
   - `2_chatmodel_anthropic.py` - Claude

### Level 2: Core Concepts
3. **Chains/** - Build your first workflows
   - `simple_chain.py` - Single chain
   - `sequential_chain.py` - Chained operations
   - `parallel_chain.py` - Parallel execution

4. **Output-Parser/** - Extract structured data
   - `str_output_parser.py` - Simple strings
   - `json_output_parser.py` - JSON format
   - `pydantic_output_parser.py` - Validated objects

### Level 3: Advanced
5. **Document-Loaders/** - Work with real data
   - Start with `text_loader.py`
   - Progress to `pdf_loader.py`
   - Then `csv_loader.py` and `webbase_loader.py`

6. **Text-Splitter/** - Process large documents
   - `legth_based.py` - Simple chunking
   - `semantic_meaning_based.py` - Intelligent chunking

7. **Runnables/** - Powerful abstractions
   - `runnable_lambda.py` - Custom functions
   - `runnable_parallel.py` - Parallel workflows
   - `runnable_branch.py` - Conditional logic

### Level 4: Expert
8. **Strctured-Output/** - Complex schemas
   - `pydentic_demo.py` - Data validation
   - `with_structured_output_pydantic.py` - Schema enforcement

9. **Models/Embedding Models/** - Semantic search
   - `1_embedding_openai_query.py` - Query embeddings
   - `4_docuement_similarity.py` - Similarity search

10. **MCP-Client/** - Advanced integrations
    - `client1.py` - Basic MCP setup
    - `client2.py` - Streamlit MCP interface

---

## 📖 Folder Guide

### [🔗 Chains/](./Chains/README.md)
Learn how to combine prompts and models into workflows:
- **Simple Chains** - Single operation
- **Sequential Chains** - Step-by-step processing
- **Parallel Chains** - Multiple concurrent operations
- **Conditional Chains** - Branching logic

### [📄 Document-Loaders/](./Document-Loaders/README.md)
Load documents from various sources:
- PDF files with `PyPDFLoader`
- CSV data with `CSVLoader`
- Text files with `TextLoader`
- Web pages with `WebBaseLoader`
- Directory of files with `DirectoryLoader`

### [🤖 Models/](./Models/README.md)
Different types of models for various tasks:
- **Chat Models** - Conversational AI
- **LLMs** - Large Language Models
- **Embeddings** - Vector representations

### [📊 Output-Parser/](./Output-Parser/README.md)
Parse and structure LLM outputs:
- String parsing
- JSON parsing
- Pydantic validation
- Custom formats

### [✍️ Prompts/](./Prompts/README.md)
Master prompt engineering:
- Prompt templates with variables
- Chat templates for conversations
- Message types and history
- Temperature and randomness
- Interactive UI with Streamlit

### [⚙️ Runnables/](./Runnables/README.md)
Advanced execution patterns:
- Lambda functions for custom logic
- Branch for conditional routing
- Parallel for concurrent execution
- Passthrough for data passing
- Sequence for complex workflows

### [🏗️ Strctured-Output/](./Strctured-Output/README.md)
Advanced structured output schemas:
- Pydantic models
- TypedDict annotations
- JSON schema validation
- Field descriptions

### [✂️ Text-Splitter/](./Text-Splitter/README.md)
Smart text chunking strategies:
- Length-based splitting
- Recursive splitting
- Language-aware splitting (Python, Markdown)
- Semantic splitting

### [🔗 MCP-Client/](./MCP-Client/README.md)
Model Context Protocol integration:
- Multi-server setup
- Tool binding with LLMs
- Async operations
- Streamlit UI integration

---

## 🔑 Key Concepts Explained

### LangChain Core Components

**1. LLMs (Large Language Models)**
- Text input → Text output
- Examples: GPT-3.5, Gemini, Claude
- Use for: General text generation

**2. Chat Models**
- Message history aware
- Better for conversations
- Examples: GPT-4, Gemini Pro
- Use for: Chatbots, multi-turn conversations

**3. Prompts**
- Templates with variables
- Define input/output format
- Examples: "Explain {topic} in {language}"

**4. Chains**
- Combine prompts, models, and parsers
- Syntax: `prompt | model | parser`
- Example: `template | llm | output_parser`

**5. Output Parsers**
- Structure raw LLM output
- Types: String, JSON, Pydantic
- Example: Extract structured data from text

**6. Embeddings**
- Convert text to vectors
- Enable semantic search
- Examples: OpenAI embeddings, HuggingFace
- Use for: Similarity search, RAG systems

**7. Document Loaders**
- Load docs from sources
- Parse different formats
- Examples: PDF, CSV, Web, Text

**8. Text Splitters**
- Break large documents into chunks
- Preserve semantic meaning
- Use for: RAG, document processing

**9. Runnables**
- Abstraction for any component
- Composable operations
- Examples: Lambda, Branch, Parallel

---

## 🚀 Getting Started

### Quick Start - Your First LangChain App

1. **Create a simple script:**
```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# Initialize model
model = ChatOpenAI(temperature=0.7)

# Create prompt
prompt = PromptTemplate(
    template="Explain {concept} in simple terms",
    input_variables=["concept"]
)

# Create chain
chain = prompt | model

# Run
result = chain.invoke({"concept": "machine learning"})
print(result.content)
```

2. **Run the script:**
```bash
python your_script.py
```

### Try Existing Examples

```bash
# Example 1: Simple prompt
python Prompts/prompt_template.py

# Example 2: Simple chain
python Chains/simple_chain.py

# Example 3: Document loading
python Document-Loaders/text_loader.py

# Example 4: Output parsing
python Output-Parser/str_output_parser.py
```

---

## 💡 Pro Tips

1. **Start Simple** - Begin with basic prompts before complex chains
2. **Test Incrementally** - Build and test one component at a time
3. **Use Print Statements** - Debug chains by printing intermediate results
4. **Set Temperature Wisely** - Lower (0.0-0.3) for factual, higher (0.7-1.0) for creative
5. **Handle Errors** - Always use try-except for API calls
6. **Read Docs** - Visit https://python.langchain.com/ for detailed docs

---

## 📚 Additional Resources

- **Official Docs** - https://python.langchain.com/
- **API Reference** - https://api.python.langchain.com/
- **GitHub** - https://github.com/langchain-ai/langchain
- **Discord Community** - https://discord.gg/6adMQxSpJS

---

## ⚠️ Common Issues & Solutions

### Issue: `ImportError: No module named 'langchain'`
**Solution:** Run `pip install -r requirements.txt`

### Issue: `API Key not found`
**Solution:** Create `.env` file with your API keys

### Issue: Async errors in scripts
**Solution:** Use `asyncio.run()` for async functions

### Issue: Rate limiting errors
**Solution:** Add delays between API calls, use exponential backoff

---

## 📝 Notes

- All examples use Google Gemini by default (easily switchable)
- Each folder has its own detailed README
- Code is well-commented for learning
- Most examples are self-contained and can run independently

---

## 🎯 What You'll Learn

After going through this repository, you'll understand:

✅ How LangChain simplifies LLM integration
✅ How to build production-ready chains
✅ How to work with multiple LLM providers
✅ How to parse and structure LLM outputs
✅ How to load and process documents
✅ How to implement semantic search with embeddings
✅ How to build interactive chatbots
✅ How to handle complex workflows with advanced runnables

---

**Happy Learning! 🎓**

*For questions or improvements, feel free to experiment with the examples and extend them further.*

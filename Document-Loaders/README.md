# Document Loaders 📄

Learn how to load documents from various sources and prepare them for processing with LangChain.

## 🎯 Overview

Document Loaders are the entry points for getting external information into your LangChain applications. They handle:

- **Loading** - Retrieve files from sources
- **Parsing** - Extract content in usable format
- **Structuring** - Convert to LangChain Document format
- **Metadata** - Capture source information

Every loaded document becomes a `Document` object with:
- `page_content` - The actual text
- `metadata` - Source info, timestamps, etc.

---

## 📂 Files in This Folder

### 1. **text_loader.py**
**What it does:** Loads text files and processes their content

**Use Cases:**
- Loading `.txt` files
- Reading configuration files
- Processing plain text data

**Key Learning Points:**
```python
from langchain_community.document_loaders import TextLoader

loader = TextLoader(file_path="Document-Loaders/cricket.txt", encoding="utf-8")
docs = loader.load()

# Output: List of Document objects
# Each document has:
# - page_content: The file text
# - metadata: {"source": "path/to/file"}
```

**Example Workflow:**
```
cricket.txt (poem about cricket)
    ↓
TextLoader
    ↓
Document with page_content (full poem)
    ↓
Chain processes it (summarization, analysis)
```

**When to Use:**
- Simple text files
- Configuration data
- Log files
- Raw text content

---

### 2. **pdf_loader.py**
**What it does:** Extracts text from PDF files with page information

**Use Cases:**
- Research papers
- Documents
- Books in PDF format
- Reports

**Key Learning Points:**
```python
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(file_path="path/to/document.pdf")
docs = loader.load()

# Each page becomes a separate Document
# Metadata includes page number
```

**Document Structure:**
```python
docs[0].page_content  # Text from first page
docs[0].metadata  # {"source": "...", "page": 0}
```

**Important Note:** Each page of a PDF becomes a separate document in the list.

**When to Use:**
- PDF documents
- Research papers
- Legal documents
- Academic materials

---

### 3. **csv_loader.py**
**What it does:** Loads CSV files and converts them to documents

**Use Cases:**
- Tabular data
- Datasets
- Structured information
- Data analysis

**Key Learning Points:**
```python
from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path="Document-Loaders/Social_Network_Ads.csv",
    encoding="utf-8"
)
docs = loader.load()

# Each row becomes a Document
# page_content contains formatted row data
```

**Example Output:**
```
Document 1: "User ID: 15624510, Gender: Male, Age: 19, ..."
Document 2: "User ID: 15810944, Gender: Male, Age: 35, ..."
```

**When to Use:**
- CSV datasets
- Databases exported to CSV
- Spreadsheet data
- Tabular information

---

### 4. **webbase_loader.py**
**What it does:** Scrapes and loads content from web pages

**Use Cases:**
- Web pages
- Online articles
- Real-time information
- Product pages

**Key Learning Points:**
```python
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://example.com")
docs = loader.load()

# Extracts text from HTML
# Handles parsing automatically
```

**Example Workflow:**
```
URL → WebBaseLoader
    ↓
Fetch HTML
    ↓
Extract text content
    ↓
Create Document
    ↓
Pass to chain for analysis
```

**Important Considerations:**
- Requires internet connection
- Respects robots.txt
- Can timeout on slow sites
- May need headers for some sites

**Practical Example:**
```python
# Extract product information from website
loader = WebBaseLoader("https://www.flipkart.com/product-page")
docs = loader.load()

# Then analyze with chain
prompt = PromptTemplate(
    template="What is the price of the product in this content: {content}",
    input_variables=["content"]
)
```

**When to Use:**
- Real-time web data
- News articles
- Product information
- Online documentation
- Wikipedia pages

---

### 5. **directory_loader.py**
**What it does:** Loads multiple files from a directory

**Use Cases:**
- Batch processing
- Working with file collections
- Processing multiple PDFs
- Reading directory structures

**Key Learning Points:**
```python
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path="Document-Loaders/books",  # Directory path
    glob="*.pdf",                     # File pattern
    loader_cls=PyPDFLoader            # Which loader to use
)

docs = loader.lazy_load()  # Generator for memory efficiency
```

**Important Features:**
- `glob` patterns for file filtering
- `lazy_load()` returns a generator (memory efficient)
- `load()` loads everything into memory
- Supports different file types

**Example Use Cases:**
```python
# Load all PDFs from books directory
pdf_loader = DirectoryLoader(
    path="./documents/books",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

# Load all text files
txt_loader = DirectoryLoader(
    path="./documents/text",
    glob="*.txt",
    loader_cls=TextLoader
)
```

**When to Use:**
- Multiple files in a folder
- Batch document processing
- Building knowledge bases
- Processing document collections

---

## 🔄 Document Structure

All loaders return `Document` objects:

```python
class Document:
    page_content: str      # The actual text content
    metadata: dict         # Information about the document
```

**Example Metadata:**
```python
{
    "source": "/path/to/file.pdf",
    "page": 0,
    "file_type": "pdf"
}
```

---

## 🎯 Loader Comparison

| Loader | File Type | Use Case | Metadata | Speed |
|--------|-----------|----------|----------|-------|
| **TextLoader** | `.txt`, `.md` | Text files | Source, encoding | Fast |
| **PyPDFLoader** | `.pdf` | PDFs | Source, page number | Medium |
| **CSVLoader** | `.csv` | Tabular data | Source, row index | Fast |
| **WebBaseLoader** | URLs | Web pages | URL, title | Slow (network) |
| **DirectoryLoader** | Any (via loader_cls) | Multiple files | Per-file metadata | Variable |

---

## 📖 Common Loader Patterns

### Pattern 1: Single File Loading
```python
loader = TextLoader("file.txt")
docs = loader.load()
print(docs[0].page_content)
```

### Pattern 2: Multiple File Loading
```python
loader = DirectoryLoader("./documents", glob="*.pdf", loader_cls=PyPDFLoader)
docs = loader.load()
```

### Pattern 3: Lazy Loading (Memory Efficient)
```python
loader = DirectoryLoader("./documents", glob="*.txt", loader_cls=TextLoader)
for doc in loader.lazy_load():  # Process one at a time
    process(doc)
```

### Pattern 4: With Chains (Complete Workflow)
```python
# Load → Parse → Analyze
loader = TextLoader("article.txt")
docs = loader.load()

chain = prompt_template | model | parser
result = chain.invoke({"content": docs[0].page_content})
```

---

## 🚀 Advanced Features

### 1. Filtering Documents
```python
# Load only certain files
loader = DirectoryLoader(
    path="./documents",
    glob="*.pdf",  # Only PDFs
    loader_cls=PyPDFLoader
)
```

### 2. Processing While Loading
```python
docs = loader.load()

# Filter by length
long_docs = [d for d in docs if len(d.page_content) > 100]

# Add custom metadata
for doc in docs:
    doc.metadata["custom_field"] = "value"
```

### 3. Error Handling
```python
try:
    loader = WebBaseLoader("https://example.com")
    docs = loader.load()
except Exception as e:
    print(f"Failed to load: {e}")
```

### 4. Lazy Loading for Large Datasets
```python
# Use generator to avoid loading everything at once
loader = DirectoryLoader("./large_documents", glob="*.pdf")
for doc in loader.lazy_load():
    # Process one document at a time
    process(doc)
    # Memory usage stays constant
```

---

## 💡 Real-World Examples

### Example 1: Analyze a PDF Report
```python
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate

loader = PyPDFLoader("report.pdf")
docs = loader.load()

# Create chain to analyze report
prompt = PromptTemplate(
    template="Summarize the key findings: {content}",
    input_variables=["content"]
)
chain = prompt | model | parser

for doc in docs:
    summary = chain.invoke({"content": doc.page_content})
    print(f"Page {doc.metadata['page']}: {summary}")
```

### Example 2: Process Web Content
```python
from langchain_community.document_loaders import WebBaseLoader

url = "https://www.example.com/article"
loader = WebBaseLoader(url)
docs = loader.load()

# Extract information from web content
content = docs[0].page_content
# Now use with chains for analysis
```

### Example 3: Batch Process CSV
```python
from langchain_community.document_loaders import CSVLoader

loader = CSVLoader("data.csv")
docs = loader.load()

# Process each row
for doc in docs:
    # Each document is one row of CSV
    analyze(doc.page_content)
```

---

## 🛠️ Best Practices

1. **Choose Right Loader** - Use appropriate loader for file type
2. **Handle Errors** - Web loaders can fail, add error handling
3. **Use Lazy Loading** - For large document collections
4. **Preserve Metadata** - Keep source info for traceability
5. **Test First** - Load and inspect small samples first
6. **Memory Management** - Don't load entire datasets into memory
7. **Encoding** - Specify correct encoding for text files

---

## 🔗 Next Steps

After loading documents:
1. **Text Splitter/** - Split large documents into chunks
2. **Chains/** - Process documents with chains
3. **Output-Parser/** - Extract structured data from documents
4. **Models/Embedding Models/** - Create embeddings for semantic search

---

## 📚 Loader Reference

```python
# Common imports
from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader,
    CSVLoader,
    WebBaseLoader,
    DirectoryLoader,
    JSONLoader,
    UnstructuredMarkdownLoader
)
```

---

## ❓ Common Questions

**Q: Can I load a file that's not in the working directory?**
A: Yes, use absolute paths or relative paths that work from your script location

**Q: Why is WebBaseLoader slow?**
A: It needs to fetch content from the internet. Network latency is unavoidable.

**Q: Can I load multiple file types at once?**
A: Use DirectoryLoader with appropriate glob patterns, or create multiple loaders

**Q: How do I handle large files?**
A: Use lazy_load() to process documents one at a time instead of loading all at once

**Q: What if a file fails to load?**
A: Add try-except blocks and handle errors gracefully

---

**Ready to load documents and build knowledge-based applications? Start with text_loader.py! 📚**

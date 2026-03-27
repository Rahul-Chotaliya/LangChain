# Text Splitters ✂️

Learn smart text chunking strategies for processing large documents with language models.

## 🎯 Overview

Text splitters break large documents into smaller chunks (chunks are the LLM's working memory limit).

**Why needed?**
- LLMs have token limits (GPT-4: ~8k-128k tokens)
- Processing entire documents may exceed limits
- Need to split intelligently to preserve meaning
- Enable semantic search on large documents

**Basic Formula:**
```
Large Document → Text Splitter → Chunks → Ready for processing
```

---

## 📂 Files in This Folder

### 1. **legth_based.py** (Note: typo - should be "length_based")
**What it does:** Splits documents by character count

**Simplest approach:**
```python
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('document.pdf')
docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=200,      # Each chunk: ~200 characters
    chunk_overlap=0,     # No overlap between chunks
    separator='\n'       # Split on newlines
)

chunks = splitter.split_documents(docs)
```

**Parameters:**
- `chunk_size` - Characters per chunk
- `chunk_overlap` - How much chunks repeat
- `separator` - What character to split on

**Separators (in order of preference):**
1. `"\n\n"` - Paragraph breaks
2. `"\n"` - Line breaks
3. `" "` - Spaces
4. `""` - Characters

**Trade-offs:**
- Small chunks: Lose context
- Large chunks: May exceed limits
- Overlap: More context but redundancy
- No overlap: Risk losing connections

**When to use:**
- Simple text files
- Quick prototyping
- When semantic structure doesn't matter much

**Example Output:**
```
Document: "This is paragraph 1. This is paragraph 2. This is paragraph 3."

With chunk_size=30:
- Chunk 1: "This is paragraph 1. This is"
- Chunk 2: "paragraph 2. This is paragraph"
- Chunk 3: "3."
```

---

### 2. **markdown_splitting.py**
**What it does:** Splits while preserving Markdown structure

**Why special handling?**
Markdown has hierarchical structure (headers, sections). Naive splitting breaks this.

**Example:**
```python
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """
# Project Name: Smart Student Tracker

A simple Python-based project...

## Features

- Add new students
- View student details
- Check if passing
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=100,
    chunk_overlap=0
)

chunks = splitter.create_documents([text])
```

**How It Works:**
- Respects markdown headers
- Keeps sections together
- Maintains hierarchy
- Better context preservation

**Output Preserves:**
- Headers with content
- Section relationships
- Hierarchical structure

**When to use:**
- Markdown files
- Documentation
- Content with structure
- When hierarchy matters

---

### 3. **python_code_splitting.py**
**What it does:** Splits Python code intelligently

**Why special handling?**
Code has syntax meaning. Breaking in wrong place breaks functionality.

**Example:**
```python
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

code = """
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_details(self):
        return self.name
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=100,
    chunk_overlap=0
)

chunks = splitter.create_documents([code])
```

**Respects:**
- Class boundaries
- Function boundaries
- Indentation levels
- Syntax structure

**When to use:**
- Python code analysis
- Code documentation
- RAG on codebases
- Technical documentation

---

### 4. **text_structure_based.py**
**What it does:** Recursive splitting that respects document structure

**Most flexible approach:**
```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Space exploration has led to discoveries. From Moon to Mars...

These missions expanded knowledge and contributed to tech...
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=0,
    separators=["\n\n", "\n", " ", ""]  # Try these in order
)

chunks = splitter.split_text(text)
```

**How It Works:**
1. Try first separator: `"\n\n"`
2. If chunks still too large, try `"\n"`
3. If still too large, try `" "`
4. If still too large, split characters

**Advantages:**
- Intelligent fallback
- Respects structure when possible
- Works for any text type
- Best general-purpose option

**When to use:**
- General text
- Mixed content
- Unknown structure
- Default choice

---

### 5. **semantic_meaning_based.py**
**What it does:** Splits based on semantic meaning (most advanced)

**How It Works:**
Uses embeddings to understand content similarity, splits where meaning changes.

**Example:**
```python
from langchain_experimental.text_splitters import SemanticChunker
from langchain_google_genai.embeddings import GoogleGenAIEmbeddings

splitter = SemanticChunker(
    GoogleGenAIEmbeddings(),
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=3
)

sample = """
Farmers working in fields, soil preparation, planting seeds.
The sun was bright, air smelled of earth.

The Indian Premier League is the biggest cricket league.
People watch matches and cheer for favorite teams.

Terrorism is a danger to peace and safety.
It causes harm and creates fear.
"""

docs = splitter.create_documents([sample])
```

**Key Features:**
- Uses embedding similarity
- Splits at meaning boundaries
- Better semantic preservation
- More compute intensive

**Threshold Types:**
- `"percentile"` - Percentile-based break
- `"standard_deviation"` - Standard deviation based
- `"gradient"` - Gradient-based breaks

**Trade-offs:**
- Pros: Best semantic preservation
- Cons: Slower (needs embeddings), more expensive

**When to use:**
- Semantic search critical
- RAG systems
- When meaning preservation essential
- High-quality output needed

---

## 📊 Splitter Comparison

| Splitter | Type | Semantic Aware | Speed | Cost | Best For |
|----------|------|----------------|-------|------|----------|
| **Length-based** | Character count | No | Very Fast | Free | Simple text |
| **Markdown** | Structure-aware | Partial | Fast | Free | Markdown files |
| **Code** | Language-aware | High | Fast | Free | Source code |
| **Recursive** | Smart fallback | Partial | Fast | Free | General text |
| **Semantic** | Meaning-based | Very High | Slow | $$$ | RAG systems |

---

## 🎯 Choosing the Right Splitter

**Question:** What type of document?
- **Plain text** → Recursive splitter
- **Markdown** → Markdown splitter
- **Python code** → Python code splitter
- **Technical docs** → Recursive or Semantic
- **Any type** → Recursive (safe default)

**Question:** How important is meaning?
- **Not critical** → Length-based
- **Moderately** → Recursive
- **Very important** → Semantic splitter

**Question:** How much compute available?
- **Limited** → Length/Recursive
- **Moderate** → Code/Markdown
- **Plenty** → Semantic

---

## 💡 Practical Guide

### Scenario 1: Process Academic Papers
```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Academic papers have sections
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,  # Larger for dense content
    chunk_overlap=100,  # Overlap for context
    separators=["\n\n", "\n", " ", ""]
)
```

### Scenario 2: Process Documentation
```python
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

# Docs are often markdown
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=500,
    chunk_overlap=50
)
```

### Scenario 3: Build RAG System
```python
from langchain_experimental.text_splitters import SemanticChunker

# Semantic preservation critical for RAG
splitter = SemanticChunker(
    embeddings_model,
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=3
)
```

---

## 🚀 Advanced Techniques

### Technique 1: Hybrid Splitting
```python
# First split by structure
recursive_split = recursive_splitter.split_documents(docs)

# Then split large ones with semantic splitter
final_chunks = []
for chunk in recursive_split:
    if len(chunk.page_content) > 2000:
        semantic_chunks = semantic_splitter.split_documents([chunk])
        final_chunks.extend(semantic_chunks)
    else:
        final_chunks.append(chunk)
```

### Technique 2: Metadata Preservation
```python
splitter = RecursiveCharacterTextSplitter(...)
chunks = splitter.split_documents(docs)

# Chunks preserve original metadata (source, page, etc.)
for chunk in chunks:
    print(chunk.metadata)  # {'source': 'file.pdf', 'page': 0}
```

### Technique 3: Custom Separators
```python
# For specialized formats
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    separators=[
        "\n## ",  # H2 headers
        "\n### ",  # H3 headers
        "\n\n",    # Paragraphs
        "\n",      # Lines
        " ",       # Words
        ""         # Chars
    ]
)
```

---

## 📝 Best Practices

1. **Start Conservative**
   ```python
   # Start with larger chunks, reduce if needed
   chunk_size=1000
   chunk_overlap=100
   ```

2. **Test Different Sizes**
   ```python
   for size in [256, 512, 1024, 2048]:
       test_splitter = CharacterTextSplitter(chunk_size=size)
       # Test quality of results
   ```

3. **Use Overlap for Context**
   ```python
   # More overlap = more context but redundancy
   chunk_overlap = chunk_size // 4  # 25% overlap
   ```

4. **Preserve Metadata**
   - Always keep source information
   - Track chunk origin
   - Enable traceability

5. **Test on Real Data**
   ```python
   # Don't guess, test with your actual documents
   sample_doc = load_document("sample.pdf")
   chunks = splitter.split_documents([sample_doc])
   # Inspect chunks quality
   ```

---

## 🔗 Workflow Integration

```
Load Documents
    ↓
Choose Splitter
    ↓
Split into Chunks
    ↓
Create Embeddings
    ↓
Store in Vector DB
    ↓
Enable Semantic Search
```

---

## ❓ Common Questions

**Q: What chunk size should I use?**
A: Start with 500-1000 characters. Adjust based on embedding model and LLM token limits.

**Q: Should I use overlap?**
A: Yes, overlap (10-20%) helps preserve context at boundaries.

**Q: Which splitter for unknown content?**
A: Use RecursiveCharacterTextSplitter - it's the safe default.

**Q: How do I know if splitting is good?**
A: Chunks should be semantically complete and not cut off mid-thought.

---

## 📚 Quick Reference

```python
# Length-based (simplest)
splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0)

# Recursive (recommended)
splitter = RecursiveCharacterTextSplitter(chunk_size=500)

# Markdown (for markdown)
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN, chunk_size=500
)

# Python code
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=500
)

# Semantic (advanced)
from langchain_experimental.text_splitters import SemanticChunker
splitter = SemanticChunker(embeddings_model)
```

---

**Ready to split documents smartly? Start with legth_based.py and progress to semantic! ✂️**

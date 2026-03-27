# Output Parsers 📊

Master the art of extracting, validating, and structuring data from LLM responses.

## 🎯 Overview

Output Parsers transform raw LLM responses into structured, validated formats. Without parsers, you get unstructured text. With parsers, you get clean data you can use in code.

**Simple Flow:**
```
LLM Output (raw text)
    ↓
Output Parser
    ↓
Structured Data (string, JSON, Pydantic object)
```

---

## 📂 Files in This Folder

### 1. **str_output_parser.py**
**What it does:** Converts LLM output to plain strings

**When to use:** 
- When you need simple text output
- When chaining multiple text operations

**Example:**
```python
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = GoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.7)
parser = StrOutputParser()

# Create chain: prompt → model → string parser
template = "Write a detailed report on {topic}"
prompt = PromptTemplate(template=template, input_variables=["topic"])

chain = prompt | model | parser  # Parser extracts the text

result = chain.invoke({"topic": "Virat Kohli"})
print(result)  # Gets clean string output
```

**Key Point:** 
`StrOutputParser` is the simplest parser. It just extracts `.content` from the response.

---

### 2. **str_output_parser1.py**
**What it does:** Chains multiple parsers and prompts

**Workflow:**
```
Input: {topic}
    ↓
Prompt 1 + Model + String Parser
    ↓ (output becomes input)
Prompt 2 + Model + String Parser
    ↓
Final Output
```

**Example:**
```python
# Step 1: Get detailed report
prompt1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

# Step 2: Summarize the report
prompt2 = PromptTemplate(
    template="Write a 3 line summary with dot points on:\n{text}",
    input_variables=["text"]
)

# Chain them: prompt1 → model → parser → prompt2 → model → parser
chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({"topic": "Virat Kohli"})
```

**When to use:**
- Multi-stage text processing
- Transforming content step by step
- Workflow pipelines

---

### 3. **json_output_parser.py**
**What it does:** Parses output as JSON and returns structured dictionary

**Benefits:**
- Structured output format
- Easy to access individual fields
- Works with JSON responses

**Example:**
```python
from langchain_core.output_parsers import JsonOutputParser

parser = JsonOutputParser()

template = """Write a 3 dot points report on {topic}. 
{format_instruction}"""

prompt = PromptTemplate(
    template=template,
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

chain = prompt | model | parser

result = chain.invoke({"topic": "Virat Kohli"})
# Result is a Python dict: {"point1": "...", "point2": "..."}
print(result["point1"])  # Access individual fields
```

**Key Features:**
- Automatically adds format instructions to prompt
- Returns Python dictionary
- Type: `dict`

**When to use:**
- Need structured key-value data
- Want easy field access
- Working with JSON APIs

---

### 4. **pydantic_output_parser.py**
**What it does:** Validates output against Pydantic models

**Benefits:**
- Type validation
- Required fields enforcement
- Type hints
- Clear data structure

**Example:**
```python
from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from langchain_core.output_parsers import PydanticOutputParser

# Define structure
class ReviewOutput(BaseModel):
    key_themes: List[str] = Field(..., description="Key themes")
    summary: str = Field(..., description="Brief summary")
    sentiment: Literal["positive", "negative", "neutral"] = Field(..., description="Sentiment")
    pros: Optional[List[str]] = Field(None, description="Pros")
    cons: Optional[List[str]] = Field(None, description="Cons")
    name: Optional[str] = Field(None, description="Reviewer name")

# Create parser
parser = PydanticOutputParser(pydantic_object=ReviewOutput)

# Build prompt with format instructions
template = """Analyze this review:
{format_instruction}
Review: {review}"""

prompt = PromptTemplate(
    template=template,
    input_variables=["review"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

chain = prompt | model | parser

# Result is ReviewOutput instance
result = chain.invoke({"review": "Great product! Highly recommend..."})
print(result.sentiment)  # Access as object attribute
print(result.pros)       # Type-safe access
```

**Key Features:**
- Full type validation
- Optional/required fields
- Clear schema definition
- Excellent for complex data

**When to use:**
- Complex nested structures
- Type safety important
- Production applications
- Data validation needed

---

## 📊 Parser Comparison

| Parser | Output Type | Validation | Complexity | Best For |
|--------|-------------|-----------|-----------|----------|
| **String** | `str` | None | Simple | Text output, chaining |
| **JSON** | `dict` | Basic | Medium | Structured data |
| **Pydantic** | `BaseModel` | Strong | Complex | Production, validation |

---

## 🎯 Advanced Parsing Scenarios

### Scenario 1: Extract Structured Data from Reviews

```python
from pydantic import BaseModel, Field
from typing import Literal, Optional, List

class Review(BaseModel):
    rating: int = Field(ge=1, le=5)  # Range validation
    sentiment: Literal["positive", "negative", "neutral"]
    keywords: List[str]
    recommendation: bool

parser = PydanticOutputParser(pydantic_object=Review)
```

### Scenario 2: Chain Parsers

```python
# Get text → parse as JSON → validate with Pydantic
json_parser = JsonOutputParser()
model = ChatGoogleGenerativeAI(...)

# First get JSON
chain1 = prompt1 | model | json_parser

# Then validate
result_dict = chain1.invoke(input)
review_obj = Review(**result_dict)
```

### Scenario 3: Custom Validation

```python
class Student(BaseModel):
    name: str
    age: int = Field(ge=0, le=120)
    cgpa: float = Field(ge=0.0, le=10.0)
    email: EmailStr  # Validates email format
```

---

## 💡 Best Practices

### 1. Choose Right Parser
```python
# Simple text → String parser
chain = prompt | model | StrOutputParser()

# Key-value data → JSON parser
chain = prompt | model | JsonOutputParser()

# Complex validated data → Pydantic
chain = prompt | model | PydanticOutputParser()
```

### 2. Clear Format Instructions
Parsers auto-generate format instructions. Make sure prompt guides model:
```python
template = """
Respond in valid JSON format with these exact fields:
{format_instruction}

User query: {query}
"""
```

### 3. Error Handling
```python
try:
    result = chain.invoke(input)
except Exception as e:
    print(f"Parsing error: {e}")
    # Handle gracefully
```

### 4. Validation Rules
```python
# Use Field validators
class Product(BaseModel):
    price: float = Field(gt=0)  # Must be positive
    quantity: int = Field(ge=0)  # Must be non-negative
    status: Literal["active", "inactive"]  # Only these values
```

---

## 🔗 Real-World Examples

### Example 1: Product Review Analysis
```python
from pydantic import BaseModel, Field
from typing import List, Optional, Literal

class ReviewAnalysis(BaseModel):
    product_name: str
    rating: int = Field(ge=1, le=5)
    pros: List[str]
    cons: List[str]
    sentiment: Literal["positive", "mixed", "negative"]
    would_recommend: bool

parser = PydanticOutputParser(pydantic_object=ReviewAnalysis)
chain = prompt | model | parser

# Gets fully structured, validated review data
```

### Example 2: Multi-Step Processing
```python
# Step 1: Extract text
chain1 = prompt1 | model | StrOutputParser()

# Step 2: Structure as JSON
chain2 = prompt2 | model | JsonOutputParser()

# Step 3: Validate with Pydantic
chain3 = prompt3 | model | PydanticOutputParser()

# Combined
result = chain1.invoke(input1)
result = chain2.invoke({"text": result})
result = chain3.invoke({"data": result})
```

### Example 3: Conditional Parsing
```python
def conditional_parser(output):
    if "json" in output.lower():
        return JsonOutputParser().parse(output)
    else:
        return StrOutputParser().parse(output)
```

---

## 🚀 Creating Custom Parsers

```python
from langchain_core.output_parsers import BaseOutputParser

class CustomParser(BaseOutputParser):
    def parse(self, text: str):
        # Your parsing logic
        return processed_output
```

---

## 📝 Common Patterns

### Pattern 1: Parse then Validate
```python
json_result = json_parser.parse(model_output)
validated_result = YourModel(**json_result)
```

### Pattern 2: Partial Validation
```python
# Some fields required, others optional
class FlexibleModel(BaseModel):
    required_field: str
    optional_field: Optional[str] = None
```

### Pattern 3: Transform Then Parse
```python
# Clean text before parsing
cleaned = output.strip().replace("\\n", "\n")
result = parser.parse(cleaned)
```

---

## ❓ Common Questions

**Q: Which parser should I use?**
A: Start with String for simple text. Use JSON for structured data. Use Pydantic for validated complex data.

**Q: How do I debug parsing errors?**
A: Print the raw model output before parsing to see what the model actually returned.

**Q: Can I combine multiple parsers?**
A: Yes! Chain them as: `prompt | model | parser1 | parser2`

**Q: What if the model doesn't return valid JSON?**
A: Add clear format instructions to your prompt. Sometimes you need to guide the model more explicitly.

---

**Ready to extract structured data from LLMs? Start with str_output_parser.py! 📊**

# Structured Output 🏗️

Master structured output schemas - ensure LLM outputs are validated, type-safe, and ready for production.

## 🎯 Overview

Structured output ensures the LLM returns data in a specific format with validation. Instead of hoping the model follows your format, you enforce it with schemas.

**Benefits:**
- Type-safe results
- Automatic validation
- Clear data contracts
- Production-ready
- IDE autocomplete support

---

## 📂 Files in This Folder

### 1. **pydentic_demo.py**
**What it does:** Demonstrates basic Pydantic data validation

**Concept:**
```python
from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Student(BaseModel):
    name: str = "Rahul"  # Default value
    age: Optional[int] = None  # Optional field
    email: EmailStr  # Validates email format
    cgpa: float = Field(ge=0.0, le=10.0, default=8.5)  # Range validation

# Create and validate
student_data = {
    "age": 21,
    "name": "piyush",
    "email": "piyush@example.com"
}

student = Student(**student_data)
print(student)  # Valid, prints formatted object
```

**Key Features:**
- Type hints define structure
- `Field()` for advanced validation
- Automatic type conversion
- Clear error messages on validation failure

**Validation Rules:**
- `ge` (>=), `le` (<=), `gt` (>), `lt` (<)
- `min_length`, `max_length`
- Custom validators
- Email validation with `EmailStr`

**When to use:**
- Any data structure
- Learning Pydantic basics
- Simple validation needs

---

### 2. **with_structured_output_pydantic.py**
**What it does:** Force LLM to return validated Pydantic objects

**Problem it solves:**
LLMs sometimes return incomplete or incorrect data formats. This enforces strict validation.

**Example:**
```python
from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from langchain_google_genai import ChatGoogleGenerativeAI

# Define expected output structure
class Review(BaseModel):
    key_themes: List[str] = Field(..., description="Key themes from review")
    summary: str = Field(..., description="Brief summary")
    sentiment: Literal["positive", "negative", "neutral"] = Field(..., description="Sentiment")
    pros: Optional[List[str]] = Field(None, description="Positive aspects")
    cons: Optional[List[str]] = Field(None, description="Negative aspects")
    name: Optional[str] = Field(None, description="Reviewer name")

# Configure model for structured output
model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")
structured_model = model.with_structured_output(Review)

# Now it returns Review object, not string
result = structured_model.invoke("iPhone 15 is amazing but expensive...")

print(result.sentiment)  # "positive"
print(result.pros)       # ["Fast", "Great camera", ...]
```

**How It Works:**
1. Define Pydantic model
2. Call `model.with_structured_output(Model)`
3. LLM returns validated object
4. Type-safe access to fields

**Advantages:**
- Type safety
- IDE autocomplete
- Validation automatic
- Clear error messages
- Production-ready

**When to use:**
- Complex nested data
- Validation required
- Type safety needed
- Production systems

---

### 3. **with_structured_output_typeddict.py**
**What it does:** Alternative to Pydantic using TypedDict annotations

**Concept:**
```python
from typing import TypedDict, Annotated, List, Optional, Literal

class Review(TypedDict):
    key_themes: Annotated[List[str], "Key themes mentioned"]
    summary: Annotated[str, "Brief summary"]
    sentiment: Annotated[Literal["positive", "negative", "neutral"], "Overall sentiment"]
    pros: Annotated[Optional[List[str]], "Positive aspects mentioned"]
    cons: Annotated[Optional[List[str]], "Negative aspects mentioned"]
    name: Annotated[Optional[str], "Reviewer name"]

# Use with model
model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")
structured_model = model.with_structured_output(Review)

result = structured_model.invoke("Samsung Galaxy S24 Ultra is powerful but heavy...")
```

**Differences from Pydantic:**
- Lighter weight
- No imports of BaseModel
- Uses type annotations with `Annotated`
- Less validation features
- Faster for simple schemas

**When to use:**
- Simple, flat structures
- Don't need complex validation
- Want lightweight approach
- TypedDict familiar

---

### 4. **with_structtured_output_json.py** (Note: typo in filename "structtured")
**What it does:** Define schema using raw JSON Schema

**Concept:**
```python
from langchain_google_genai import GoogleGenerativeAI

model = GoogleGenerativeAI(model="gemini-3-flash-preview")

# Define schema as JSON
json_schema = {
    "title": "Review",
    "type": "object",
    "properties": {
        "key_themes": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Key themes from review"
        },
        "summary": {
            "type": "string",
            "description": "Brief summary"
        },
        "sentiment": {
            "type": "string",
            "enum": ["positive", "negative", "neutral"],
            "description": "Overall sentiment"
        },
        "pros": {
            "type": ["array", "null"],
            "items": {"type": "string"}
        },
        "cons": {
            "type": ["array", "null"],
            "items": {"type": "string"}
        }
    },
    "required": ["key_themes", "summary", "sentiment"]
}

# Use JSON schema
structured_model = model.with_structured_output(json_schema)
result = structured_model.invoke("Product review text...")
```

**Advantages:**
- Language-agnostic
- Works with non-Python systems
- JSON standard
- Maximum control

**When to use:**
- Integration with other languages
- API contracts
- Complex nested schemas
- Maximum flexibility

---

## 📊 Schema Definition Comparison

| Method | Syntax | Validation | Complexity | Best For |
|--------|--------|-----------|-----------|----------|
| **Pydantic** | `BaseModel` | Strong | High | Complex, production |
| **TypedDict** | Type hints | Light | Medium | Simple, lightweight |
| **JSON Schema** | JSON objects | Custom | High | Multi-language integration |

---

## 🎯 Field Validation Examples

### Pydantic Validation Rules

```python
from pydantic import BaseModel, Field, EmailStr, HttpUrl
from typing import Optional, List, Literal

class Product(BaseModel):
    # String validations
    name: str = Field(min_length=1, max_length=255)
    
    # Number validations
    price: float = Field(gt=0, lt=100000)  # gt=greater than
    stock: int = Field(ge=0)  # ge=greater than or equal
    
    # Pattern matching
    sku: str = Field(pattern=r"^[A-Z]{3}-\d{4}$")
    
    # Email and URL
    support_email: EmailStr
    website: Optional[HttpUrl] = None
    
    # Enum/Literal
    status: Literal["active", "inactive", "archived"]
    
    # Collections
    tags: List[str] = Field(min_items=1, max_items=10)
    
    # Custom defaults
    created_by: str = Field(default="system")
```

---

## 💡 Real-World Examples

### Example 1: Customer Support Classification
```python
from pydantic import BaseModel, Field
from typing import Literal

class SupportTicket(BaseModel):
    subject: str = Field(..., description="Ticket subject")
    category: Literal["billing", "technical", "general"] = Field(..., description="Category")
    priority: Literal["low", "medium", "high", "urgent"] = Field(..., description="Priority")
    description: str = Field(..., description="Detailed issue")

# LLM automatically returns SupportTicket object with validation
model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")
support_model = model.with_structured_output(SupportTicket)
result = support_model.invoke("Can't login to my account!")
```

### Example 2: Product Information Extraction
```python
class ProductInfo(BaseModel):
    product_name: str
    price: float
    currency: str
    availability: Literal["in_stock", "out_of_stock", "pre_order"]
    rating: float = Field(ge=0, le=5)
    reviews_count: int
    key_features: List[str]

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")
product_model = model.with_structured_output(ProductInfo)

result = product_model.invoke("iPhone 15 product page...")
print(result.price)  # Type-safe access
```

### Example 3: Meeting Notes Extraction
```python
from typing import Optional
from datetime import datetime

class MeetingNote(BaseModel):
    date: str
    attendees: List[str]
    agenda: str
    decisions: List[str] = Field(..., description="Key decisions made")
    action_items: List[Dict[str, str]] = Field(..., description="Tasks with owners")
    next_meeting_date: Optional[str] = None

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")
note_model = model.with_structured_output(MeetingNote)

# Extract structure from meeting transcript
result = note_model.invoke(meeting_transcript)
```

---

## 🚀 Advanced Patterns

### Pattern 1: Nested Models
```python
class Address(BaseModel):
    street: str
    city: str
    country: str
    zip_code: str

class Person(BaseModel):
    name: str
    email: EmailStr
    address: Address  # Nested model
    phone_numbers: List[str]
```

### Pattern 2: Model Inheritance
```python
class BaseEntity(BaseModel):
    id: str
    created_at: str
    updated_at: str

class User(BaseEntity):
    username: str
    email: EmailStr
    role: Literal["admin", "user"]
```

### Pattern 3: Custom Validators
```python
from pydantic import field_validator

class BlogPost(BaseModel):
    title: str
    content: str
    tags: List[str]
    
    @field_validator('title')
    @classmethod
    def title_not_empty(cls, v):
        if len(v) < 5:
            raise ValueError('Title must be at least 5 characters')
        return v
```

---

## 🔍 Best Practices

1. **Use Pydantic for Production**
   - Best validation features
   - Type-safe
   - Great error messages

2. **Use Descriptive Field Names**
   ```python
   review_text: str  # ✓ Clear
   text: str         # ✗ Ambiguous
   ```

3. **Provide Good Descriptions**
   ```python
   sentiment: Literal["positive", "negative"] = Field(
       ..., 
       description="Overall sentiment of the review"
   )
   ```

4. **Use Optional for Nullable Fields**
   ```python
   middle_name: Optional[str] = None
   ```

5. **Set Constraints**
   ```python
   age: int = Field(ge=0, le=150)
   price: float = Field(gt=0)
   ```

---

## 🛠️ Debugging Structured Output

### Check Schema
```python
print(Review.model_json_schema())  # See generated schema
```

### Test Validation
```python
try:
    Review(**invalid_data)
except ValidationError as e:
    print(e.errors())  # See validation errors
```

### Inspect Results
```python
result = structured_model.invoke(input)
print(result.model_dump())  # Convert to dict
print(result.model_dump_json())  # Convert to JSON
```

---

## ❓ Common Questions

**Q: What's the difference between Pydantic and TypedDict?**
A: Pydantic has more validation features. TypedDict is lighter but less powerful.

**Q: Can I use nested models?**
A: Yes, define models inside models with Pydantic.

**Q: What if the LLM doesn't follow the schema?**
A: It will fail validation. Add clearer instructions or better descriptions.

**Q: How do I handle optional fields?**
A: Use `Optional[Type] = None` in Pydantic or `Optional` with TypedDict.

---

## 📚 Schema Reference

```python
# Common Pydantic imports
from pydantic import (
    BaseModel,
    Field,
    EmailStr,
    HttpUrl,
    field_validator,
    ValidationError
)

from typing import (
    Optional,
    List,
    Dict,
    Literal,
    Annotated
)
```

---

**Ready to enforce structured outputs? Start with pydentic_demo.py! 🏗️**

# Runnables ⚙️

Advanced patterns for composing, branching, and executing complex LLM workflows.

## 🎯 Overview

Runnables are the building blocks for sophisticated LangChain applications:

- **Lambda** - Custom functions
- **Branch** - Conditional routing
- **Parallel** - Concurrent execution
- **Passthrough** - Data flow
- **Sequence** - Step-by-step execution

**Core Syntax:**
```python
runnable = runnable1 | runnable2 | runnable3
```

---

## 📂 Files in This Folder

### 1. **runnable_lambda.py**
**What it does:** Convert custom Python functions into runnables

**Concept:**
```python
from langchain_core.runnables import RunnableLambda

# Define custom function
def process_text(text):
    return text.upper()

# Convert to runnable
runnable = RunnableLambda(process_text)

# Use in chain
result = runnable.invoke("hello")  # "HELLO"
```

**Why use Lambda?**
- Integrate custom logic
- Process data between chains
- Transform intermediate outputs

**Example Workflow:**
```
Input
    ↓
RunnableLambda: Clean text
    ↓
Model: Generate response
    ↓
RunnableLambda: Format output
    ↓
Output
```

**Practical Example:**
```python
from langchain_core.runnables import RunnableLambda
from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI()

# Custom functions as runnables
def uppercase(text):
    return text.upper()

def count_words(text):
    return {"text": text, "word_count": len(text.split())}

# Chain them
chain = RunnableLambda(uppercase) | model | RunnableLambda(count_words)
```

**When to use:**
- Custom data transformation
- Integration with external APIs
- Complex logic between chain steps

---

### 2. **runnable_parallel.py**
**What it does:** Execute multiple chains concurrently

**Concept:**
```
                ┌─ Chain 1
Input ──────────┤
                └─ Chain 2
                
Both run at same time ↓
                
Output: {chain1_result, chain2_result}
```

**Example:**
```python
from langchain_core.runnables import RunnableParallel

chain1 = prompt1 | model | parser
chain2 = prompt2 | model | parser

parallel = RunnableParallel({
    "topic_summary": chain1,
    "competitors_summary": chain2
})

result = parallel.invoke({"topic": "Virat Kohli"})
# Result: {"topic_summary": "...", "competitors_summary": "..."}
```

**Key Points:**
- Both chains run simultaneously (faster!)
- Results are combined in a dictionary
- Each chain is independent

**Advantages:**
- Performance improvement
- Parallel processing
- Combining multiple perspectives

**When to use:**
- Comparison tasks
- Getting multiple analyses
- Performance optimization
- Gathering data from parallel sources

---

### 3. **runnable_passthrough.py**
**What it does:** Pass data through without modification

**Concept:**
```python
from langchain_core.runnables import RunnablePassthrough

# Keep input available for later steps
chain = RunnablePassthrough() | process_function
```

**Why needed?**
When chaining, intermediate data can be lost. `RunnablePassthrough` preserves it.

**Example:**
```python
# Without passthrough - data is lost
prompt1 = PromptTemplate(...)
chain1 = prompt1 | model  # Original input is lost here

# With passthrough - preserve original input
chain = RunnablePassthrough() | {"original": RunnablePassthrough(), "response": prompt1 | model}
# Now you have both the original input and the response
```

**When to use:**
- Need original input and processed output together
- Complex workflows requiring data preservation
- Building advanced chains

---

### 4. **runnable_branch.py**
**What it does:** Route execution based on conditions (conditional logic)

**Concept:**
```
Input
    ↓
Check Condition
    ↓
    ├─ If True → Execute Path A
    │
    └─ If False → Execute Path B
    ↓
Output
```

**Example:**
```python
from langchain_core.runnables import RunnableBranch

# Define branches
branch = RunnableBranch(
    (lambda x: x["sentiment"] == "positive", positive_prompt | model),
    (lambda x: x["sentiment"] == "negative", negative_prompt | model),
    neutral_prompt | model  # Default
)

result = branch.invoke({"sentiment": "positive", "feedback": "Great product!"})
```

**How It Works:**
1. Evaluate condition
2. Route to appropriate chain
3. Return result

**Practical Application:**
```python
# Route based on time of day
from datetime import datetime

branch = RunnableBranch(
    (lambda x: datetime.now().hour > 12, prompt2 | model),  # Afternoon
    prompt3 | model  # Morning/other
)
```

**When to use:**
- Sentiment-based routing
- Category-based processing
- Conditional logic
- A/B testing
- Smart routing workflows

---

### 5. **runnable_sequance.py** (Note: File has typo in name - "sequance" should be "sequence")
**What it does:** Execute chains in sequence with proper data flow

**Concept:**
```python
from langchain_core.runnables import RunnableSequence

# Define sequential execution
sequence = RunnableSequence(chain1, chain2, chain3)

# Or use pipe operator
sequence = chain1 | chain2 | chain3
```

**Example:**
```python
from langchain_core.runnables import RunnableSequence
from langchain_core.prompts import PromptTemplate

# Step 1: Generate response
prompt1 = PromptTemplate(template="Generate response for: {query}", input_variables=["query"])

# Step 2: Summarize
prompt2 = PromptTemplate(template="Summarize: {text}", input_variables=["text"])

# Step 3: Extract keywords
prompt3 = PromptTemplate(template="Extract 5 keywords from: {text}", input_variables=["text"])

# Chain them sequentially
sequence = prompt1 | model | parser | prompt2 | model | parser | prompt3 | model | parser

result = sequence.invoke({"query": "Tell me about AI"})
```

**Data Flow:**
```
Input (query)
    ↓
Prompt1 + Model + Parser
    ↓ (output becomes input)
Prompt2 + Model + Parser
    ↓
Prompt3 + Model + Parser
    ↓
Final Output
```

**When to use:**
- Multi-step workflows
- Progressive refinement
- Sequential transformation
- Pipeline processing

**Visualization:**
```python
sequence.get_graph().print_ascii()  # See the sequence structure
```

---

## 🎯 Runnable Patterns Comparison

| Runnable | Purpose | Best For |
|----------|---------|----------|
| **Lambda** | Custom functions | Data transformation, integration |
| **Parallel** | Concurrent execution | Multiple analyses, performance |
| **Passthrough** | Data preservation | Complex workflows, multi-input |
| **Branch** | Conditional routing | Smart logic, categorization |
| **Sequence** | Step-by-step | Pipelines, progressive refinement |

---

## 🚀 Advanced Patterns

### Pattern 1: Parallel Then Branch
```python
parallel = RunnableParallel({
    "summary": summary_chain,
    "sentiment": sentiment_chain
})

branch = RunnableBranch(
    (lambda x: x["sentiment"] == "positive", positive_response),
    negative_response
)

chain = parallel | branch
```

### Pattern 2: Lambda for Complex Logic
```python
def complex_logic(input_dict):
    if input_dict.get("score") > 0.8:
        return {"status": "high", "action": "escalate"}
    else:
        return {"status": "normal", "action": "process"}

processor = RunnableLambda(complex_logic)
```

### Pattern 3: Nested Sequences
```python
sequence1 = prompt1 | model | parser
sequence2 = prompt2 | model | parser
sequence3 = prompt3 | model | parser

main = RunnableBranch(
    (condition1, sequence1),
    (condition2, sequence2),
    sequence3
)
```

### Pattern 4: Error Handling with Lambda
```python
def safe_invoke(runnable, input_data, default="Error occurred"):
    try:
        return runnable.invoke(input_data)
    except Exception as e:
        return default

safe_wrapper = RunnableLambda(lambda x: safe_invoke(chain, x))
```

---

## 💡 Real-World Examples

### Example 1: Sentiment Analysis Pipeline
```python
# Get response → Analyze sentiment → Route response
analyze_sentiment = PydanticOutputParser(sentiment_schema)

pipeline = (
    classification_chain |
    RunnableBranch(
        (lambda x: x.sentiment == "positive", positive_handler),
        (lambda x: x.sentiment == "negative", negative_handler),
        neutral_handler
    )
)
```

### Example 2: Multi-Step Refinement
```python
# Draft → Review → Refine → Finalize
sequence = (
    draft_chain |
    RunnableLambda(lambda x: review_draft(x)) |
    refine_chain |
    finalize_chain
)
```

### Example 3: Parallel Analysis
```python
# Analyze from multiple angles simultaneously
analysis = RunnableParallel({
    "technical": technical_analysis_chain,
    "business": business_analysis_chain,
    "social": social_analysis_chain
})

# Then combine results
combined = analysis | merge_results_chain
```

---

## 🔍 Debugging Runnables

### 1. Visualize Structure
```python
chain.get_graph().print_ascii()
```

### 2. Test Individual Components
```python
# Test each component separately
result1 = chain1.invoke(input)
result2 = chain2.invoke(result1)
```

### 3. Add Logging
```python
def log_step(data):
    print(f"Step data: {data}")
    return data

chain = step1 | RunnableLambda(log_step) | step2
```

### 4. Use Streaming
```python
for chunk in chain.stream(input):
    print(chunk)
```

---

## 📊 Execution Flow Comparison

```
LAMBDA:
Input → Custom Function → Output

PARALLEL:
Input → ├─ Chain1 → ├─ Combined Output
         └─ Chain2 → ┘

BRANCH:
Input → Check Condition → Route Decision → Selected Chain → Output

SEQUENCE:
Input → Step1 → Step2 → Step3 → Output

PASSTHROUGH:
Input → Keep Input & Process → {original: input, processed: output}
```

---

## 🛠️ Best Practices

1. **Start Simple** - Use basic sequences first
2. **Test Components** - Test each runnable independently
3. **Visualize** - Use `get_graph().print_ascii()` to verify
4. **Handle Errors** - Wrap in try-except or error-handling runnables
5. **Use Lambda Carefully** - Keep functions simple and pure
6. **Monitor Performance** - Parallel execution is faster but uses more resources

---

## ❓ Common Questions

**Q: When should I use Parallel vs Sequence?**
A: Use Parallel for independent operations (faster). Use Sequence when output depends on previous steps.

**Q: How do I pass multiple inputs to chains?**
A: Use RunnableLambda to transform input format, or use RunnablePassthrough.

**Q: Can I nest branches?**
A: Yes, you can have branches inside branches for complex logic.

**Q: How do I debug data flow?**
A: Print intermediate results or use RunnableLambda with print statements.

---

## 🔗 Related Topics

- **Chains/** - Basic chain concepts
- **Output-Parser/** - Parse runnable outputs
- **Models/** - Understand model components

---

**Ready to build sophisticated workflows? Start with runnable_lambda.py! ⚙️**

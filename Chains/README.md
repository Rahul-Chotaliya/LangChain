# Chains 🔗

Master the art of building sophisticated workflows by combining prompts, models, and processing steps into reusable chains.

## 📚 Overview

Chains are the backbone of LangChain. They allow you to combine multiple components (prompts, models, output parsers) into a single workflow. Think of a chain as a pipeline where data flows through multiple processing stages.

**Basic Chain Syntax:**
```python
chain = prompt | model | output_parser
```

This reads as: "Pass the prompt to the model, then parse the output"

---

## 📂 Files in This Folder

### 1. **simple_chain.py** 
**What it does:** Creates the simplest possible chain

**Concept:**
- Single prompt template
- One model invocation
- Direct output

**Example Flow:**
```
Input: {topic: "Hardik Pandya"}
    ↓
PromptTemplate: "What are the latest news about {topic}?"
    ↓
ChatGoogleGenerativeAI Model
    ↓
Output: Latest news about Hardik Pandya
```

**Key Learning Points:**
- How to create a `PromptTemplate`
- How to initialize a model
- How to use the pipe operator `|` to chain components
- How to invoke a chain with `.invoke()`

**When to use:** 
- Single-step operations
- General Q&A
- Simple text generation

---

### 2. **sequential_chain.py**
**What it does:** Chains multiple operations where output of one becomes input to the next

**Concept:**
```
Input Topic
    ↓
Prompt 1: Generate news summary
    ↓
Model: Generate text
    ↓
Parser: Convert to string
    ↓
Prompt 2: Extract 3 keywords
    ↓
Model: Extract keywords
    ↓
Parser: Convert to string
    ↓
Final Output: Keywords
```

**Workflow:**
1. Takes a topic as input
2. Generates news summary
3. From the summary, extracts 3 important words
4. Returns just the words

**Key Learning Points:**
- Chaining multiple prompts together
- Using `StrOutputParser` to convert outputs to strings
- How data flows through multiple stages
- Visualizing chain structure with `.get_graph().print_ascii()`

**When to use:**
- Multi-step processes
- Text transformation pipelines
- Summarize → Analyze → Transform workflows
- Tasks requiring multiple processing stages

---

### 3. **parallel_chain.py**
**What it does:** Execute multiple chains concurrently and merge their outputs

**Concept:**
```
                    ┌─ Prompt 1: Get summary of {topic}
Input {topic}───┤
                    └─ Prompt 2: Get summary of {topic} competitors

    Both run in parallel →

Output: Merged report combining both summaries
```

**Workflow:**
1. Takes a topic (e.g., "Virat Kohli")
2. Generates 5-point summary in parallel chain 1
3. Generates 3-point summary of competitors in parallel chain 2
4. Merges both outputs into a single comprehensive report

**Key Learning Points:**
- Using `RunnableParallel` for concurrent execution
- How parallel execution improves performance
- Merging outputs from multiple sources
- The structure of parallel workflows

**When to use:**
- Need multiple analyses simultaneously
- Comparing entities or perspectives
- Performance optimization
- Combining multiple perspectives (pros/cons, market/competition)

---

### 4. **conditional_chain.py**
**What it does:** Routes execution based on conditions (branching logic)

**Concept:**
```
User Feedback
    ↓
Classify sentiment (positive/negative)
    ↓
    ├─ If positive → Generate positive response
    │
    └─ If negative → Generate empathetic response
    ↓
Final Response
```

**Workflow:**
1. Takes feedback text as input
2. Uses a classifier chain to determine sentiment
3. Based on sentiment, routes to different response prompts
4. Returns appropriate response

**Key Learning Points:**
- Using `PydanticOutputParser` for structured classification
- Implementing `RunnableBranch` for conditional logic
- Lambda functions for condition checking
- Intelligent routing based on data content

**When to use:**
- Sentiment-based routing
- Different handling for different categories
- Intelligent branching workflows
- Customer service automation
- Content moderation and routing
- A/B testing scenarios

**Example Use Cases:**
- Route positive feedback for rewards pipeline
- Route negative feedback for support system
- Route urgent emails differently than regular ones
- Route medical symptoms to appropriate specialists

---

## 🎯 Understanding Chain Components

### What is a Prompt?
A template that defines how to format your input and instruct the model:
```python
prompt = PromptTemplate(
    template="What are the latest news about {topic}?",
    input_variables=["topic"]
)
```

### What is a Model?
An LLM that processes the prompt and generates output:
```python
model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")
```

### What is an Output Parser?
Converts raw LLM output into usable formats:
```python
parser = StrOutputParser()  # Outputs as string
```

### The Pipe Operator (|)
Chains components together. Python calls `__or__` method:
```python
chain = prompt | model | parser
```

This is equivalent to:
```python
chain = prompt.pipe(model).pipe(parser)
```

---

## 💡 Different Chain Patterns

### Pattern 1: Prompt → Model
**Simplest chain:**
```python
chain = prompt | model
result = chain.invoke({"topic": "AI"})
```

### Pattern 2: Prompt → Model → Parser
**Most common:**
```python
chain = prompt | model | parser
result = chain.invoke({"topic": "AI"})
```

### Pattern 3: Multiple Prompts (Sequential)
**For step-by-step processing:**
```python
chain = prompt1 | model | parser | prompt2 | model | parser
result = chain.invoke({"initial_input": "..."})
```

### Pattern 4: Parallel Processing
**For concurrent operations:**
```python
parallel = RunnableParallel({
    "result1": chain1,
    "result2": chain2
})
result = parallel.invoke({"input": "..."})
```

### Pattern 5: Conditional Routing
**For intelligent branching:**
```python
branch = RunnableBranch(
    (lambda x: x.sentiment == "positive", positive_prompt | model),
    (negative_prompt | model)
)
```

---

## 📊 Comparison: When to Use Each Chain Type

| Chain Type | Use Case | Complexity | Speed |
|------------|----------|-----------|-------|
| **Simple** | Basic Q&A, text generation | ⭐ | Fast |
| **Sequential** | Multi-step transformation | ⭐⭐ | Medium |
| **Parallel** | Multiple independent ops | ⭐⭐ | Very Fast |
| **Conditional** | Smart routing, branching | ⭐⭐⭐ | Medium |

---

## 🚀 Hands-On Exercises

### Exercise 1: Create Your Own Simple Chain
```python
# Create a chain that explains concepts
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.7)
prompt = PromptTemplate(
    template="Explain {concept} to a {audience}",
    input_variables=["concept", "audience"]
)
chain = prompt | model
result = chain.invoke({"concept": "Machine Learning", "audience": "5-year-old"})
print(result.content)
```

### Exercise 2: Build a Sequential Chain
```python
# Chain that summarizes then analyzes
prompt1 = PromptTemplate(template="Summarize: {text}", input_variables=["text"])
prompt2 = PromptTemplate(template="Analyze sentiment of: {text}", input_variables=["text"])
from langchain_core.output_parsers import StrOutputParser
parser = StrOutputParser()
chain = prompt1 | model | parser | prompt2 | model | parser
```

### Exercise 3: Visualize Your Chain
```python
chain.get_graph().print_ascii()  # See chain structure visually
```

---

## 🔍 Chain Visualization

All chains support visualization:
```python
chain.get_graph().print_ascii()
```

This shows you:
- Order of execution
- Input/output flow
- Component connections

---

## ⚙️ Advanced Chain Concepts

### 1. Chain Input/Output
```python
# Define what enters and exits
chain.input_schema  # Shows expected inputs
chain.output_schema  # Shows output format
```

### 2. Debugging Chains
```python
# Enable verbose output
chain.invoke(input, verbose=True)

# Or stream intermediate results
for chunk in chain.stream(input):
    print(chunk)
```

### 3. Async Chains
```python
import asyncio

# Run chains asynchronously for better performance
result = await chain.ainvoke(input)
```

---

## 📝 Best Practices

1. **Start Simple** - Build simple chains first, then add complexity
2. **Test Components** - Test each component individually
3. **Use Meaningful Names** - Name chains and prompts clearly
4. **Visualize** - Use `get_graph().print_ascii()` to verify structure
5. **Handle Errors** - Wrap API calls in try-except
6. **Monitor Costs** - LLM calls have costs, watch your usage
7. **Set Appropriate Temperatures** - 0 for deterministic, 1 for creative

---

## 🎓 Learning Progression

**Week 1:** Master simple and sequential chains
**Week 2:** Explore parallel chains and performance
**Week 3:** Implement conditional logic with branches
**Week 4:** Combine all patterns for real-world applications

---

## 🔗 Related Topics

- **Prompts/** - Learn prompt engineering
- **Output-Parser/** - Master output formatting
- **Runnables/** - Advanced chain abstractions
- **Document-Loaders/** - Feed documents into chains

---

## 💬 Common Questions

**Q: What's the difference between simple and sequential chains?**
A: Simple chains have one step. Sequential chains have multiple steps where output of one feeds into the next.

**Q: Can I use the same prompt in multiple chains?**
A: Yes! Prompts are reusable components.

**Q: How do I debug a failing chain?**
A: Use `verbose=True`, print intermediate outputs, and test each component separately.

**Q: Can I save and load chains?**
A: Yes, using LangChain's serialization methods.

---

**Ready to build sophisticated workflows? Start with simple_chain.py and progress from there! 🚀**

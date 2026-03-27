# Prompts ✍️

Master prompt engineering - the art of instructing AI models effectively.

## 🎯 Overview

A prompt is your instruction to the AI model. Good prompts = better results.

**Formula:** Input Variables + Template = Prompt

```
Template: "Greet {person} in {language}"
Variables: person="Alice", language="French"
Result: "Greet Alice in French"
```

---

## 📂 Files in This Folder

### 1. **prompt_template.py**
**What it does:** Creates reusable prompt templates with variables

**Concept:**
```python
from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template='Greet this person in 5 languages. The name of the person is {name}',
    input_variables=['name']
)

# Use the template
prompt = template.invoke({'name': 'Rahul'})
# Result: 'Greet this person in 5 languages. The name of the person is Rahul'

# Pass to model
result = model.invoke(prompt)
```

**Why use templates?**
- Reusability - Define once, use many times
- Clarity - Easy to see what variables you need
- Maintainability - Change template in one place
- Dynamic - Fill in values at runtime

**When to use:**
- Any prompt with variables
- Building chains
- Production applications

---

### 2. **chhat_prompt_template.py**
**What it does:** Creates chat-specific prompts (system + user messages)

**Concept:**
```python
from langchain_core.prompts import ChatPromptTemplate

# Define roles and messages
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])

# Fill in variables
prompt = chat_template.invoke({
    'domain': 'cricket',
    'topic': 'Dusra'
})
```

**Key Difference:**
- `PromptTemplate`: Simple text template
- `ChatPromptTemplate`: Multiple roles (system, human, assistant)

**Message Roles:**
- `system` - Instructions for the AI
- `human` - User message
- `assistant` - Previous AI responses

**When to use:**
- Conversations
- Multi-turn interactions
- Chat-based applications

---

### 3. **message.py**
**What it does:** Work with message objects for conversations

**Message Types:**
```python
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# Create different message types
messages = [
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about LangChain'),
    AIMessage(content='LangChain is a framework for...'),
]

# All messages together create conversation context
result = model.invoke(messages)
```

**Why Message Objects?**
- Clear communication structure
- Model understands roles
- Maintains conversation history
- Type-safe

**Message Flow:**
```
SystemMessage (instructions)
    ↓
HumanMessage (user input)
    ↓
AIMessage (model response)
    ↓
HumanMessage (next user input)
    ↓
...continues...
```

**When to use:**
- Multi-turn conversations
- Managing chat history
- Complex dialogues

---

### 4. **message_placeholder.py**
**What it does:** Use placeholders for dynamic chat history

**Problem it solves:**
How do you insert chat history into a prompt?

**Solution:**
```python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])

# Later, pass chat history
history = [
    HumanMessage("Previous question"),
    AIMessage("Previous answer")
]

prompt = chat_template.invoke({
    'chat_history': history,
    'query': 'Where is my refund?'
})
```

**Key Feature:**
`MessagesPlaceholder` - Inserts entire list of messages

**When to use:**
- Maintaining conversation history
- Building chatbots
- Multi-turn support systems

---

### 5. **prompt_generator.py**
**What it does:** Creates and saves complex prompt templates

**Example:**
```python
from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}" 
with the following specifications:
Explanation Style: {style_input}
Explanation Length: {length_input}

Include mathematical details and analogies.
""",
    input_variables=['paper_input', 'style_input', 'length_input'],
    validate_template=True
)

# Save to file
template.save('template.json')
```

**Validates Variables:**
The prompt checks that `{variable_name}` matches `input_variables`

**When to use:**
- Complex prompts with many variables
- Templates you want to save/share
- Production systems

---

### 6. **prompt_ui.py**
**What it does:** Interactive prompt interface with Streamlit

**Concept:**
```python
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

# UI inputs
paper = st.selectbox("Select Paper", ["Paper 1", "Paper 2", ...])
style = st.selectbox("Select Style", ["Beginner", "Technical", ...])
length = st.selectbox("Select Length", ["Short", "Medium", "Long"])

# Load saved template
template = load_prompt('template.json')

# Generate response
if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
        'paper_input': paper,
        'style_input': style,
        'length_input': length
    })
    st.write(result.content)
```

**Features:**
- Interactive dropdowns
- Save/load templates
- Beautiful UI

**When to use:**
- Demo applications
- User-facing tools
- Testing prompts quickly

---

### 7. **temprature.py**
**What it does:** Demonstrates temperature effect on responses

**What is temperature?**
Controls randomness/creativity:
- 0.0 → Always deterministic (same facts)
- 0.5 → Balanced (default)
- 1.0+ → Very creative/random (creative writing)

**Example:**
```python
from langchain_google_genai import ChatGoogleGenerativeAI

# Deterministic (for facts)
model_factual = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0)

# Creative (for writing)
model_creative = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=1.5)

# Test with same prompt
prompt = "Write a poem about cricket"
print(model_factual.invoke(prompt))   # Consistent
print(model_creative.invoke(prompt))  # Different each time
```

**Temperature Guide:**
- 0.0-0.3: Factual tasks (Q&A, summarization, math)
- 0.5-0.7: Balanced (general use, default)
- 0.8-1.0: Creative (writing, brainstorming)
- 1.0+: Very creative (fiction, experiments)

**When to use:**
- Understanding model behavior
- Tuning for specific tasks
- Production optimization

---

### 8. **chatbot.py**
**What it does:** Simple chatbot with conversation history

**Concept:**
```python
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

model = ChatOpenAI()

# Start conversation
chat_history = [
    SystemMessage(content='You are a helpful AI assistant')
]

# Chat loop
while True:
    user_input = input('You: ')
    if user_input == 'exit':
        break
    
    # Add user message
    chat_history.append(HumanMessage(content=user_input))
    
    # Get response
    result = model.invoke(chat_history)
    
    # Add AI response
    chat_history.append(AIMessage(content=result.content))
    print("AI: " + result.content)
```

**How It Works:**
1. Keep list of all messages
2. Add new user message
3. Send entire history to model
4. Model responds with context
5. Add response to history

**When to use:**
- Building chatbots
- Interactive applications
- Multi-turn conversations

---

## 📊 Template Types Comparison

| Type | Use Case | Roles | Best For |
|------|----------|-------|----------|
| **PromptTemplate** | Simple text | None | Q&A, simple tasks |
| **ChatPromptTemplate** | Multiple roles | system, human, assistant | Conversations |
| **MessagesPlaceholder** | Dynamic history | Any | Chatbots, history |
| **File Templates** | Reusable | Any | Production, teams |

---

## 🎯 Prompt Engineering Principles

### 1. Be Specific
**Bad:** "Write about machine learning"
**Good:** "Write a 3-paragraph explanation of neural networks for a high school student"

### 2. Give Context
**Bad:** "Summarize this"
**Good:** "Summarize this research paper in 100 words focusing on the methodology"

### 3. Define Output Format
**Bad:** "Tell me about Python"
**Good:** "List 5 key advantages of Python with bullet points"

### 4. Use Examples (Few-shot)
```python
template = """
Examples:
- Input: "sunny" → Output: "pleasant"
- Input: "rainy" → Output: "gloomy"

Now respond:
- Input: "{weather}" → Output:
"""
```

### 5. Use Role Playing
```python
template = """
You are a {role} expert with 10 years of experience.
Explain how {topic} works to {audience}.
"""
```

---

## 💡 Advanced Techniques

### Technique 1: Chain of Thought
Encourage the model to think step-by-step:
```python
template = """
Let's solve this step-by-step:
1. First, understand the problem
2. Then, identify key components
3. Finally, provide the solution

Problem: {problem}
"""
```

### Technique 2: Temperature Tuning per Stage
```python
# Stage 1: Brainstorm (high temperature)
model1 = ChatOpenAI(temperature=0.9)

# Stage 2: Refine (medium temperature)
model2 = ChatOpenAI(temperature=0.5)

# Stage 3: Finalize (low temperature)
model3 = ChatOpenAI(temperature=0.1)
```

### Technique 3: Prompt Templates for Different Audiences
```python
templates = {
    'child': 'Explain {topic} using simple words and examples',
    'expert': 'Provide technical details about {topic}',
    'executive': 'Summarize key business impact of {topic}'
}
```

---

## 🚀 Hands-On Exercises

### Exercise 1: Create Your Own Template
```python
from langchain_core.prompts import PromptTemplate

my_template = PromptTemplate(
    template="What would a {character} say about {situation}?",
    input_variables=["character", "situation"]
)

result = model.invoke(my_template.invoke({
    "character": "Shakespeare",
    "situation": "learning programming"
}))
```

### Exercise 2: Build a Chat Template
```python
from langchain_core.prompts import ChatPromptTemplate

chat = ChatPromptTemplate([
    ('system', 'You are a {role}'),
    ('human', '{query}')
])

prompt = chat.invoke({
    'role': 'Python expert',
    'query': 'How do decorators work?'
})
```

### Exercise 3: Experiment with Temperature
```python
# Run same prompt with different temperatures
for temp in [0, 0.5, 1.0]:
    model = ChatOpenAI(temperature=temp)
    result = model.invoke("Write a creative title for a tech blog")
    print(f"Temp {temp}: {result.content}")
```

---

## 📝 Template Variables Best Practices

1. **Use Descriptive Names**
   - ✓ `{user_query}`, `{document_content}`
   - ✗ `{x}`, `{input}`

2. **Keep Variable Lists Clear**
   - `input_variables=["topic", "audience", "style"]`

3. **Document Variables**
   - Add comments explaining each variable

4. **Test All Combinations**
   - Ensure prompt works with different inputs

---

## ⚙️ Advanced Features

### Feature 1: Partial Variables
```python
# Pre-fill some variables
template = PromptTemplate(
    template="Explain {concept} to {audience}",
    input_variables=["concept"],
    partial_variables={"audience": "expert"}
)
```

### Feature 2: Template Validation
```python
template = PromptTemplate(
    template="Hello {name}, you are {age} years old",
    input_variables=["name", "age"],
    validate_template=True  # Checks variables match template
)
```

### Feature 3: Output Formats
```python
template = """
Respond in this format:
Title: {format_instruction}
Content: 
{content}
"""
```

---

## ❓ Common Questions

**Q: Should I use variables or hardcode values?**
A: Use variables for anything that changes. This makes prompts reusable.

**Q: How many variables is too many?**
A: Keep it under 5-6 for clarity. Too many becomes confusing.

**Q: Can I use conditionals in templates?**
A: Templates are just strings. Use code logic for conditionals.

**Q: How do I test prompts?**
A: Try with different inputs, check outputs, iterate based on results.

---

**Ready to craft effective prompts? Start with prompt_template.py! ✍️**

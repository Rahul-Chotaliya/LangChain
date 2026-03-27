# MCP Client 🔗

Master the Model Context Protocol (MCP) - connect LLMs with external tools and services seamlessly.

## 🎯 Overview

MCP (Model Context Protocol) allows LLMs to access and interact with external tools:

- **Math operations** - Complex calculations
- **Expense tracking** - Data management
- **Visualization** - Create diagrams (Manim)
- **Custom services** - Your own tools

**Architecture:**
```
LLM ← → MCP Client ← → MCP Server 1 (Math)
                    ← → MCP Server 2 (Expense)
                    ← → MCP Server 3 (Visualization)
```

---

## 📂 Files in This Folder

### 1. **client1.py**
**What it does:** Basic MCP client connecting to multiple servers

**Concept:**
```python
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_google_genai import ChatGoogleGenerativeAI

# Define servers
SERVERS = {
    "math": {
        "transport": "stdio",
        "command": "/path/to/python",
        "args": ["math_server.py"]
    },
    "expense": {
        "transport": "streamable_http",
        "url": "https://expense-server.app/mcp"
    }
}

# Create client
client = MultiServerMCPClient(SERVERS)

# Get available tools
tools = await client.get_tools()

# Bind with LLM
llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")
llm_with_tools = llm.bind_tools(tools)

# Use in conversation
response = await llm_with_tools.ainvoke("Draw a triangle")
```

**How It Works:**
1. Define server connections
2. Client discovers available tools
3. Bind tools to LLM
4. LLM can now call tools
5. Results flow back to LLM

**When to use:**
- Accessing external services
- Math calculations
- Data operations
- Custom integrations

---

### 2. **client2.py**
**What it does:** Advanced MCP client with Streamlit UI

**Features:**
- Interactive chatbot
- Multi-server integration
- Streamlit for beautiful UI
- Tool invocation with streaming

**Example:**
```python
import streamlit as st
from langchain_mcp_adapters.client import MultiServerMCPClient

st.title("🧰 MCP Chat")

# Initialize MCP servers
if "initialized" not in st.session_state:
    client = MultiServerMCPClient(SERVERS)
    tools = asyncio.run(client.get_tools())
    st.session_state.client = client
    st.session_state.tools = tools
    st.session_state.llm_with_tools = llm.bind_tools(tools)
    st.session_state.initialized = True

# Chat interface
user_input = st.chat_input("Type a message...")

if user_input:
    # Invoke LLM with tools
    response = asyncio.run(st.session_state.llm_with_tools.ainvoke(user_input))
    
    # Handle tool calls
    if response.tool_calls:
        # Execute tools
        for tool_call in response.tool_calls:
            tool_result = asyncio.run(
                st.session_state.tool_by_name[tool_call["name"]].ainvoke(
                    tool_call.get("args", {})
                )
            )
    
    st.write(response.content)
```

**When to use:**
- Production applications
- User-facing tools
- Interactive demos
- Complex workflows

---

## 🏗️ MCP Architecture

### Server Types

#### 1. **stdio Transport** (Local Process)
```python
"math": {
    "transport": "stdio",
    "command": "/usr/bin/python3",
    "args": ["math_server.py"],
    "env": {"PYTHONPATH": "/path/to/server"}
}
```

**Pros:**
- No network latency
- Full control
- Can be local binary

**Cons:**
- Must be available locally
- Process management needed

#### 2. **HTTP Transport** (Remote Server)
```python
"expense": {
    "transport": "streamable_http",
    "url": "https://api.example.com/mcp"
}
```

**Pros:**
- Remote access
- No local setup
- Scalable

**Cons:**
- Network latency
- Requires server availability
- Authentication needed

---

## 🎯 Workflow: Using Tools

### Step 1: Define Servers
```python
SERVERS = {
    "math_server": {
        "transport": "stdio",
        "command": "uv",
        "args": ["run", "fastmcp", "run", "math_server.py"]
    }
}
```

### Step 2: Create Client
```python
client = MultiServerMCPClient(SERVERS)
```

### Step 3: Get Tools
```python
tools = await client.get_tools()
# tools is a list of tool definitions
```

### Step 4: Bind to LLM
```python
llm_with_tools = llm.bind_tools(tools)
```

### Step 5: Use in Conversation
```python
response = await llm_with_tools.ainvoke("Calculate 2+2")

# If LLM wants to use a tool:
if response.tool_calls:
    for tool_call in response.tool_calls:
        result = await tool_by_name[tool_call["name"]].ainvoke(
            tool_call.get("args", {})
        )
```

---

## 🛠️ Common MCP Servers

### Math Server
```python
# Performs mathematical operations
{
    "transport": "stdio",
    "command": "uv",
    "args": ["run", "fastmcp", "run", "math_server.py"]
}
```

**Available Tools:**
- Calculate expressions
- Solve equations
- Matrix operations
- Statistical functions

### Expense Server
```python
# Manages expense tracking
{
    "transport": "streamable_http",
    "url": "https://expense-api.app/mcp"
}
```

**Available Tools:**
- Create expenses
- Generate reports
- Track budgets

### Manim Server (Visualization)
```python
# Creates mathematical animations/diagrams
{
    "transport": "stdio",
    "command": "python3",
    "args": ["manim_server.py"],
    "env": {"MANIM_EXECUTABLE": "/path/to/manim"}
}
```

**Available Tools:**
- Draw shapes
- Create animations
- Visualize math concepts

---

## 📊 Example Interactions

### Example 1: Math Calculation
```
User: "What is 15% of 280?"
    ↓
LLM: "I'll calculate this using the math tool"
    ↓
Tool Call: calculate(280 * 0.15)
    ↓
Server Response: 42
    ↓
LLM: "15% of 280 is 42"
```

### Example 2: Visualization
```
User: "Draw a rotating triangle"
    ↓
LLM: "I'll use manim to create that"
    ↓
Tool Call: draw_animation(shape="triangle", rotation=True)
    ↓
Server: Creates video file
    ↓
LLM: Returns path to animation
```

### Example 3: Data Management
```
User: "Log my coffee expense of $5"
    ↓
LLM: "I'll add that to your expenses"
    ↓
Tool Call: add_expense(amount=5, category="food", description="coffee")
    ↓
Server: Stores expense
    ↓
LLM: "Expense logged successfully"
```

---

## 🚀 Advanced Patterns

### Pattern 1: Multi-Step Tool Usage
```python
# LLM uses multiple tools in sequence
response = await llm_with_tools.ainvoke(
    "Calculate 10% tax on $500 and format the result"
)

# Resulting tool calls:
# 1. math.calculate(500 * 0.1)
# 2. format(result)
```

### Pattern 2: Error Handling
```python
try:
    result = await tool.ainvoke(args)
except Exception as e:
    # Send error back to LLM for recovery
    error_message = f"Tool failed: {str(e)}"
    # LLM can try alternative approach
```

### Pattern 3: Tool Chaining
```python
# Call tools in sequence based on results
result1 = await tool1.ainvoke(input_data)
result2 = await tool2.ainvoke(result1)
result3 = await tool3.ainvoke(result2)
```

---

## 🔐 Security Considerations

### 1. Server Validation
```python
# Verify server identity before connecting
TRUSTED_SERVERS = ["math.example.com", "expense.example.com"]

if server_url not in TRUSTED_SERVERS:
    raise SecurityError("Untrusted server")
```

### 2. Tool Restrictions
```python
# Limit what tools are available
ALLOWED_TOOLS = ["calculate", "format"]

available_tools = [t for t in all_tools if t.name in ALLOWED_TOOLS]
```

### 3. Rate Limiting
```python
# Prevent tool abuse
from tenacity import retry, stop_after_attempt

@retry(stop=stop_after_attempt(3))
async def safe_tool_call(tool, args):
    return await tool.ainvoke(args)
```

---

## 📈 Performance Tips

1. **Async Operations**
   - Use `ainvoke()` for non-blocking calls
   - Parallel tool execution when possible

2. **Caching**
   - Cache tool results for repeated calls
   - Reduces latency and costs

3. **Batch Operations**
   - Group multiple tool calls
   - Send together when possible

4. **Connection Pooling**
   - Reuse connections to servers
   - Reduces connection overhead

---

## 🔍 Debugging MCP

### Enable Verbose Logging
```python
import logging
logging.basicConfig(level=logging.DEBUG)

# Now see detailed MCP communication
```

### Inspect Tool Definitions
```python
tools = await client.get_tools()
for tool in tools:
    print(f"Tool: {tool.name}")
    print(f"Description: {tool.description}")
    print(f"Parameters: {tool.execute}")
```

### Test Individual Tools
```python
# Test tool before using in LLM
test_result = await tool.ainvoke({"x": 5, "y": 3})
print(test_result)
```

---

## 📚 Building Custom MCP Servers

### Basic Server Structure
```python
from mcp.server import Server
from mcp.server.stdio import stdio_server

app = Server("my-server")

@app.call_tool()
async def calculate(operation: str, a: float, b: float):
    """Perform mathematical operations"""
    if operation == "add":
        return a + b
    elif operation == "multiply":
        return a * b
    # ... more operations

if __name__ == "__main__":
    stdio_server(app).run()
```

---

## ⚙️ Configuration Guide

### Environment Setup
```bash
# Install dependencies
pip install langchain-mcp-adapters

# Set environment variables
export MATH_SERVER_PATH="/path/to/math_server"
export EXPENSE_API_URL="https://expense.example.com"
export MANIM_EXECUTABLE="/usr/bin/manim"
```

### Server Configuration
```python
SERVERS = {
    "server_name": {
        "transport": "stdio" or "streamable_http",
        # For stdio:
        "command": "executable_path",
        "args": ["arg1", "arg2"],
        "env": {"VAR": "value"},
        # For HTTP:
        "url": "https://api.example.com/mcp",
        "headers": {"Authorization": "Bearer token"}
    }
}
```

---

## ❓ Common Questions

**Q: What's the difference between MCP transport types?**
A: stdio is local (fast, no network). HTTP is remote (slow, but remote access).

**Q: Can I create custom tools?**
A: Yes, write an MCP server with your tools and connect it.

**Q: How are tool results returned to the LLM?**
A: As ToolMessage objects with tool_call_id and content.

**Q: Can multiple tools be called in parallel?**
A: Yes, but the LLM must request them. You can execute them in parallel.

**Q: What if a tool fails?**
A: Return error to LLM as ToolMessage. LLM can try alternative approach.

---

## 🔗 Related Topics

- **Models/** - Understand LLM binding with tools
- **Chains/** - Use tools in chain workflows
- **Prompts/** - Craft effective tool-using prompts

---

## 📚 Quick Reference

```python
# Import MCP client
from langchain_mcp_adapters.client import MultiServerMCPClient

# Define servers
servers = {
    "math": {...},
    "expense": {...}
}

# Create client
client = MultiServerMCPClient(servers)

# Get tools
tools = await client.get_tools()

# Bind to LLM
llm_with_tools = llm.bind_tools(tools)

# Use
response = await llm_with_tools.ainvoke("query")
```

---

**Ready to connect external tools to your LLMs? Start with client1.py! 🔗**

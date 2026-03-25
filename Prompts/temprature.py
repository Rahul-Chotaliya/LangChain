from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file    

# Initialize Google Generative AI model
model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",   # or "gemini-pro", etc.
    temperature=1.5
)


# Invoke model
response = model.invoke([
    HumanMessage(content="Write a 5 line poem on cricket")
])

# Print result
# print(response.content)
print(response.content[0]["text"])
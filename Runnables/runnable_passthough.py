from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_core.runnables import RunnableLambda, RunnablePassthrough, RunnableSequence , RunnableParallel

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.7)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = "write a joke about {topic}",
    input_variables=["topic"]
)

joke_gen_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    ""
})
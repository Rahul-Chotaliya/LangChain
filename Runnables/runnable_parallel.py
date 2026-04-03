from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableLambda,RunnableParallel

load_dotenv()

prompt1 = PromptTemplate(
    template = "write a joke about {topic}",
    input_variables=["topic"]
)

prompr2 = PromptTemplate(
    template = "write a pun about {topic}",
    input_variables=["topic"]
)   

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.7)

parser = StrOutputParser()

run_parallel = RunnableParallel({
    "joke": RunnableLambda(lambda x: joke_gen_chain.invoke(x)), # type: ignore
    "pun": RunnableLambda(lambda x: pun_gen_chain.invoke(x)) # type: ignore
})

result = run_parallel.invoke({"topic": "programming"})

print("Joke: ", result["joke"])
print("Pun: ", result["pun"])
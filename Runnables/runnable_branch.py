from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda, RunnablePassthrough, RunnableSequence # type: ignore


load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.7)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = "what is the today time and date?",
    input_variables=[]
)

prompt2 = PromptTemplate(
    template = "Good Evening! Rahul...",
    input_variables=[]
)

prompt3 = PromptTemplate(
    template = "Good Morning! Rahul...",
    input_variables=[]
)

time_chain = prompt1 | model | parser

branch_chain = RunnableBranch(
    (lambda x: x.strip().split(",")[0].split(":")[0]>12, prompt2 | model | parser),
    (prompt3 | model | parser)
)

sequence_chain = RunnableSequence(time_chain, branch_chain)

print(sequence_chain.invoke({}))

sequence_chain.get_graph().print_ascii()
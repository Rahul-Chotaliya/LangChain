from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableParallel,RunnableLambda
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.7)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Write a Short and simple 5 dot points summary with latest information about {topic}:",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Write a Short and simple 3 dot points summary with latest information about {topic} competitors:",
    input_variables=["topic"]
)

prompt3 = PromptTemplate(
    template="Merge the provided info and write a single report about {topic1} and its competitors {topic2}: \n",
    input_variables=["topic1", "topic2"]
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "topic1" : prompt1 | model | parser,
    "topic2" : prompt2 | model | parser
})

merge_chain = prompt3 | model | parser

main_chain = parallel_chain | merge_chain

print(main_chain.invoke({"topic": "Virat Kohli"}))

main_chain.get_graph().print_ascii()
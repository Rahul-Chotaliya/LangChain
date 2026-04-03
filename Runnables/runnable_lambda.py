from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableLambda,RunnablePassthrough, RunnableParallel

load_dotenv()

prompt = PromptTemplate(
    template = "write a joke about {topic}",
    input_variables=["topic"]
)

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.7)
# model = ChatOpenAI()

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)


parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "word_count": RunnableLambda(lambda x: len(x.split())) # type: ignore                                 
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({"topic": "programming"})

final_result  = """ {} \n word count : {}""".format(result["joke"], result["word_count"])

print(final_result)


from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
from langchain_core.runnables import RunnablePassthrough # type: ignore
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
from typing import Literal

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.7)

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="The sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback text into positive or negative: \n {feedback} \n {format_instructions}",
    input_variables=["feedback"],
    partial_variables={"format_instructions": parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model  | parser2

prompt2 = PromptTemplate(
    template = "Write an appropriate response to this positive feedback: \n {feedback}",
    input_variables=["feedback"]
)

prompt3 = PromptTemplate(
    template = "Write an appropriate response to this negative feedback: \n {feedback}",
    input_variables=["feedback"]
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive" , prompt2 | model| parser),
    (lambda x: x.sentiment == "negative" ,prompt3 | model | parser),
    RunnableLambda(lambda x: "could not classify sentiment")
)

chain = classifier_chain | branch_chain

print(chain.invoke({"feedback": "I love this product! It has changed my life for the better."}))

# chain.get_graph().
chain.get_graph().print_ascii()
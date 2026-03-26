from langchain_google_genai import GoogleGenerativeAI
from typing import List, Optional, Literal
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


load_dotenv()

model = GoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.7)

class ReviewOutput(BaseModel):
    key_themes : List[str] = Field(..., description="Key themes mentioned in the review")
    summary : str = Field(..., description="A brief summary of the review")
    sentiment : Literal["positive", "negative", "neutral"] = Field(..., description="The overall sentiment of the review")
    pros : Optional[List[str]] = Field(None, description="Positive aspects mentioned in the review, if any")
    cons : Optional[List[str]] = Field(None, description="Negative aspects mentioned in the review, if any")
    name : Optional[str] = Field(None, description="The name of the reviewer")
    
parser = PydanticOutputParser(pydantic_object=ReviewOutput)
template = PromptTemplate(
    template= "Write a detailed review analysis on following review. \n {format_instruction} \n Review: {review}",
    input_variables=["review"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({"review": """I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.      
The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.
However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things
    Google already provides? The $1,300 price tag is also a hard pill to swallow.
Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
Review by Rahul Chotaliya
"""})

print(result)
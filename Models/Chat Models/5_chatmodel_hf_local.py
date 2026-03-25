from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline(
    model="google/flan-t5-xl",
    task="text2text-generation",
    pipeline_kwargs={"temperature": 0.9,"max_new_tokens": 100}    
)

model = ChatHuggingFace(llm=llm)
response = model.invoke("What year did the first man land on the moon?")
print(response.content)
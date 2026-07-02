from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from typing import TypedDict
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)

#Schema how the strucured output will look like 
class Review(TypedDict):
    summary:str
    sentiment:str

structured_model=model.with_structured_output(Review)


result=structured_model.invoke("""Problem: For deep extraction tasks, your schema may exceed standard prompt lengths, which can cause token
limits, memory consumption issues, or latency.""")

print(type(result))
print(result["summary"])
print(result['sentiment'])
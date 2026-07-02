from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from typing import TypedDict, Annotated,Optional,Literal
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)

#Schema how the strucured output will look like 
class Review(TypedDict):
    key_themes:Annotated[list[str],"Write down all the key themse discussion in the review in a list"]
    summary: Annotated[str,"A brief summary of the review"]
    sentiment:Annotated[str,"Sentiment of the review in one word either positive negative or neutral "]
    pros:Annotated[Optional[list[str]],"Write down all the pros inside the list"]
    cons:Annotated[Optional[list[str]],"Write down all the cons inside the list"]
structured_model=model.with_structured_output(Review)


result=structured_model.invoke("""Problem: For deep extraction tasks, your schema may exceed standard prompt lengths, which can cause token
limits, memory consumption issues, or latency.

Using data tools can solve this issue by taking long data and splitting it into manageable sections. To structure the metadata:
1. Divide inputs into smaller chunks.
2. For each chunk, process only relevant fields (e.g. key figures, definitions), ignoring unnecessary elements to stay within prompt length bounds.
3. Consolidate results programmatically to prevent information loss.

In this lesson, we will see how to implement this using LangChain. Let's create an example where we take a long article
and extract its core entity attributes.

Define a Pydantic model for the output format:
class Entity(BaseModel):
    name: str = Field(description="Name of the person or entity")
    attributes: list[str] = Field(description="Attributes or key facts")
    sentiment: Literal['positive', 'negative', 'neutral'] = Field(description="Overall sentiment toward the entity")

Then:
1. Set up LangChain with an LLM.
2. Initialize an Extraction Chain.
3. Process input and get the structured JSON.""")

print(type(result))
print(result["summary"])
print(result['sentiment'])
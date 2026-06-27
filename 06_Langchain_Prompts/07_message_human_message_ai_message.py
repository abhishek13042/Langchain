from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)
#System mesaage the messgae wihc u sent before the using ai like u are helpful assitant
messages=[
    SystemMessage(content='Yout are a helpful '),
    HumanMessage(content="Tell me about the langchain ")
]

result=model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)
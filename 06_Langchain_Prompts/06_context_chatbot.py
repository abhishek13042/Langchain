# Whar we wukk do in order to have the context is we will make 
#chat history list in where 
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)
chat_history=[]

while True:
    user_input=input('You:')
    chat_history.append(user_input)
    if user_input=="exit":
        break
    result=model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI:",result.content)


print(chat_history)

## Problem arsies here is that when the chat hsitory become larger it will a
## hvae problem in understandinh ehihc was humna message and which whas ai reponse
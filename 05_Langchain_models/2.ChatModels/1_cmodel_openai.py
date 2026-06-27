from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
model= ChatOpenAI(model="gpt-4",temperature=0.2,max_completion_tokens="50")
model.invoke("What is capital of india ")

#HEre the ourpit us content m
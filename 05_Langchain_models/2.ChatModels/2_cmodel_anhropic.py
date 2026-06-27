from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model=ChatAnthropic(model="Sonnet4.6")

results =model.invoke("What is capiral of india")

print(results.content)

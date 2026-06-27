from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 
embedding= OpenAIEmbeddings(model='')
load_dotenv()

documents = [
    "Virat Kohli is one of the greatest modern batsmen, known for his consistency, aggression, and ability to chase targets under pressure. He has scored thousands of runs across all formats for India.",

    "Rohit Sharma is an elegant opening batsman and the captain of the Indian cricket team. He holds the record for the highest individual score in One Day Internationals with 264 runs.",

    "MS Dhoni is regarded as one of the best wicketkeeper-batsmen and captains in cricket history. He led India to victories in the 2007 T20 World Cup, 2011 Cricket World Cup, and 2013 Champions Trophy.",

    "Sachin Tendulkar, often called the 'God of Cricket', is the highest run-scorer in international cricket. His career spanned 24 years and inspired generations of cricketers.",

    "Jasprit Bumrah is one of the world's leading fast bowlers, famous for his unique bowling action and deadly yorkers. He has been a key player for India across all formats."
]

query="tell me about the virat kohli "
doc_embeddings= embedding.embed_documents(documents)
query_embeddings=embedding.query_embeddings(query)

scores=cosine_similarity([query_embeddings],doc_embeddings)[0]

index,score =sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

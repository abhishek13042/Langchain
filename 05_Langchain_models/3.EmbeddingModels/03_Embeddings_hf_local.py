from langchain_huggingface import HuggingFaceEmbeddings

embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text="Delhi is capital of India"
vector=embedding.embed_query(text)

print(str(vector))

#we can do same as previous for the doucments too 
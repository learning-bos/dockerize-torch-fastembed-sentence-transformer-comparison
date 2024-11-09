from langchain_huggingface import HuggingFaceEmbeddings

# Define embedding function
def extract_embedding(document: str, model_path="BAAI/bge-small-en-v1.5"):
    """Extract embedding using HF Embedding 
       with a default model from HF if no path is specify
    """

    embed_model = HuggingFaceEmbeddings(model_name=model_path)
    embedding = embed_model.embed_query(text=document)
    return embedding

documents = [
    "passage: Hello, World!",
    "query: Hello, World!",
    "passage: This is an example passage.",
    "fastembed is supported by and maintained by Qdrant."
]
embedding = extract_embedding(documents[0])
assert len(embedding) == 384
assert type(embedding[0]) == float
print("All good")

from sentence_transformers import SentenceTransformer
from numpy import float32

# 1. Load a pretrained Sentence Transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# The sentences to encode
documents = [
    "passage: Hello, World!",
    "query: Hello, World!",
    "passage: This is an example passage.",
    "fastembed is supported by and maintained by Qdrant."
]
# 2. Calculate embeddings by calling model.encode()
embeddings = model.encode(documents)
#print(embeddings.shape)
assert len(embeddings[0]) == 384
assert type(embeddings[0][0]) == float32
print("All good")

# 3. Calculate the embedding similarities
#similarities = model.similarity(embeddings, embeddings)
#print(similarities)
####### Pandas Implementation #######____________________________________________________________________
# import pandas as pd
# # Create sample data
# data = {
#     "Name": ["Alice", "Bob", "Charlie"],
#     "Age": [24, 30, 28],
#     "City": ["Chennai", "Salem", "Bangalore"]
# }
# # Create DataFrame
# df = pd.DataFrame(data)
#
# # Show dataset
# print(df)
#
# # Filter people older than 25
# filtered = df[df["Age"] > 25]
# print(filtered)

####### FAISS Implementation ######____________________________________________________________________
# import faiss
# import numpy as np
#
# # Example embeddings
# vectors = np.array([
#     [0.1, 0.2],
#     [0.2, 0.1],
#     [0.9, 0.8],
#     [0.8, 0.9]
# ]).astype("float32")
#
# # Create index
# index = faiss.IndexFlatL2(2)
#
# # Add vectors
# index.add(vectors)
#
# # Query vector
# query = np.array([[0.1, 0.3]]).astype("float32")
#
# D, I = index.search(query, k=2)
#
# print("Nearest vectors index:", I)
# print("Distance:", D)

###### spaCy ######____________________________________________________________________
# import spacy
#
# # Load NLP model
# nlp = spacy.load("en_core_web_sm")
#
# text = "Apple was founded by Steve Jobs in 1976."
#
# doc = nlp(text)
#
# # Named Entity Recognition
# for ent in doc.ents:
#     print(ent.text, ent.label_)

###### Hugging Face Transformers ######____________________________________________________________________
from transformers import AutoTokenizer, AutoModel
import torch

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

sentence = "Artificial Intelligence is powerful"

inputs = tokenizer(sentence, return_tensors="pt")
outputs = model(**inputs)

embedding = outputs.last_hidden_state
print(embedding.shape)
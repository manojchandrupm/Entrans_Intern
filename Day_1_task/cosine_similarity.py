########## normal code without using library #########
import math
sentence1 = "AI is amazing"
sentence2 = "Artificial intelligence is powerful"

words1 = sentence1.lower().split()
words2 = sentence2.lower().split()

vocab = list(set(words1 + words2))

def vector_count(words,vocab):
    res = []
    for word in vocab:
        count = words.count(word)
        res.append(count)
    return res
vec_1 = vector_count(words1,vocab)
vec_2 = vector_count(words2,vocab)

dot_product = []
for i in range(len(vocab)):
    dot_product.append(vec_1[i]*vec_2[i])
dot_product = sum(dot_product)

modulo_1 = math.sqrt(sum([v**2 for v in vec_1]))
modulo_2 = math.sqrt(sum([v**2 for v in vec_2]))

cos_sim = dot_product/(modulo_1*modulo_2)

print(f"Similarity Score: {cos_sim:.2f}") #// output:Similarity Score: 0.29


#########  using library TF-IDF #########

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

sentence1 = "AI is amazing"
sentence2 = "Artificial intelligence is powerful"

sentence1 = sentence1.lower().replace("ai", "artificial intelligence")
sentence2 = sentence2.lower()

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform([sentence1, sentence2])

similarity = cosine_similarity(vectors[0], vectors[1])

print("Similarity Score:", round(similarity[0][0], 2))#// output:Similarity Score: 0.6

# ########## using library ##########
from sentence_transformers import SentenceTransformer, util

# Load a valid pre-trained model
model = SentenceTransformer('all-mpnet-base-v2')

# Sentences
sentence1 = "AI is amazing"
sentence2 = "Artificial intelligence is powerful"

# Get sentence embeddings
embedding1 = model.encode(sentence1)
embedding2 = model.encode(sentence2)

# Compute cosine similarity
similarity = util.cos_sim(embedding1, embedding2)

print("Similarity Score:", round(similarity.item(), 2))#output:Similarity Score: 0.67
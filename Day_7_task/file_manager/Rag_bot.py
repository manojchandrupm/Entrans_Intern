from langchain_text_splitters import CharacterTextSplitter
from database import collection
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline

### extract the content from database and make it into chunks
def chunk_documents():
    docs = collection.find()
    text_chunks = []

    splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    for doc in docs:
        content = doc["content"]
        chunks = splitter.split_text(content)
        for chunk in chunks:
            text_chunks.append({
                "filename": doc["filename"],
                "chunk": chunk
            })
    return text_chunks

# print(chunk_documents())

### embedding the chunks to store in the vector db
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

### vector store
text_chunks = chunk_documents()
texts = [chunk["chunk"] for chunk in text_chunks]

vector_store = FAISS.from_texts(texts, embeddings)

### local LLM for generating answers
pipe = pipeline(
    "text-generation",
    model="gpt2",  # or "facebook/opt-125m" for better answers
    max_length=512
)

llm = HuggingFacePipeline(pipeline=pipe)

### retrieve top  3 chunks
retriever = vector_store.as_retriever(search_kwargs={"k": 3})

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="Use the following context to answer the question:\n\n{context}\n\nQuestion: {question}\nAnswer:"
)
llm_chain = LLMChain(llm=llm, prompt=prompt)

### Retrieval-based QA chain
qa_chain = RetrievalQA(
    retriever=retriever,
    combine_documents_chain=llm_chain
)
### Function to answer user queries
def answer_question(question):
    return qa_chain.invoke({"query": question})

print(answer_question("What is the content of the uploaded PDF?"))
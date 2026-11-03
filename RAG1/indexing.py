from dotenv import load_dotenv
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_cohere import CohereEmbeddings
from .file_reader import extract_paragraphs
import os

load_dotenv()

embedding = CohereEmbeddings(
    model="embed-multilingual-v3.0",
    cohere_api_key=os.getenv("COHERE_API_KEY")
)

vector_store = InMemoryVectorStore(embedding=embedding)

chunks = extract_paragraphs("pdfs/RAG_M1.pdf")

vector_store.add_texts(texts=chunks)

print(f"indexed {len(chunks)} chunks")
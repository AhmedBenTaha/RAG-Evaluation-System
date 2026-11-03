from .indexing import vectore_store
from langchain.tools import tool


@tool
def collecting_info(query: str) -> str:
    """
    Search the PDF knowledge base and retrieve the most relevant
    information based on the user's question.
    """
    docs = vectore_store.similarity_search(
        query=query,
        k=2
    )

    if not docs:
        return "No relevant information was found in the PDF."

    retrieved_context = [
        doc.page_content for doc in docs
    ]

    return "\n\n".join(retrieved_context)

import RAG1.tools as tl
from .prompts import system_agent_prompt
from langchain_openai import ChatOpenAI
from .tools import collecting_info
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from .objects import Answer
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize Groq LLM
llm = ChatOpenAI(
    base_url="https://api.groq.com/openai/v1",
    model="openai/gpt-oss-120b",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

# Create RAG Agent
agent = create_agent(
    model=llm,
    tools=[collecting_info],
    system_message=system_agent_prompt,
    response_format=Answer
)


def ask(question: str) -> dict:
    """Answer the user's question about the PDF."""

    tl.last_retrieved_context = []

    result = agent.invoke(
        {"messages": [HumanMessage(content=question)]}
    )

    structured_response = result["structured_response"]

    return {
        "answer": structured_response.answer,
        "context": structured_response.context
    }

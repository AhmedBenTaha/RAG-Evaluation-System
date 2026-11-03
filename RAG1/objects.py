from pydantic import BaseModel, Field


class Answer(BaseModel):
    answer: str = Field(
        description="A clear and accurate answer to the user's question."
    )

    context: str = Field(
        description="The relevant information retrieved from the PDF or other tools that supports the answer."
    )
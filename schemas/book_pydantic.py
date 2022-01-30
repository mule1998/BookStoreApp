from pydantic import BaseModel


class Books(BaseModel):
    author_name: str
    title: str
    image: str
    quantity: int
    price: int
    description: str

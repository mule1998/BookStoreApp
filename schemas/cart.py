from pydantic import BaseModel


class Cart(BaseModel):
    book_id: int

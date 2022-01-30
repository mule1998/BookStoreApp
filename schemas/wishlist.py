from pydantic import BaseModel


class Wishlist(BaseModel):
    book_id: int

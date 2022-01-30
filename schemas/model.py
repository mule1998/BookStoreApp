from pydantic import BaseModel


class Users(BaseModel):
    user_name: str
    email_id: str
    password: str
    mobile_no: str


class Books(BaseModel):
    author_name: str
    title: str
    image: str
    quantity: int
    price: int
    description: str

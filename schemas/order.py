from pydantic import BaseModel


class Order(BaseModel):
    """
    Contains address
    """
    address: str

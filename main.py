import uvicorn
from fastapi import FastAPI
from routers import user_api, book_api, wishlist_api, cart_api, order_api

app = FastAPI(title="Book Store App")

app.include_router(user_api.route)
app.include_router(book_api.route)
app.include_router(wishlist_api.route)
app.include_router(cart_api.route)
app.include_router(order_api.route)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)

from fastapi import FastAPI
from database import engine, Base
from api import users, products, orders

# Tables create karne ke liye
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(users.router)
app.include_router(products.router)
app.include_router(orders.router)
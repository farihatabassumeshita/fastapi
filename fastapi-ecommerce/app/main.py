from fastapi import FastAPI
from service.products import get_all_products

app = FastAPI()

#static route
@app.get("/")
def root():
    return {"message": "Welcome to Fastapi"}

#dynamic route
# @app.get("/products/{id}")
# def get_products(id: int):
#     products = ['Laptop', 'Mouse', 'Keyboard', 'Camera']
#     return products[id]

@app.get("/products")
def get_products():
    return get_all_products()


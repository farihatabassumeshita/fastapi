from fastapi import FastAPI, HTTPException, Query
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

#getting all product
# @app.get("/products")
# def get_products():
#     return get_all_products()

#product Query from all products
@app.get("/products")
def get_product_list(
    name: str = Query(
        default= None,
        min_length= 1,
        max_length= 50,
        description="Search by product name (case insensitive)",
    ),
    sort_by_price: bool = Query(
        default= False,
        description= "Sort products By Price"
    ),
    order: str = Query(
        default="asc", description="Sort order when sort_by_price=true (asc,desc)"
    ), 
    limit : int = Query(
        default=10,
        ge=1,
        le=100,
        description="Number of items to return"
    )
):
    products = get_all_products()
    if name:
        lower = name.strip().lower()
        products = [p for p in products if lower in p.get("name").lower()]

        if not products:
            raise HTTPException(status_code=404, detail=f"No product found matching name={name}")
    
    if sort_by_price:
        reverse = order == "desc"
        products = sorted(products, key = lambda p:p.get("price", 0), reverse=reverse)

    total = len(products)
    products = products[0:limit]
    return{
        "total":total,
        "item":products
    }


from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from database import get_connection

app = FastAPI(title="Product Display API", version="1.0.0")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
    )


@app.get("/products", response_class=HTMLResponse)
def products(request: Request):
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT id, name, price FROM products ORDER BY id")
        product_list = cursor.fetchall()
    finally:
        cursor.close()
        connection.close()

    return templates.TemplateResponse(
        request=request,
        name="product.html",
        context={"products": product_list},
    )

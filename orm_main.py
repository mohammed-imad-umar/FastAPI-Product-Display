
import os
from urllib.parse import quote_plus

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from models import Base, Product

load_dotenv()

DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD", ""))
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "product_store")

DATABASE_URL = (
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Product Display API - ORM",
    version="1.0.0"
)

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html"
    )


@app.get("/products", response_class=HTMLResponse)
def products(request: Request):
    with SessionLocal() as db:
        product_list = db.scalars(
            select(Product).order_by(Product.id)
        ).all()

        products_data = [
            (p.id, p.name, p.price)
            for p in product_list
        ]

    return templates.TemplateResponse(
        request=request,
        name="product.html",
        context={"products": products_data},
    )

# Product Display Application

A simple assignment project based on the provided class code. It uses FastAPI, Jinja2 and MySQL Connector/Python (PDBC-style direct SQL) to fetch and display product records. An optional SQLAlchemy ORM version is included in `orm_main.py`.

## 1. Create the database

Open MySQL Workbench and execute the contents of `schema.sql`.

## 2. Install dependencies (Windows / VS Code)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 3. Set database credentials

Set environment variables in the same terminal. Replace the password with your local MySQL password:

```powershell
$env:DB_HOST="localhost"
$env:DB_USER="root"
$env:DB_PASSWORD="your_mysql_password"
$env:DB_NAME="product_store"
```

## 4. Run the PDBC version first

```powershell
uvicorn main:app --reload
```

Open `http://127.0.0.1:8000/products`. FastAPI's interactive docs are at `http://127.0.0.1:8000/docs`.

## 5. Optional SQLAlchemy ORM version

Install dependencies as above and set `DATABASE_URL`, for example:

```powershell
$env:DATABASE_URL="mysql+mysqlconnector://root:your_mysql_password@localhost/product_store"
uvicorn orm_main:app --reload
```

The ORM version uses the same `products` table and Jinja2 template. Run and verify the PDBC version before trying the ORM version.

## Files

- `openapi.yaml`: initial OpenAPI specification, as requested by the trainer
- `main.py`, `database.py`: primary direct-SQL / PDBC-style implementation
- `orm_main.py`, `models.py`: optional SQLAlchemy ORM implementation
- `templates/`: Jinja2 HTML templates
- `schema.sql`: database and sample data setup

This project uses only the features needed for the assignment; it does not implement authentication, cart or checkout features.

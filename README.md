# ✨ Product Display Application

### A modern FastAPI + MySQL project with a premium glass-inspired experience.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL">
  <img src="https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white" alt="Jinja2">
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy">
</p>

<p align="center">
  <a href="https://github.com/mohammed-imad-umar/FastAPI-Product-Display">
    <img src="https://img.shields.io/badge/⭐_VIEW_SOURCE_CODE-GitHub-181717?style=for-the-badge&logo=github" alt="View Source Code">
  </a>
  <a href="http://127.0.0.1:8000/docs">
    <img src="https://img.shields.io/badge/⚡_API_DOCUMENTATION-Swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=black" alt="API Documentation">
  </a>
  <a href="http://127.0.0.1:8000/products">
    <img src="https://img.shields.io/badge/🛍️_EXPLORE_PRODUCTS-Local_Demo-06B6D4?style=for-the-badge" alt="Explore Products">
  </a>
</p>

> **Live Demo:** Deployment pending. The local demo links above work only when the application is running on your computer.

---

## 🚀 Overview

Product Display is a Python web application that retrieves product records from a MySQL database and renders them as HTML pages using FastAPI and Jinja2.

The project includes two implementations:

- **PDBC-style direct SQL:** MySQL Connector/Python.
- **SQLAlchemy ORM:** Database interaction through models and ORM queries.

## ✨ Features

- 📦 Display products stored in MySQL.
- ⚡ FastAPI routes with interactive Swagger documentation.
- 🎨 Jinja2 HTML templates.
- 🗄️ Direct SQL and optional SQLAlchemy ORM implementations.
- 🔐 Environment-based database configuration.
- 📱 Responsive, glass-inspired website UI.
- 📄 OpenAPI specification included.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application programming |
| FastAPI | Web framework and routes |
| MySQL | Product database |
| MySQL Connector/Python | Direct database connection |
| SQLAlchemy | Optional ORM implementation |
| Jinja2 | HTML template rendering |
| Uvicorn | Development server |

## 📁 Project Structure

```text
FastAPI-Product-Display/
│
├── templates/
│   ├── home.html
│   └── product.html
│
├── .env.example
├── .gitignore
├── database.py
├── main.py
├── models.py
├── orm_main.py
├── openapi.yaml
├── requirements.txt
├── schema.sql
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/mohammed-imad-umar/FastAPI-Product-Display.git
cd FastAPI-Product-Display
```

### 2. Create a virtual environment

On Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Set up MySQL

Open MySQL Workbench and execute the SQL statements in `schema.sql`. This creates the `product_store` database, the `products` table, and sample records.

### 5. Configure database credentials

Create a `.env` file in the project root using `.env.example` as a reference.

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=product_store
```

Replace `your_mysql_password` with your own local MySQL password. Do not upload `.env` to GitHub.

### 6. Run the direct SQL implementation

```powershell
uvicorn main:app --reload
```

Open these links while the server is running:

- **Home:** http://127.0.0.1:8000/
- **Products:** http://127.0.0.1:8000/products
- **Interactive API Docs:** http://127.0.0.1:8000/docs
- **OpenAPI JSON:** http://127.0.0.1:8000/openapi.json

### 7. Run the optional ORM implementation

Stop the first server with `Ctrl + C`, then run:

```powershell
uvicorn orm_main:app --reload --port 8001
```

Open:

- **ORM Home:** http://127.0.0.1:8001/
- **ORM Products:** http://127.0.0.1:8001/products
- **ORM API Docs:** http://127.0.0.1:8001/docs

Both implementations use the same MySQL database and product table.

## 📖 API Routes

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Display the home page |
| GET | `/products` | Display database products |
| GET | `/docs` | Interactive Swagger UI |
| GET | `/openapi.json` | Generated OpenAPI JSON |

The HTML routes render web pages; they are not JSON product-list endpoints.

## 🔒 Security Notes

- Keep database passwords in `.env`.
- Never commit credentials, `.env`, or virtual environment files.
- Use a dedicated database account with limited privileges for production deployments.
- Configure HTTPS and production settings before hosting publicly.

## 🚧 Deployment Status

**Status: Local development ready; public deployment pending.**

The application can be tested locally after completing the setup steps. The localhost links are not public demo links and will not work for other users on GitHub.

## 👨‍💻 Author

**Mohammed Imad Umar**

- GitHub: [@mohammed-imad-umar](https://github.com/mohammed-imad-umar)
- Project Repository: [FastAPI Product Display](https://github.com/mohammed-imad-umar/FastAPI-Product-Display)

---

<p align="center">
  Built with ❤️ using Python, FastAPI and MySQL.
</p>
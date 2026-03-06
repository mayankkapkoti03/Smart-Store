# Smart Store Backend

A backend API for a Smart Store system built using **FastAPI**.
This project demonstrates backend development concepts such as **authentication, role-based authorization, pagination, filtering, logging, and environment configuration**.

---

##  Features

* User Registration and Login
* JWT Authentication
* Role-Based Authorization (Admin / User)
* Product CRUD APIs
* Product Search
* Filtering and Sorting
* Pagination
* Structured Logging
* Environment Variables (.env)
* Basic API Testing with pytest

---

##  Tech Stack

* Python
* FastAPI
* SQLAlchemy
* Pydantic
* SQLite
* JWT (python-jose)
* Passlib (bcrypt)
* pytest
* Git & GitHub

---

##  Project Structure

```
smart-store-backend
│
├── app/
│   ├── auth/
│   │   ├── hashing.py
│   │   ├── jwt_handler.py
│   │   └── dependencies.py
│   │
│   ├── routers/
│   │   ├── auth.py
│   │   └── product.py
│   │
│   ├── services/
│   │   ├── auth_service.py
│   │   └── product_service.py
│   │
│   ├── config.py
│   ├── database.py
│   ├── logger.py
│   ├── models.py
│   └── schemas.py
│
├── tests/
│   └── test_auth.py
│
├── requirements.txt
└── main.py
```

---

##  Installation

### Clone the repository

```
git clone https://github.com/YOUR_USERNAME/smart-store-backend.git
cd smart-store-backend
```

### Create virtual environment

```
python -m venv venv
```

Activate it:

Windows

```
venv\Scripts\activate
```

Mac/Linux

```
source venv/bin/activate
```

### Install dependencies

```
pip install -r requirements.txt
```

### Run the server

```
uvicorn app.main:app --reload
```

Open Swagger docs:

```
http://127.0.0.1:8000/docs
```

---

##  API Endpoints

### Authentication

| Method | Endpoint       | Description                |
| ------ | -------------- | -------------------------- |
| POST   | /auth/register | Register user              |
| POST   | /auth/login    | Login user                 |
| GET    | /auth/me       | Get current logged in user |

---

### Products

| Method | Endpoint         | Description       |
| ------ | ---------------- | ----------------- |
| POST   | /products        | Create product    |
| GET    | /products        | Get all products  |
| GET    | /products/search | Search products   |
| GET    | /products/{id}   | Get product by ID |
| PATCH  | /products/{id}   | Partial update    |
| PUT    | /products/{id}   | Full update       |
| DELETE | /products/{id}   | Delete product    |

---

##  Authorization

Admin users can:

* Create products
* Update products
* Delete products

Normal users can:

* View products
* Search products

---

##  Running Tests

Run tests using:

```
python -m pytest
```

---

##  Author

Mayank Kapkoti
B.Tech CSE Student

# 🛒 Smart Store – Full Stack E-commerce Application

A full-stack e-commerce application built using FastAPI (backend) and React (frontend). 
The system supports authentication, product management, cart operations with quantity handling, and order processing.

This project demonstrates real-world backend architecture with modular design, REST APIs, and database management using SQLAlchemy.

---

## ✨ Features

### 🔐 Authentication
- User Registration & Login
- JWT Authentication
- Role-Based Authorization (Admin / User)

### 🛍️ Product Management
- Product CRUD APIs
- Search, Filtering, Sorting
- Pagination

### 🛒 Cart System
- Add to Cart
- Remove from Cart
- Quantity Increase/Decrease

### 📦 Order System
- Place Order from Cart
- Order Data Storage

### ⚙️ Backend Features
- Modular Architecture (Router + Service Pattern)
- SQLAlchemy ORM
- Environment Variables (.env)
- Structured Logging

### 🧪 Testing
- Basic API Testing using pytest

### 🌐 Frontend
- React-based UI
- API integration using Axios

---

## ⚙️ Tech Stack

### Backend
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite / PostgreSQL
- JWT (python-jose)
- Passlib (bcrypt)

### Frontend
- React
- Axios

### Tools
- Git & GitHub
- pytest

---

##  Project Structure

```
smart-store/
│
├── backend/
│   ├── app/
│   │   ├── auth/
│   │   │   ├── dependencies.py
│   │   │   ├── hashing.py
│   │   │   └── jwt_handler.py
│   │   │
│   │   ├── routers/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   ├── product.py
│   │   │   ├── cart.py
│   │   │   └── order.py
│   │   │
│   │   ├── services/
│   │   │   ├── auth_service.py
│   │   │   ├── product_service.py
│   │   │   ├── cart_service.py
│   │   │   └── order_service.py
│   │   │
│   │   ├── core/                 # (optional but PRO 🔥)
│   │   │   ├── config.py
│   │   │   └── logger.py
│   │   │
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── product.py
│   │   │   ├── cart.py
│   │   │   └── order.py
│   │   │
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── product.py
│   │   │   ├── cart.py
│   │   │   └── order.py
│   │   │
│   │   ├── database.py
│   │   ├── main.py
│   │   └── __init__.py
│   │
│   ├── tests/
│   │   └── test_auth.py
│   │
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── public/
│   │   ├── index.html
│   │   └── ...
│   │
│   ├── src/
│   │   ├── api/
│   │   │   └── axios.js
│   │   │
│   │   ├── components/
│   │   │   └── ProductList.js
│   │   │
│   │   ├── pages/
│   │   │   ├── Login.js
│   │   │   ├── Products.js
│   │   │   └── Admin.js
│   │   │
│   │   ├── App.js
│   │   ├── index.js
│   │   └── index.css
│   │
│   ├── package.json
│   └── package-lock.json
│
├── README.md
└── .gitignore
```

---

##  Installation

### Clone the repository

```
git clone https://github.com/mayankkapkoti03/smart-store.git
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
cd backend
pip install -r requirements.txt
```

### Run the server

```
cd backend
python -m uvicorn app.main:app --reload
```

### Run Frontend

```
cd frontend
npm install
npm start
```

Open Swagger docs:

```
http://127.0.0.1:8000/docs
```

---

## 🚀 API Endpoints

---

### 🔐 Authentication

| Method | Endpoint       | Description                |
| ------ | -------------- | -------------------------- |
| POST   | /auth/register | Register user              |
| POST   | /auth/login    | Login user                 |
| GET    | /auth/me       | Get current logged in user |

---

### 🛍️ Products

| Method | Endpoint         | Description              |
| ------ | ---------------- | ------------------------ |
| POST   | /products        | Create product (Admin)   |
| GET    | /products        | Get all products         |
| GET    | /products/search | Search products          |
| GET    | /products/{id}   | Get product by ID        |
| PATCH  | /products/{id}   | Partial update (Admin)   |
| PUT    | /products/{id}   | Full update (Admin)      |
| DELETE | /products/{id}   | Delete product (Admin)   |

---

### 🛒 Cart

| Method | Endpoint        | Description                          |
| ------ | --------------- | ------------------------------------ |
| POST   | /cart/add       | Add product to cart                  |
| DELETE | /cart/remove    | Remove or decrease product quantity  |
| GET    | /cart           | Get user cart                        |

---

### 📦 Orders

| Method | Endpoint   | Description                     |
| ------ | ---------- | ------------------------------- |
| POST   | /orders    | Place order from cart           |
| GET    | /orders    | Get all orders of current user  |
| GET    | /orders/{id} | Get order details by ID       |

---
## 🔐 Authorization

### 👨‍💼 Admin Users can:
- Create products  
- Update products  
- Delete products  

### 👤 Normal Users can:
- View products  
- Search products  
- Add products to cart  
- Remove/decrease items from cart  
- Place orders  
- View their orders  

---

## 🧪 Running Tests & Author

Run tests using:

```bash
cd backend
python -m pytest
```
---

👨‍💻 Author:
Mayank Kapkoti  
B.Tech CSE Student

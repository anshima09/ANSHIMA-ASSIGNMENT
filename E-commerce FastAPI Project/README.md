
# 🛒 FastAPI E-commerce Backend

## 📖 Introduction

This repository features a complete RESTful API backend designed for an e-commerce platform using **FastAPI**. It delivers a secure and scalable architecture with functionality that includes:

* Admin product management
* User authentication
* Product browsing
* Cart management
* Order processing

---

## 🎯 Project Goals

This application aims to establish a reliable and extensible backend for online shopping systems, offering:

- 🔧 Full CRUD capabilities for admins on product data
- 🔐 Secure user authentication (sign-up, sign-in, password forgot and reset)
- 🔍 Product browsing via search and filters
- 🛒 Shopping cart features and dummy checkout
- 📦 Viewing order history and details

---

## 📋 Requirements

Ensure the following are installed and understood before setup:

- Python 3.9
- Postgres ( used as a database)
- Postman (for API requests testing)
- Knowledge of RESTful APIs

---

## ⚙️ Tools & Libraries Used

| Category         | Technology            |
|------------------|------------------------|
| Backend Framework | FastAPI               |
| ORM & DB         | SQLAlchemy + Postgres   |
| Auth Mechanism   | JWT via PyJWT         |
| Validation       | Pydantic              |
| Password Security| bcrypt                |
| DB Migration     | Alembic               |
| Logging          | Built-in logging      |
| Web Server       | Uvicorn               |

---

## 📁 Directory Layout

```
python_project/
├── alembic/
│   └── versions/
├── app/
│   ├── main.py
│   ├── core/
│   ├── auth/
│   ├── products/
│   ├── cart/
│   ├── orders/
│   ├── checkout/
│   ├── exceptions/
│   └── utils/
├── .env
├── alembic.ini
├── requirements.txt
└── .gitignore
```

---

## 🧑‍💻 Installation Guide

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
cd python_project
```

### Step 2: Set Up Virtual Environment

```bash
python -m venv venv
# Activate accordingly:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Packages

```bash
pip install -r requirements.txt
```

### Step 4: Set Environment Variables

Create a `.env` file with the following content:

```env
DATABASE_URL=sqlite:///./ecommerce.db
JWT_SECRET_KEY=your_jwt_key_here
JWT_ALGORITHM=HS256
EMAIL_SENDER=your_email_address
EMAIL_API_KEY=your_api_key
```

### Step 5: Apply Migrations

```bash
alembic upgrade head
```

### Step 6: Load Sample Data

```bash
python seed_data.py
```

### Step 7: Start the App

```bash
uvicorn app.main:app --reload
```

Access at [http://localhost:8000](http://localhost:8000)  
Interactive API docs at [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 API Usage & Testing

You can use the provided `postman_collection.json` to test endpoints via Postman.

### Main Endpoints

- **Authentication**: `/auth/signup`, `/auth/signin`, `/auth/forgot-password`, `/auth/reset-password`
- **Products (Admin)**: `/admin/products`
- **Products (Public)**: `/products`, `/products/search`, `/products/{id}`
- **Cart**: `/cart`
- **Checkout**: `/checkout`
- **Orders**: `/orders`, `/orders/{order_id}`

---

## 🔒 Security Highlights

- Passwords hashed with **bcrypt**
- **JWT tokens** for user sessions with RBAC
- Time-sensitive password reset tokens
- Input validation using **Pydantic**
- Custom error handling with structured logging

---

## 🧾 Database Overview

| Table                   | Fields/Info                                                |
|-------------------------|------------------------------------------------------------|
| `Users`                 | id, name, email, hashed password, role                     |
| `Products`              | id, name, description, price, stock, category, image url   |
| `Cart`                  | id, user id, product id, quantity                          |
| `PasswordResetTokens`   | id, user id, token, expiry time, usage status              |
| `Orders`                | id, user id, total amount, status, creation time           |
| `OrderItems`            | id, order id, product id, quantity, purchase-time price    |

---

## ❌ Error Response Standard

All API errors follow a consistent JSON structure:

```json
{
  "error": true,
  "message": "Description of the error",
  "code": 400
}
```

---

## 🚀 Deployment Tips

- Use **Uvicorn** for production deployment
- Ensure environment variables are used for sensitive data
- Regularly back up the database before migration runs

---

## 🧪 Manual Testing

Conduct manual testing to validate:

- User authentication flow
- Admin and product CRUD operations
- Cart management and dummy checkout
- Order listings

---

## 🧭 Next Steps

Future enhancements may include:

- Writing unit tests using **pytest**
- Adding **rate limiting** for abuse prevention
- Enabling real payment gateway integrations

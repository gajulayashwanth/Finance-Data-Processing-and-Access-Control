# Finance Data Processing and Access Control Backend

A Django REST Framework backend for managing financial records with role-based access control and dashboard summary APIs.

## Features

- Custom user model with roles: `ADMIN`, `ANALYST`, `VIEWER`
- JWT authentication using Simple JWT
- Financial record CRUD APIs
- Record filtering by transaction type and category
- Dashboard summary API for income, expenses, and net balance
- Backend access control using custom permissions
- SQLite-based persistence for simple local setup

## Tech Stack

- Python
- Django
- Django REST Framework
- Simple JWT
- SQLite
- python-dotenv

## Roles

- `ADMIN`: Full access to financial records
- `ANALYST`: Read-only access to financial records
- `VIEWER`: No access to financial record endpoints

## Main APIs

### User APIs
- `POST /api/users/register/`
- `POST /api/users/login/`
- `POST /api/users/token/refresh/`

### Finance APIs
- `GET /api/finance/records/`
- `POST /api/finance/records/`
- `GET /api/finance/records/{id}/`
- `PUT/PATCH /api/finance/records/{id}/`
- `DELETE /api/finance/records/{id}/`
- `GET /api/finance/dashboard/summary/`

## Record Fields

Each financial record includes:

- `amount`
- `transaction_type`
- `category`
- `date`
- `notes`
- `user`
- `created_at`

## Setup
```bash
git clone <your-repository-url>
cd finance-dashboard-backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install django djangorestframework djangorestframework-simplejwt python-dotenv
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

Environment Variables
Create a .env file:
SECRET_KEY=replace-with-your-own-secret-key
DEBUG=True

Notes
SQLite is used for simplicity
JWT is used for authentication
Financial summary currently returns global totals across records
The project focuses on backend structure, API design, and access control

Future Improvements
Pagination
Date-range filters
Category-wise analytics
Better test coverage
API documentation
Admin user management endpoints

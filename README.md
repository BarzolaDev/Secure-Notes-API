# To-Do List API (Authentication & Multi-user)

REST API built with FastAPI and MongoDB, focused on user authentication and data isolation.

## 🚀 Features
- User registration and login with password hashing (bcrypt)
- JWT-based authentication (OAuth2)
- Multi-user system (each user has private data)
- Full CRUD for tasks and lists

## 🛠️ Tech Stack
- Python (FastAPI)
- MongoDB
- JWT / OAuth2
- bcrypt

## 🔐 Authentication Flow
- Passwords are securely hashed before storage
- JWT tokens are generated on login
- Protected routes require authentication via Authorization header

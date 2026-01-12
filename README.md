# Secure User Authentication & Task Management API

A robust FastAPI application with JWT authentication and comprehensive task management features.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68.0+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🚀 Features

- **User Authentication**: Secure registration and login with JWT tokens
- **Password Security**: Bcrypt hashing for secure password storage
- **Protected Routes**: Authentication required for sensitive operations
- **Task Management**: Full CRUD operations for tasks
- **User-Specific Tasks**: Each task is linked to a specific user
- **Database**: SQLite for local development (easily upgradeable to PostgreSQL)

## 🛠 Tech Stack

- **FastAPI** - Modern, fast web framework for building APIs
- **Pydantic** - Data validation using Python type annotations
- **SQLAlchemy** - SQL toolkit and ORM
- **SQLite** - Lightweight database for development
- **JWT Authentication** - Secure token-based authentication
- **Uvicorn** - ASGI server for running FastAPI apps

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/farhaanthebillionaire/sua-tmapi.git
   cd sua-tmapi
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Unix/MacOS
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   uvicorn app.main:app --reload
   ```

The API will be available at `http://localhost:8000`

## 📚 API Documentation

Once the server is running, visit:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🔗 API Endpoints

### Authentication
- `POST /auth/register` - Register a new user
- `POST /auth/login` - Login and get JWT token

### Tasks (Protected - requires JWT token)
- `GET /tasks/` - Get all tasks for the current user
- `POST /tasks/` - Create a new task
- `GET /tasks/{task_id}` - Get a specific task
- `PUT /tasks/{task_id}` - Update a task
- `DELETE /tasks/{task_id}` - Delete a task

### Other
- `GET /` - Welcome message
- `GET /health` - Health check endpoint

## 💡 Usage Example

1. **Register a user**
   ```bash
   curl -X POST "http://localhost:8000/auth/register" \
   -H "Content-Type: application/json" \
   -d '{"username": "john", "email": "john@example.com", "password": "secret123"}'
   ```

2. **Login to get token**
   ```bash
   curl -X POST "http://localhost:8000/auth/login" \
   -H "Content-Type: application/json" \
   -d '{"username": "john", "password": "secret123"}'
   ```

3. **Create a task** (use the token from login)
   ```bash
   curl -X POST "http://localhost:8000/tasks/" \
   -H "Authorization: Bearer YOUR_JWT_TOKEN" \
   -H "Content-Type: application/json" \
   -d '{"title": "Buy groceries", "description": "Milk, eggs, bread"}'
   ```

4. **Get all tasks**
   ```bash
   curl -X GET "http://localhost:8000/tasks/" \
   -H "Authorization: Bearer YOUR_JWT_TOKEN"
   ```

## 📁 Project Structure

```
app/
├── main.py              # FastAPI application entry point
├── database.py          # Database configuration
├── models/
│   ├── user.py          # User database model
│   └── task.py          # Task database model
├── schemas/
│   ├── user.py          # User Pydantic schemas
│   └── task.py          # Task Pydantic schemas
├── routers/
│   ├── auth.py          # Authentication routes
│   └── tasks.py         # Task management routes
├── dependencies.py      # FastAPI dependencies
└── utils/
    └── security.py      # Security utilities (JWT, password hashing)
```

## 🔒 Security Notes

- **Secret Key**: The secret key in `utils/security.py` should be changed in production
- **Environment Variables**: Use environment variables for sensitive configuration
- **Production Database**: Consider using PostgreSQL in production instead of SQLite
- **HTTPS**: Always use HTTPS in production environments

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Credits

**Developed by:**
- **Farhaan** - Project owner and lead developer

This project was created and is maintained by Farhaan as a comprehensive authentication and task management solution.

## 📞 Support

If you have any questions or need support, please open an issue on GitHub.

---

⭐ If you find this project helpful, please give it a star!

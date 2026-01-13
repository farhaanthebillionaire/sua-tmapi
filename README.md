# Secure User Authentication & Task Management API

A robust FastAPI application with JWT authentication and comprehensive task management features.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95.2-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue)
![Render](https://img.shields.io/badge/Deployed%20on-Render-000000)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🚀 Features

- **User Authentication**: Secure registration and login with JWT tokens
- **Password Security**: Bcrypt hashing with 72-byte truncation for compatibility
- **Protected Routes**: OAuth2 Bearer token authentication
- **Task Management**: Full CRUD operations for tasks
- **User-Specific Tasks**: Each task is linked to a specific user
- **Database**: SQLite for local development, PostgreSQL for production
- **Auto-Documentation**: Interactive Swagger UI and ReDoc
- **Production Ready**: Deployed on Render with PostgreSQL database
- **Health Monitoring**: Health check endpoints for monitoring
- **Security Best Practices**: JWT expiration, SQL injection prevention

## 🛠 Tech Stack

- **FastAPI 0.95.2** - Modern, fast web framework for building APIs
- **Pydantic 1.10.12** - Data validation using Python type annotations
- **SQLAlchemy 2.0.23** - SQL toolkit and ORM
- **PostgreSQL** - Production database (Render managed)
- **SQLite** - Lightweight database for local development
- **JWT Authentication** - Secure token-based authentication with HS256
- **Uvicorn** - ASGI server for running FastAPI apps
- **Passlib** - Password hashing with bcrypt
- **Render** - Cloud deployment platform

## 📦 Installation

### Local Development

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
   # Option 1: Direct uvicorn
   python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
   
   # Option 2: Auto-open docs (recommended for development)
   python start_server.py
   ```

The API will be available at `http://localhost:8000` and documentation at `http://localhost:8000/docs`

### Production Deployment

**Deployed on Render:** https://sua-tmapi.onrender.com

The application is automatically deployed with:
- PostgreSQL database (`taskdb`)
- Environment variables configured
- SSL/TLS encryption
- Health monitoring

## 📚 API Documentation

### Local Development
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Production
- **Swagger UI**: `https://sua-tmapi.onrender.com/docs`
- **ReDoc**: `https://sua-tmapi.onrender.com/redoc`

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

### Authentication & Authorization
- **JWT Tokens**: 30-minute expiration with HS256 algorithm
- **Password Security**: Bcrypt hashing with 72-byte truncation
- **OAuth2 Bearer**: Standardized token authentication scheme
- **Environment Variables**: Sensitive data stored in environment

### Database Security
- **SQL Injection Prevention**: SQLAlchemy ORM parameterized queries
- **Data Validation**: Pydantic schemas for input validation
- **User Isolation**: Tasks are scoped to authenticated users

### Production Security
- **HTTPS/SSL**: Automatic SSL certificates on Render
- **Environment Variables**: Production secrets managed by Render
- **Database Encryption**: PostgreSQL with SSL connections
- **CORS Configuration**: Proper cross-origin request handling

### Development Security
- **Secret Key**: Change `SECRET_KEY` in production environment
- **Database**: Use PostgreSQL in production (configured on Render)
- **Monitoring**: Health endpoints for system monitoring

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Project Information

### Purpose
This project demonstrates modern Python development skills with a focus on building secure, scalable RESTful APIs.

### Developer
- **Developed by**: Farhaan
- **Certification**: Certified Agile Scrum Master
- **Focus**: Modern Python development with security best practices

### Technical Demonstration
This project showcases expertise in:
- FastAPI web framework and RESTful API development
- JWT authentication and security implementation
- Database design with SQLAlchemy ORM
- Production deployment on cloud platforms
- Code quality and maintainability
- Agile development practices

## 📞 Support

If you have any questions or need support, please open an issue on GitHub.

---

⭐ If you find this project helpful, please give it a star!

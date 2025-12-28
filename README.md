# Flask Projects

A collection of Flask applications demonstrating different use cases and patterns.

## Projects

### 1. REST API Training (`rest_api_training/`)

A RESTful API application demonstrating Flask-RESTful patterns and SQLAlchemy ORM.

**Features:**
- Video resource management (CRUD operations)
- People resource API
- Hello World endpoint
- SQLite database integration
- Request parsing and validation

**API Endpoints:**
- `GET /helloworld` - Get hello world message
- `GET /people/<name>` - Get person information
- `GET /video/<id>` - Get video by ID
- `POST /video/<id>` - Create new video
- `PATCH /video/<id>` - Partial update video
- `DELETE /video/<id>` - Delete video

**Getting Started:**
```bash
cd rest_api_training
python3 main.py
```

The API will run on `http://localhost:5000/`

**Testing:**
```bash
python3 test.py
```

## Installation

Each project has its own dependencies. Install them using:

```bash
pip install -r requirements.txt
```

### 2. Todo App (`todo_app/`)

A simple task management application built with Flask and SQLite.

**Features:**
- Create, read, update, and delete tasks
- Mark tasks as completed
- Set task priorities (Low, Medium, High)
- Add due dates to tasks
- Bootstrap-based responsive UI

**Getting Started:**
```bash
cd todo_app
uv run python app.py
```

Visit `http://localhost:5000/` in your browser.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2025 Wiktor Sędzimir

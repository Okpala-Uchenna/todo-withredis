# Flask Todo List Application with Redis

This is a simple Todo list web application built using Flask as the web framework and Redis as the backend data store. The application allows users to perform basic CRUD operations (Create, Read, Update, Delete) on todo tasks, with Redis storing task data.

## Project Structure

```
flask-todo/
│
├── app/
│   ├── app.py          # Main application code
│   ├── redis_client.py # Redis connection 
│   │   
│   └── templates/      # HTML templates
│       ├── index.html
│       └── edit.html
│
├── Dockerfile          # Docker instructions for building the app
├── docker-compose.yml  # Docker Compose file for running services
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── .gitignore          # Ignored files and directories for Gitflask-todo/
```
## Requirements

- Docker
- Docker Compose

### Python Libraries

- Flask: Web framework
- Redis: Python client for Redis

## Setup and Run

Follow these steps to get the app running with Redis in Docker containers.

### Step 1: Clone the repository

```bash
git clone https://github.com/Okpala-Uchenna/flask-todo.git
cd flask-todo
```

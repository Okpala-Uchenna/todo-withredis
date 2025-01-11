from flask import Flask, render_template, request, redirect, url_for
from shared.redis_client import redis_client  # Assuming this module initializes Redis connection

app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route("/")
def index():
    # Retrieve all task keys from Redis
    keys = redis_client.keys("task:*")
    todos = []

    for key in keys:
        todo = redis_client.hgetall(key)
        # Add task_id to each task dictionary for easier reference in templates
        todo["task_id"] = key
        # Convert "done" field from string to boolean
        todo["done"] = todo["done"] == "True"
        todos.append(todo)

    return render_template("index.html", todos=todos)


@app.route("/add", methods=["POST"])
def add():
    task = request.form["todo"]
    if task.strip():  # Ensure non-empty task
        # Generate a new task ID
        task_id = f"task:{len(redis_client.keys('task:*')) + 1}"
        # Store task in Redis with "done" initially set to "False"
        redis_client.hset(task_id, mapping={"task": task, "done": "False"})
    return redirect(url_for("index"))


@app.route("/edit/<task_id>", methods=["GET", "POST"])
def edit(task_id):
    # Fetch task from Redis
    todo = redis_client.hgetall(task_id)
    if not todo:
        return redirect(url_for("index"))  # Redirect if task not found

    if request.method == "POST":
        task = request.form["todo"]
        if task.strip():  # Ensure non-empty task
            redis_client.hset(task_id, "task", task)  # Update task in Redis
        return redirect(url_for("index"))
    
    # Render edit page with task details
    return render_template("edit.html", todo=todo, task_id=task_id)


@app.route("/check/<task_id>")
def check(task_id):
    # Fetch task from Redis
    todo = redis_client.hgetall(task_id)
    if todo:
        # Toggle "done" field in Redis
        redis_client.hset(task_id, "done", "False" if todo["done"] == "True" else "True")
    return redirect(url_for("index"))


@app.route("/delete/<task_id>")
def delete(task_id):
    # Delete task from Redis
    redis_client.delete(task_id)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

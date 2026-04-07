from db.database import get_connection


def create_project(name, description=""):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO projects (name, description) VALUES (?, ?)",
        (name, description)
    )

    conn.commit()
    conn.close()


def add_task(project_id, title):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (project_id, title) VALUES (?, ?)",
        (project_id, title)
    )

    conn.commit()
    conn.close()


def complete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tasks SET status = 'done' WHERE id = ?",
        (task_id,)
    )

    conn.commit()
    conn.close()


def get_tasks(project_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, title, status FROM tasks WHERE project_id = ?",
        (project_id,)
    )

    results = cursor.fetchall()
    conn.close()
    return results
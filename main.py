from db.database import init_db
from services.task_service import create_project, add_task, get_tasks


def main():
    # initialize database
    init_db()

    # create project
    create_project("Boot.dev", "Backend learning")

    # add task
    add_task(1, "Finish API lesson")

    # fetch + print tasks
    tasks = get_tasks(1)

    print("\n--- TASKS ---")
    for task in tasks:
        print(task)


if __name__ == "__main__":
    main()

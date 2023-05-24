from colors import *

def show_menu():
    colors_print(COLORS_MAGENTA, "==================")
    print(COLORS_MAGENTA + "|" + COLORS_RESET, COLORS_CYAN + "TODO LIST MENU" + COLORS_RESET, COLORS_MAGENTA + "|" + COLORS_RESET)
    print(COLORS_MAGENTA + "|" + COLORS_RESET, COLORS_CYAN + "--------------" + COLORS_RESET, COLORS_MAGENTA + "|" + COLORS_RESET)
    print(COLORS_MAGENTA + "|" + COLORS_RESET, COLORS_CYAN + "1. Add Task   " + COLORS_RESET, COLORS_MAGENTA + "|" + COLORS_RESET)
    print(COLORS_MAGENTA + "|" + COLORS_RESET, COLORS_CYAN + "2. View Tasks " + COLORS_RESET, COLORS_MAGENTA + "|" + COLORS_RESET)
    print(COLORS_MAGENTA + "|" + COLORS_RESET, COLORS_CYAN + "3. View Done  " + COLORS_RESET, COLORS_MAGENTA + "|" + COLORS_RESET)
    print(COLORS_MAGENTA + "|" + COLORS_RESET, COLORS_CYAN + "4. Tag as Done" + COLORS_RESET, COLORS_MAGENTA + "|" + COLORS_RESET)
    print(COLORS_MAGENTA + "|" + COLORS_RESET, COLORS_CYAN + "5. Quit       " + COLORS_RESET, COLORS_MAGENTA + "|" + COLORS_RESET)
    colors_print(COLORS_MAGENTA, "==================\n")


def add_task(todo_list):
    task = input("\nEnter Task: \n")
    todo_list.append(task)
    colors_print(COLORS_GREEN, "Task added.\n")


def view_tasks(todo_list):
    if len(todo_list) == 0:
        colors_print(COLORS_RED, "No tasks in the list!\n")
    else:
        print("\nTasks: ")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}\n")


def view_done(done_list):
    if len(done_list) == 0:
        colors_print(COLORS_RED, "No done tasks in the list!\n")
    else:
        print("\nDone Tasks: ")
        for index, task in enumerate(done_list, start=1):
            print(f"{index}. {task}\n")


def tag_as_done(todo_list, done_list):
    if len(todo_list) == 0:
        colors_print(COLORS_RED, "No tasks in the list!\n")
    else:
        view_tasks(todo_list)
        task_index = int(input("\nEnter the index of the task to mark as done: "))
        if task_index < 1 or task_index > len(todo_list):
            colors_print(COLORS_RED, "Invalid task index.\n")
        else:
            task = todo_list.pop(task_index - 1)
            done_list.append(task)
            colors_print(COLORS_GREEN, f"Marked '{task}' as done.\n")


def main():
    todo_list = []
    done_list = []

    while True:
        show_menu()

        choice = input("What do you want to do?\n")

        if choice in ["1", "1.", "a", "j", "A", "J"]:
            add_task(todo_list)
        elif choice in ["2", "2.", "s", "k", "S", "K"]:
            view_tasks(todo_list)
        elif choice in ["3", "3.", "d", "l", "D", "L"]:
            view_done(done_list)
        elif choice in ["4", "4.", "f", "ů", ";", "F", "Ů"]:
            tag_as_done(todo_list, done_list)
        elif choice in ["5", "5.", "§", "g", "'", "G"]:
            colors_print(COLORS_GREEN, "Exiting...\n")
            break
        else:
            colors_print(COLORS_RED, "Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
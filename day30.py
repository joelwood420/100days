import csv
import time
from datetime import datetime

def start_task():
    task_name = input("Enter task name: ")
    start_time = time.time()
    input("Press Enter to stop the timer")
    end_time = time.time()
    duration_seconds = end_time - start_time
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open('tasks.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([date_str, task_name, duration_seconds])
    
    print(f"Task '{task_name}' recorded with duration {duration_seconds:.2f} seconds.")


def show_history():
    try:
        with open('tasks.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            total_time = 0
            print(f"{'Date':<20} {'Task Name':<30} {'Duration (s)':<15}")
            print("-" * 65)
            for row in reader:
                date_str, task_name, duration_seconds = row
                duration_seconds = float(duration_seconds)
                total_time += duration_seconds
                print(f"{date_str:<20} {task_name:<30} {duration_seconds:<15.2f}")
            print("-" * 65)
            print(f"Total time: {total_time:.2f} seconds.")
    except FileNotFoundError:
        print("No tasksed timed.")

def main_menu():
    while True:
        print("\nMenu:")
        print("1) Start new task")
        print("2) Show history")
        print("3) Quit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            start_task()
        elif choice == '2':
            show_history()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")
            main_menu()

if __name__ == "__main__":
    main_menu()
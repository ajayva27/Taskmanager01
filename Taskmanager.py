class Task:
    id=1
    def __init__(self,title,description,priority,status):
        self.task_id=Task.id
        Task.id+=1
        self.title=title
        self.description=description
        self.priority=priority
        self.status=status
    
    def __str__(self):
        return f'Task ID:{self.task_id}\nTitle:{self.title}\nDescription:{self.description}\nPriority:{self.priority}\nStatus:{self.status}'
    
class TaskManager:
    def __init__(self):
        self.tasks=[]

    def add_task(self,task):
        self.tasks.append(task)

    def edit_task(self,task_id,title=None,description=None,priority=None,status=None):
        for task in self.tasks:
            if task.task_id ==task_id:
                if task.title is not None:
                    task.title=title
                if task.description is not None:
                    task.description=description
                if task.priority is not None:
                    task.priority=priority
                if task.status is not None:
                    task.status=status
                return True
        return False
    
    def delete_task(self,task_id):
        for task in self.tasks:
            if task.task_id==task_id:
                self.tasks.remove(task)
                return True
        return False
    
    def get_task_by_id(self,task_id):
        for task in self.tasks:
            if task.task_id==task_id:
                return task
        return None
    
    def view_all_tasks(self):
        if not self.tasks:
            return "No tasks available"
        else:
            return "\n".join([str(task) for task in self.tasks])
        
    def filter_tasks_by_priority(self,priority):
        filtered_tasks=[task for task in self.tasks if task.priority.lower()==priority.lower()]
        if not filtered_tasks:
            return "No tasks with this priority"
        else:
            return "\n".join([str(task) for task in filtered_tasks])
        
        
def main():
    task_manager=TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. View All Tasks")
        print("5. Filter Task By Priority")
        print("6. Exit")

        choice=input("Enter your choice (1-6):")

        if choice=="1":  #add task
            title = input("Enter Title: ")
            description = input("Enter Description: ")
            priority = input("Enter Priority (High/Medium/Low): ")
            status = input("Enter Status (Pending/In Progress/Completed): ")
            task=Task(title,description,priority,status)
            task_manager.add_task(task)
            print("Task added successfully")

        elif choice=="2":  #edit task
            task_id = int(input("Enter Task ID to edit: "))
            title = input("Enter new Title (leave blank to keep existing): ")
            description = input("Enter new Description (leave blank to keep existing): ")
            priority = input("Enter new Priority (leave blank to keep existing): ")
            status = input("Enter new Status (leave blank to keep existing): ")
            if task_manager.edit_task(task_id,title,description,priority,status):
                print("Task updated sucessfully.")
            else:
                print("Task not found.")

        elif choice=="3": #delete task
            task_id=int(input("Enter the task ID to delete:"))
            if task_manager.delete_task(task_id):
                print("Task deleted successfully")
            else:
                print("Task not found")

        elif choice=="4":  #view all tasks
            print(task_manager.view_all_tasks())

        elif choice=="5":
            priority=input("Enter priority to filter (High/Medium/low):")
            print(task_manager.filter_tasks_by_priority(priority))

        elif choice=="6":
            print("Exiting Task Manager.!!!")
            break

        else:
            print("Invalid choice, Please enter a number between 1 to 6.")

if __name__=="__main__":
    main()

        




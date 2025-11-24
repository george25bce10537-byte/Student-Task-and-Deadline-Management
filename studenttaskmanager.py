import tkinter as tk
from tkinter import ttk, messagebox
import json
from datetime import datetime
import os

class Task:
    
    def __init__(self, title, due_date, priority, status="Pending"):
        self.title = title
        self.due_date = due_date
        self.priority = priority
        self.status = status

    def to_dict(self):
        
        return {
            "title": self.title,
            "due_date": self.due_date,
            "priority": self.priority,
            "status": self.status
        }

class TaskManager:
    
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def add_task(self, title, due_date, priority):
        new_task = Task(title, due_date, priority)
        self.tasks.append(new_task)
        self.save_tasks()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()

    def mark_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].status = "Completed"
            self.save_tasks()

    def get_tasks(self):
        return self.tasks

    def sort_tasks(self, by="date"):
        if by == "date":
            self.tasks.sort(key=lambda x: x.due_date)
        elif by == "priority":
            # Sort order: High -> Medium -> Low
            priority_map = {"High": 1, "Medium": 2, "Low": 3}
            self.tasks.sort(key=lambda x: priority_map.get(x.priority, 4))
        self.save_tasks()

    def save_tasks(self):
        
        data = [t.to_dict() for t in self.tasks]
        with open(self.filename, 'w') as f:
            json.dump(data, f)

    def load_tasks(self):
        
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r') as f:
            data = json.load(f)
            return [Task(d['title'], d['due_date'], d['priority'], d['status']) for d in data]


class TaskApp:
    
    def __init__(self, root):
        self.manager = TaskManager()
        self.root = root
        self.root.title("Student Task & Deadline Manager")
        self.root.geometry("600x500")

        
        input_frame = tk.Frame(root, padx=10, pady=10)
        input_frame.pack(fill="x")

        tk.Label(input_frame, text="Task Title:").grid(row=0, column=0)
        self.entry_title = tk.Entry(input_frame, width=30)
        self.entry_title.grid(row=0, column=1)

        tk.Label(input_frame, text="Due Date (YYYY-MM-DD):").grid(row=1, column=0)
        self.entry_date = tk.Entry(input_frame, width=30)
        self.entry_date.grid(row=1, column=1)

        tk.Label(input_frame, text="Priority:").grid(row=2, column=0)
        self.combo_priority = ttk.Combobox(input_frame, values=["High", "Medium", "Low"], width=27)
        self.combo_priority.current(1) # Default to Medium
        self.combo_priority.grid(row=2, column=1)

        btn_add = tk.Button(input_frame, text="Add Task", command=self.add_task_gui, bg="#4CAF50", fg="white")
        btn_add.grid(row=3, column=0, columnspan=2, pady=10, sticky="we")

        
        control_frame = tk.Frame(root, padx=10, pady=5)
        control_frame.pack(fill="x")

        tk.Button(control_frame, text="Sort by Date", command=lambda: self.refresh_list("date")).pack(side="left", padx=5)
        tk.Button(control_frame, text="Sort by Priority", command=lambda: self.refresh_list("priority")).pack(side="left", padx=5)
        tk.Button(control_frame, text="Mark Complete", command=self.complete_task_gui, bg="orange").pack(side="right", padx=5)
        tk.Button(control_frame, text="Delete Task", command=self.delete_task_gui, bg="#f44336", fg="white").pack(side="right", padx=5)

        
        self.tree = ttk.Treeview(root, columns=("Title", "Date", "Priority", "Status"), show="headings")
        self.tree.heading("Title", text="Task Title")
        self.tree.heading("Date", text="Due Date")
        self.tree.heading("Priority", text="Priority")
        self.tree.heading("Status", text="Status")
        
        
        self.tree.column("Title", width=200)
        self.tree.column("Date", width=100)
        self.tree.column("Priority", width=80)
        self.tree.column("Status", width=100)
        
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        
        self.refresh_list()

    def add_task_gui(self):
        title = self.entry_title.get()
        date_str = self.entry_date.get()
        priority = self.combo_priority.get()

        
        if not title or not date_str:
            messagebox.showerror("Input Error", "Please fill in all fields.")
            return
        
        try:
            
            datetime.strptime(date_str, "%Y-%m-%d")
            self.manager.add_task(title, date_str, priority)
            self.entry_title.delete(0, tk.END)
            self.entry_date.delete(0, tk.END)
            self.refresh_list()
        except ValueError:
            messagebox.showerror("Date Error", "Date must be in YYYY-MM-DD format.")

    def delete_task_gui(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")
            return
        index = self.tree.index(selected[0])
        self.manager.delete_task(index)
        self.refresh_list()

    def complete_task_gui(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select a task.")
            return
        index = self.tree.index(selected[0])
        self.manager.mark_complete(index)
        self.refresh_list()

    def refresh_list(self, sort_by=None):
        if sort_by:
            self.manager.sort_tasks(sort_by)
        
        
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        
        for task in self.manager.get_tasks():
            self.tree.insert("", "end", values=(task.title, task.due_date, task.priority, task.status))


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()
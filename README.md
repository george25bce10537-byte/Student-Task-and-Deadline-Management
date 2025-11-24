# Manager of Student Tasks and Deadlines

 ### A quick and easy way to keep track of homework and tests.


 ---

 ## Synopsis
 Everyone has experienced waking up in a panic after forgetting that an assignment was due at 11:59 PM.  To address that issue, I created the **Student Task & Deadline Manager**. 

 This small desktop program was created especially to help students manage their academic lives.  This is entirely student-focused, unlike sophisticated project management tools designed for corporate teams. Students can track tasks, set priorities, and receive visual reminders of upcoming deadlines.

## Key Features: * **Create & Track Tasks:** Add assignments with a title, due date, and priority level with ease. * **Smart Sorting:**  Overpowered?  To arrange tasks according to **Date** (what's due soonest) or **Priority** (what matters most), click a single button.
 * Tracking the status:  When you're finished, mark tasks as "Completed" or remove them completely.
 * **Automatic Save:  You never lose your list, even if you shut down the application, because your tasks are automatically saved to a local file called tasks.json.  To prevent you from inadvertently entering incorrect deadlines, the app verifies that dates are formatted correctly.

 ## Methods Employed
 Python appealed to me because of its robust standard libraries and ease of reading.
 * **Language:** Python 3.x * **GUI Framework:** Tkinter (a standard Python interface) * **Data Storage:** JSON (for lightweight, readable data persistence) * **Modules:** `datetime` (for date logic) and `os` (for file handling)

## Overview of the Project
[cite_start] In order to maintain clean, modular code [cite: 57], I structured the project as follows:

**text
Student Task Manager
■
The application can be launched from main.py.
The logic is handled by models.py (Task class & TaskManager).
■ ui.py # Manages the GUI (widgets & Tkinter window)
Tasks.json is automatically generated to store your data.
■ README.md # The file!
The problem statement and scope are found in statement.md

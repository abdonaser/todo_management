# To-Do Management - Odoo 17 Module

A sleek, lightweight task-tracking module for Odoo 17, designed to streamline task management. Assign tasks to contacts, set deadlines, track progress, and centralize communication within a single interface.

---

## ✨ Key Features

| Feature                          | Description                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| **Per-Contact Task List**        | Each `res.partner` has a dedicated *Tasks* tab displaying all assignments.  |
| **Status Workflow**              | Intuitive `New → In Progress → Completed` flow with one-click buttons and a visual status bar. |
| **Deadline Guardrails**          | Prevents past due dates and auto-suggests a +7-day deadline if none is set. |
| **Unique Task Names**            | Database-level constraint ensures no duplicate task titles per assignee.    |
| **Auto-Notifications**           | Built-in mail and activity mixins keep assignees and followers informed.    |
| **Inline Contact Info**          | Clean form layout with assignee photo, name, and email at a glance.         |
| **Search & Group By**            | Quick filters for status, overdue tasks, assignee, or due date.             |
| **Tree & Kanban Views**          | Fully functional tree view with seamless Kanban view compatibility.         |

---

## 📸 Screenshots

| Task Form                        | Task List                        | Partner Tab                            |
|----------------------------------|----------------------------------|---------------------------------------|
| ![Task Form](docs/Todo_Form.png) | ![Task List](docs/Todo_Tree.png) | ![Partner Tab](docs/contact_Form.png) |

---

## 🚀 Getting Started

1. **Access Tasks**  
   Create tasks directly from the *Tasks* tab in a contact’s form or via the *To-Do List* menu.

2. **Manage Status**  
   Use *Start* to move a task to *In Progress* and *Done* to mark it *Completed*.

3. **Collaborate with Chatter**  
   Leverage Odoo’s built-in `mail.thread` to discuss tasks, log notes, or schedule follow-up activities.

4. **Filter & Find**  
   Use the search view to filter tasks by *New*, *In Progress*, *Completed*, or *Overdue* (tasks with deadlines before today).

---

## 🛠 Technical Details

### Models
- **`todo.task` (`toDoTask.py`)**  
  - Inherits `mail.thread` and `mail.activity.mixin` for robust communication.  
  - SQL constraint: `unique(task_name, assign_to)` prevents duplicate task names per assignee.  
  - Python constraints enforce valid due dates and email formats.  

- **`res.partner` Extension**  
  - Adds `task_ids` (One2many relation) to link tasks to contacts.

### Views
- Custom form, tree, and search views defined in `toDoTask_view.xml`.  
- Partner form extended via `res_partner_view.xml` to include the *Tasks* tab.

### Assets
- Custom CSS (`static/src/css/todo.css`) enhances avatar and field layouts in the backend.

### Access Control
- Basic security configuration included in the module. Customize groups and access rights as needed.

---

## 👨‍💻 Author & Maintainer

**Abdelrahman Naser**  
📍 [LinkedIn](https://www.linkedin.com/in/abdelrahman-naser-muhammed)  
📂 [GitHub](https://github.com/abdonaser)
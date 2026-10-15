import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime


# ===========================================================
# DATABASE
# ===========================================================

conn = sqlite3.connect("todo.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    category TEXT DEFAULT 'General',
    priority TEXT DEFAULT 'Medium',
    due_date TEXT,
    completed INTEGER DEFAULT 0,
    created_at TEXT
)
""")

conn.commit()


# ===========================================================
# COLORS
# ===========================================================

BG = "#F5F7FB"
WHITE = "#FFFFFF"
DARK = "#172033"
TEXT = "#273142"
MUTED = "#7A8496"
BLUE = "#2563EB"
GREEN = "#16A34A"
RED = "#DC2626"
ORANGE = "#EA580C"
PURPLE = "#7C3AED"
BORDER = "#E5E7EB"


# ===========================================================
# MAIN WINDOW
# ===========================================================

root = tk.Tk()
root.title("TaskFlow Pro | Smart Task Manager")
root.geometry("1200x750")
root.minsize(1000, 650)
root.configure(bg=BG)


# ===========================================================
# STYLES
# ===========================================================

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Treeview",
    background=WHITE,
    foreground=TEXT,
    rowheight=42,
    fieldbackground=WHITE,
    font=("Segoe UI", 10),
    borderwidth=0
)

style.configure(
    "Treeview.Heading",
    background=DARK,
    foreground=WHITE,
    font=("Segoe UI", 10, "bold"),
    padding=10
)

style.map(
    "Treeview",
    background=[("selected", "#DBEAFE")],
    foreground=[("selected", TEXT)]
)

style.configure(
    "TCombobox",
    padding=7,
    font=("Segoe UI", 10)
)


# ==========================================================
# SIDEBAR
# ==========================================================

sidebar = tk.Frame(
    root,
    bg=DARK,
    width=220
)

sidebar.pack(
    side="left",
    fill="y"
)

sidebar.pack_propagate(False)


tk.Label(
    sidebar,
    text="TaskFlow",
    bg=DARK,
    fg=WHITE,
    font=("Segoe UI", 25, "bold")
).pack(
    pady=(35, 2)
)

tk.Label(
    sidebar,
    text="PRO",
    bg=DARK,
    fg="#60A5FA",
    font=("Segoe UI", 10, "bold")
).pack()


tk.Label(
    sidebar,
    text="SMART TASK MANAGEMENT",
    bg=DARK,
    fg="#9CA3AF",
    font=("Segoe UI", 8)
).pack(pady=(5, 35))


# Sidebar information

def sidebar_button(text, command):
    button = tk.Button(
        sidebar,
        text=text,
        command=command,
        bg=DARK,
        fg="#D1D5DB",
        activebackground="#26334D",
        activeforeground=WHITE,
        bd=0,
        anchor="w",
        padx=25,
        pady=12,
        font=("Segoe UI", 10),
        cursor="hand2"
    )

    button.pack(fill="x", pady=2)

    return button


# ===========================================================
# MAIN CONTENT
# ===========================================================

content = tk.Frame(
    root,
    bg=BG
)

content.pack(
    side="left",
    fill="both",
    expand=True
)


# ===========================================================
# HEADER
# ===========================================================

header = tk.Frame(
    content,
    bg=BG
)

header.pack(
    fill="x",
    padx=30,
    pady=(25, 5)
)


tk.Label(
    header,
    text="Dashboard",
    bg=BG,
    fg=DARK,
    font=("Segoe UI", 25, "bold")
).pack(side="left")


tk.Label(
    header,
    text="Organize your work. Stay productive.",
    bg=BG,
    fg=MUTED,
    font=("Segoe UI", 10)
).pack(
    side="left",
    padx=15,
    pady=10
)


# ===========================================================
# DASHBOARD CARDS
# ===========================================================

cards = tk.Frame(
    content,
    bg=BG
)

cards.pack(
    fill="x",
    padx=30,
    pady=20
)


def create_card(parent, title, color):

    frame = tk.Frame(
        parent,
        bg=WHITE,
        highlightbackground=BORDER,
        highlightthickness=1
    )

    frame.pack(
        side="left",
        fill="x",
        expand=True,
        padx=5
    )

    tk.Label(
        frame,
        text=title,
        bg=WHITE,
        fg=MUTED,
        font=("Segoe UI", 9, "bold")
    ).pack(
        anchor="w",
        padx=18,
        pady=(15, 2)
    )

    value = tk.Label(
        frame,
        text="0",
        bg=WHITE,
        fg=color,
        font=("Segoe UI", 24, "bold")
    )

    value.pack(
        anchor="w",
        padx=18,
        pady=(0, 15)
    )

    return value


total_value = create_card(
    cards,
    "TOTAL TASKS",
    BLUE
)

pending_value = create_card(
    cards,
    "PENDING",
    ORANGE
)

completed_value = create_card(
    cards,
    "COMPLETED",
    GREEN
)

overdue_value = create_card(
    cards,
    "OVERDUE",
    RED
)


# ===========================================================
# ADD TASK PANEL
# ===========================================================

add_panel = tk.Frame(
    content,
    bg=WHITE,
    highlightbackground=BORDER,
    highlightthickness=1
)

add_panel.pack(
    fill="x",
    padx=30,
    pady=5
)


tk.Label(
    add_panel,
    text="CREATE NEW TASK",
    bg=WHITE,
    fg=DARK,
    font=("Segoe UI", 11, "bold")
).grid(
    row=0,
    column=0,
    columnspan=5,
    sticky="w",
    padx=20,
    pady=(15, 10)
)


# Task

tk.Label(
    add_panel,
    text="Task name",
    bg=WHITE,
    fg=MUTED,
    font=("Segoe UI", 9)
).grid(
    row=1,
    column=0,
    sticky="w",
    padx=20
)

task_entry = tk.Entry(
    add_panel,
    width=30,
    font=("Segoe UI", 10),
    bd=1,
    relief="solid"
)

task_entry.grid(
    row=2,
    column=0,
    padx=20,
    pady=(3, 18)
)


# Category

tk.Label(
    add_panel,
    text="Category",
    bg=WHITE,
    fg=MUTED,
    font=("Segoe UI", 9)
).grid(
    row=1,
    column=1,
    sticky="w"
)

category_box = ttk.Combobox(
    add_panel,
    values=[
        "General",
        "College",
        "Coding",
        "Project",
        "Personal",
        "Work"
    ],
    state="readonly",
    width=14
)

category_box.set("General")

category_box.grid(
    row=2,
    column=1,
    padx=10,
    pady=(3, 18)
)


# Priority

tk.Label(
    add_panel,
    text="Priority",
    bg=WHITE,
    fg=MUTED,
    font=("Segoe UI", 9)
).grid(
    row=1,
    column=2,
    sticky="w"
)

priority_box = ttk.Combobox(
    add_panel,
    values=[
        "Low",
        "Medium",
        "High"
    ],
    state="readonly",
    width=12
)

priority_box.set("Medium")

priority_box.grid(
    row=2,
    column=2,
    padx=10,
    pady=(3, 18)
)


# Due date

tk.Label(
    add_panel,
    text="Due date",
    bg=WHITE,
    fg=MUTED,
    font=("Segoe UI", 9)
).grid(
    row=1,
    column=3,
    sticky="w"
)

date_entry = tk.Entry(
    add_panel,
    width=14,
    font=("Segoe UI", 10),
    bd=1,
    relief="solid"
)

date_entry.grid(
    row=2,
    column=3,
    padx=10,
    pady=(3, 18)
)


tk.Button(
    add_panel,
    text="+  ADD TASK",
    command=lambda: add_task(),
    bg=BLUE,
    fg=WHITE,
    activebackground="#1D4ED8",
    activeforeground=WHITE,
    font=("Segoe UI", 10, "bold"),
    bd=0,
    padx=18,
    pady=9,
    cursor="hand2"
).grid(
    row=2,
    column=4,
    padx=20,
    pady=(3, 18)
)


# ===========================================================
# SEARCH AND FILTER
# ===========================================================

control = tk.Frame(
    content,
    bg=BG
)

control.pack(
    fill="x",
    padx=30,
    pady=(20, 5)
)


tk.Label(
    control,
    text="Search",
    bg=BG,
    fg=DARK,
    font=("Segoe UI", 10, "bold")
).pack(side="left")


search_entry = tk.Entry(
    control,
    width=30,
    font=("Segoe UI", 10),
    bd=1,
    relief="solid"
)

search_entry.pack(
    side="left",
    padx=8,
    ipady=5
)


tk.Label(
    control,
    text="Filter",
    bg=BG,
    fg=DARK,
    font=("Segoe UI", 10, "bold")
).pack(
    side="left",
    padx=(20, 5)
)


filter_box = ttk.Combobox(
    control,
    values=[
        "All Tasks",
        "Pending",
        "Completed",
        "Overdue",
        "High Priority",
        "Medium Priority",
        "Low Priority"
    ],
    state="readonly",
    width=18
)

filter_box.set("All Tasks")

filter_box.pack(
    side="left"
)


# ===========================================================
# TABLE
# ===========================================================

table_frame = tk.Frame(
    content,
    bg=WHITE,
    highlightbackground=BORDER,
    highlightthickness=1
)

table_frame.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=10
)


columns = (
    "ID",
    "Task",
    "Category",
    "Priority",
    "Due Date",
    "Status"
)

table = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings",
    selectmode="browse"
)


widths = {
    "ID": 50,
    "Task": 330,
    "Category": 120,
    "Priority": 100,
    "Due Date": 120,
    "Status": 120
}

for column in columns:

    table.heading(
        column,
        text=column.upper()
    )

    table.column(
        column,
        width=widths[column],
        anchor="center"
    )


table.column(
    "Task",
    anchor="w"
)


scrollbar = ttk.Scrollbar(
    table_frame,
    orient="vertical",
    command=table.yview
)

table.configure(
    yscrollcommand=scrollbar.set
)

table.pack(
    side="left",
    fill="both",
    expand=True
)

scrollbar.pack(
    side="right",
    fill="y"
)


# ============================================================
# FUNCTIONS
# ============================================================

def is_overdue(due_date):

    if not due_date:
        return False

    try:

        date = datetime.strptime(
            due_date,
            "%d-%m-%Y"
        ).date()

        return date < datetime.now().date()

    except ValueError:

        return False


def update_dashboard():

    cursor.execute(
        "SELECT COUNT(*) FROM tasks"
    )

    total = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM tasks WHERE completed=0"
    )

    pending = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM tasks WHERE completed=1"
    )

    completed = cursor.fetchone()[0]

    cursor.execute(
        "SELECT due_date FROM tasks WHERE completed=0"
    )

    overdue = 0

    for row in cursor.fetchall():

        if is_overdue(row[0]):
            overdue += 1

    total_value.config(text=str(total))
    pending_value.config(text=str(pending))
    completed_value.config(text=str(completed))
    overdue_value.config(text=str(overdue))


def load_tasks():

    for item in table.get_children():
        table.delete(item)

    search = search_entry.get().strip()
    selected_filter = filter_box.get()

    query = """
        SELECT id, title, category, priority, due_date, completed
        FROM tasks
    """

    conditions = []
    values = []

    if search:

        conditions.append(
            "(title LIKE ? OR category LIKE ?)"
        )

        values.extend([
            "%" + search + "%",
            "%" + search + "%"
        ])

    if selected_filter == "Pending":

        conditions.append(
            "completed = 0"
        )

    elif selected_filter == "Completed":

        conditions.append(
            "completed = 1"
        )

    elif selected_filter == "High Priority":

        conditions.append(
            "priority = 'High'"
        )

    elif selected_filter == "Medium Priority":

        conditions.append(
            "priority = 'Medium'"
        )

    elif selected_filter == "Low Priority":

        conditions.append(
            "priority = 'Low'"
        )

    if conditions:

        query += " WHERE " + " AND ".join(conditions)

    query += " ORDER BY id DESC"

    cursor.execute(
        query,
        values
    )

    tasks = cursor.fetchall()

    for task in tasks:

        task_id = task[0]
        title = task[1]
        category = task[2]
        priority = task[3]
        due_date = task[4]
        completed = task[5]

        if completed:

            status = "Completed"

        elif is_overdue(due_date):

            status = "Overdue"

        else:

            status = "Pending"

        table.insert(
            "",
            "end",
            values=(
                task_id,
                title,
                category,
                priority,
                due_date,
                status
            )
        )

    update_dashboard()


def add_task():

    title = task_entry.get().strip()
    category = category_box.get()
    priority = priority_box.get()
    due_date = date_entry.get().strip()

    if not title:

        messagebox.showwarning(
            "Missing Information",
            "Please enter a task name."
        )

        return

    if due_date:

        try:

            datetime.strptime(
                due_date,
                "%d-%m-%Y"
            )

        except ValueError:

            messagebox.showwarning(
                "Invalid Date",
                "Use DD-MM-YYYY format.\nExample: 25-09-2026"
            )

            return

    cursor.execute(
        """
        INSERT INTO tasks
        (title, category, priority, due_date, completed, created_at)
        VALUES (?, ?, ?, ?, 0, ?)
        """,
        (
            title,
            category,
            priority,
            due_date,
            datetime.now().strftime(
                "%d-%m-%Y %H:%M"
            )
        )
    )

    conn.commit()

    task_entry.delete(
        0,
        tk.END
    )

    date_entry.delete(
        0,
        tk.END
    )

    category_box.set(
        "General"
    )

    priority_box.set(
        "Medium"
    )

    load_tasks()


def get_selected():

    selected = table.selection()

    if not selected:

        messagebox.showwarning(
            "No Selection",
            "Please select a task first."
        )

        return None

    return table.item(
        selected[0]
    )["values"]


def complete_task():

    values = get_selected()

    if values is None:
        return

    task_id = values[0]

    cursor.execute(
        """
        UPDATE tasks
        SET completed = 1
        WHERE id = ?
        """,
        (task_id,)
    )

    conn.commit()

    load_tasks()


def reopen_task():

    values = get_selected()

    if values is None:
        return

    task_id = values[0]

    cursor.execute(
        """
        UPDATE tasks
        SET completed = 0
        WHERE id = ?
        """,
        (task_id,)
    )

    conn.commit()

    load_tasks()


def delete_task():

    values = get_selected()

    if values is None:
        return

    task_id = values[0]

    answer = messagebox.askyesno(
        "Delete Task",
        "Are you sure you want to delete this task?"
    )

    if answer:

        cursor.execute(
            "DELETE FROM tasks WHERE id=?",
            (task_id,)
        )

        conn.commit()

        load_tasks()


def edit_task():

    values = get_selected()

    if values is None:
        return

    task_id = values[0]

    window = tk.Toplevel(root)

    window.title("Edit Task")
    window.geometry("430x400")
    window.configure(bg=WHITE)
    window.resizable(False, False)

    tk.Label(
        window,
        text="Edit Task",
        bg=WHITE,
        fg=DARK,
        font=("Segoe UI", 20, "bold")
    ).pack(pady=20)

    tk.Label(
        window,
        text="Task Name",
        bg=WHITE,
        fg=MUTED
    ).pack()

    edit_title = tk.Entry(
        window,
        width=35,
        font=("Segoe UI", 11)
    )

    edit_title.pack(
        pady=5
    )

    edit_title.insert(
        0,
        values[1]
    )

    tk.Label(
        window,
        text="Category",
        bg=WHITE,
        fg=MUTED
    ).pack(pady=(10, 0))

    edit_category = ttk.Combobox(
        window,
        values=[
            "General",
            "College",
            "Coding",
            "Project",
            "Personal",
            "Work"
        ],
        state="readonly",
        width=25
    )

    edit_category.set(values[2])

    edit_category.pack(
        pady=5
    )

    tk.Label(
        window,
        text="Priority",
        bg=WHITE,
        fg=MUTED
    ).pack(pady=(10, 0))

    edit_priority = ttk.Combobox(
        window,
        values=[
            "Low",
            "Medium",
            "High"
        ],
        state="readonly",
        width=25
    )

    edit_priority.set(values[3])

    edit_priority.pack(
        pady=5
    )

    tk.Label(
        window,
        text="Due Date (DD-MM-YYYY)",
        bg=WHITE,
        fg=MUTED
    ).pack(pady=(10, 0))

    edit_date = tk.Entry(
        window,
        width=27,
        font=("Segoe UI", 10)
    )

    edit_date.insert(
        0,
        values[4]
    )

    edit_date.pack(
        pady=5
    )

    def save_changes():

        new_title = edit_title.get().strip()
        new_category = edit_category.get()
        new_priority = edit_priority.get()
        new_date = edit_date.get().strip()

        if not new_title:

            messagebox.showwarning(
                "Error",
                "Task name cannot be empty."
            )

            return

        if new_date:

            try:

                datetime.strptime(
                    new_date,
                    "%d-%m-%Y"
                )

            except ValueError:

                messagebox.showwarning(
                    "Error",
                    "Use DD-MM-YYYY format."
                )

                return

        cursor.execute(
            """
            UPDATE tasks
            SET title=?, category=?, priority=?, due_date=?
            WHERE id=?
            """,
            (
                new_title,
                new_category,
                new_priority,
                new_date,
                task_id
            )
        )

        conn.commit()

        window.destroy()

        load_tasks()

    tk.Button(
        window,
        text="SAVE CHANGES",
        command=save_changes,
        bg=BLUE,
        fg=WHITE,
        font=("Segoe UI", 10, "bold"),
        bd=0,
        padx=25,
        pady=9,
        cursor="hand2"
    ).pack(
        pady=20
    )


def refresh():

    search_entry.delete(
        0,
        tk.END
    )

    filter_box.set(
        "All Tasks"
    )

    load_tasks()


def show_all():

    refresh()


# ============================================================
# SIDEBAR BUTTONS
# ============================================================

sidebar_button(
    "▣   Dashboard",
    show_all
)

sidebar_button(
    "✓   Complete Task",
    complete_task
)

sidebar_button(
    "↻   Reopen Task",
    reopen_task
)

sidebar_button(
    "✎   Edit Task",
    edit_task
)

sidebar_button(
    "×   Delete Task",
    delete_task
)

sidebar_button(
    "⟳   Refresh",
    refresh
)


# ============================================================
# SEARCH EVENTS
# ============================================================

search_entry.bind(
    "<KeyRelease>",
    lambda event: load_tasks()
)

filter_box.bind(
    "<<ComboboxSelected>>",
    lambda event: load_tasks()
)


# ============================================================
# FOOTER
# ============================================================

footer = tk.Label(
    sidebar,
    text="TaskFlow Pro\nPython • Tkinter • SQLite",
    bg=DARK,
    fg="#6B7280",
    font=("Segoe UI", 8),
    justify="left"
)

footer.pack(
    side="bottom",
    anchor="w",
    padx=25,
    pady=25
)


# ============================================================
# CLOSE
# ============================================================

def close_application():

    conn.close()
    root.destroy()


root.protocol(
    "WM_DELETE_WINDOW",
    close_application
)


# ============================================================
# START APPLICATION
# ============================================================

load_tasks()

root.mainloop()

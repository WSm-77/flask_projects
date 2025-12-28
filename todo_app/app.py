from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "your_secret_key"

def init_db():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            due_date TEXT,
            priority TEXT,
            completed BOOLEAN NOT NULL DEFAULT 0,
            created_at TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

def get_db_connection():
    conn = sqlite3.connect('tasks.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks ORDER BY completed, due_date').fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date']
        priority = request.form['priority']

        if not title:
            flash('Title is required!')
            return redirect(url_for('add'))

        conn = get_db_connection()
        conn.execute('INSERT INTO tasks (title, description, due_date, priority, created_at) VALUES (?, ?, ?, ?, ?)',
                    (title, description, due_date, priority, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        conn.commit()
        conn.close()
        flash('Task added successfully!')
        return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = get_db_connection()
    task = conn.execute('SELECT * FROM tasks WHERE id = ?', (id,)).fetchone()
    conn.close()

    if task is None:
        flash('Task not found!')
        return redirect(url_for('index'))

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date']
        priority = request.form['priority']
        completed = 1 if 'completed' in request.form else 0

        if not title:
            flash('Title is required!')
            return redirect(url_for('edit', id=id))

        conn = get_db_connection()
        conn.execute('UPDATE tasks SET title = ?, description = ?, due_date = ?, priority = ?, completed = ? WHERE id = ?',
                    (title, description, due_date, priority, completed, id))
        conn.commit()
        conn.close()
        flash('Task updated successfully!')
        return redirect(url_for('index'))

    return render_template('edit.html', task=task)

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('Task deleted successfully!')
    return redirect(url_for('index'))

@app.route('/toggle/<int:id>')
def toggle_complete(id):
    conn = get_db_connection()
    task = conn.execute('SELECT * FROM tasks WHERE id = ?', (id,)).fetchone()

    if task is None:
        flash('Task not found!')
        return redirect(url_for('index'))

    new_status = 0 if task['completed'] else 1
    conn.execute('UPDATE tasks SET completed = ? WHERE id = ?', (new_status, id))
    conn.commit()
    conn.close()

    status = "completed" if new_status else "marked as incomplete"
    flash(f'Task {status}!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

import sqlite3


class Database:
    def __init__(self, db_path='task_base.db'):
        self.conn = sqlite3.connect(db_path)
        # self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT
            )
        ''')
        self.conn.commit()

    def get_tasks(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM task')
        return cursor.fetchall()

    def close(self):
        self.conn.close()

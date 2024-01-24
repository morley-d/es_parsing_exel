import sqlite3

# Подключение к базе данных SQLite
db_path = 'task_base.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Название таблицы, которую вы хотите удалить
table_name = 'task'

try:
    # Выполнение SQL-запроса для удаления таблицы
    cursor.execute(f'DROP TABLE IF EXISTS {table_name};')
    print(f'Таблица {table_name} удалена.')

    # Подтверждение и сохранение изменений
    conn.commit()

except Exception as e:
    print(f'Ошибка при удалении таблицы: {e}')

finally:
    # Закрытие соединения с базой данных
    conn.close()
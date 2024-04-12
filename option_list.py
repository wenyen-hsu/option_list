import sqlite3

def create_connection(db_file):
    """創建數據庫連接"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(conn):
    """創建表格"""
    try:
        sql = '''CREATE TABLE IF NOT EXISTS commands (
                    name TEXT PRIMARY KEY,
                    description TEXT NOT NULL
                 );'''
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error as e:
        print(e)

def add_command(conn, command_name, description):
    """新增命令到數據庫"""
    sql = '''INSERT INTO commands(name, description)
             VALUES(?, ?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (command_name, description))
        conn.commit()
    except sqlite3.IntegrityError:
        print("錯誤: 命令已存在。")

def search_command(conn, command_name):
    """搜索命令"""
    sql = 'SELECT name, description FROM commands WHERE name=?'
    cursor = conn.cursor()
    cursor.execute(sql, (command_name,))
    rows = cursor.fetchall()
    for row in rows:
        print(f"Command: {row[0]}, Description: {row[1]}")

def main():
    database = "commands.db"

    # 創建數據庫連接
    conn = create_connection(database)
    if conn is not None:
        create_table(conn)

        # 新增和搜索命令
        add_command(conn, "ls", "List directory contents")
        search_command(conn, "ls")

        # 關閉連接
        conn.close()

if __name__ == '__main__':
    main()

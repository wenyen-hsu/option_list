import sqlite3

def create_connection(db_file):
    """創建數據庫連接"""
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def create_table(conn):
    """在數據庫中創建表格"""
    try:
        sql_create_commands_table = """
        CREATE TABLE IF NOT EXISTS commands (
            name TEXT PRIMARY KEY,
            description TEXT NOT NULL
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_commands_table)
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

def add_command(conn, command_name, description):
    """將新命令添加到數據庫"""
    try:
        sql = """INSERT INTO commands (name, description)
                 VALUES (?, ?);"""
        cursor = conn.cursor()
        cursor.execute(sql, (command_name, description))
        conn.commit()
    except sqlite3.IntegrityError:
        print("命令已存在。")

def search_command(conn, command_name):
    """從數據庫搜索命令的描述"""
    try:
        sql = "SELECT name, description FROM commands WHERE name=?"
        cursor = conn.cursor()
        cursor.execute(sql, (command_name,))
        row = cursor.fetchone()
        if row:
            print(f"Command: {row[0]}\nDescription: {row[1]}")
        else:
            print("該命令未被記錄。")
    except sqlite3.Error as e:
        print(f"Error searching command: {e}")

def main():
    database = "commands.db"

    # 創建數據庫連接並創建表格
    conn = create_connection(database)
    if conn is not None:
        create_table(conn)

        while True:
            print("\n主菜單:")
            print("1. 新增 Command")
            print("2. 搜索 Command")
            print("3. 退出")
            choice = input("請選擇一個選項 (1/2/3): ")

            if choice == '1':
                command_name = input("請輸入 Command 名稱: ")
                description = input("請輸入 Command 註解: ")
                add_command(conn, command_name, description)
            elif choice == '2':
                command_name = input("請輸入要搜索的 Command 名稱: ")
                search_command(conn, command_name)
            elif choice == '3':
                print("退出程式。")
                break
            else:
                print("無效的選項，請重新輸入！")

        conn.close()

if __name__ == '__main__':
    main()

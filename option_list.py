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

def delete_command(conn, command_name):
    """删除指定的命令"""
    sql = "DELETE FROM commands WHERE name=?"
    cursor = conn.cursor()
    cursor.execute(sql, (command_name,))
    conn.commit()
    if cursor.rowcount > 0:
        print(f"命令 '{command_name}' 已被删除。")
    else:
        print("没有找到该命令。")

def update_description(conn, command_name, new_description):
    """更新命令的描述"""
    sql = "UPDATE commands SET description=? WHERE name=?"
    cursor = conn.cursor()
    cursor.execute(sql, (new_description, command_name))
    conn.commit()
    if cursor.rowcount > 0:
        print(f"命令 '{command_name}' 的描述已更新。")
    else:
        print("没有找到该命令。")

def main():
    database = "commands.db"
    conn = create_connection(database)
    if conn is not None:
        create_table(conn)

        while True:
            print("\n主菜单:")
            print("1. 新增 Command")
            print("2. 搜索 Command")
            print("3. 删除 Command")
            print("4. 更新 Command 描述")
            print("5. 退出")
            choice = input("请选择一个选项 (1/2/3/4/5): ")

            if choice == '1':
                command_name = input("请输入 Command 名称: ")
                description = input("请输入 Command 描述: ")
                add_command(conn, command_name, description)
            elif choice == '2':
                command_name = input("请输入要搜索的 Command 名称: ")
                search_command(conn, command_name)
            elif choice == '3':
                command_name = input("请输入要删除的 Command 名称: ")
                delete_command(conn, command_name)
            elif choice == '4':
                command_name = input("请输入要更新描述的 Command 名称: ")
                new_description = input("请输入新的描述: ")
                update_description(conn, command_name, new_description)
            elif choice == '5':
                print("退出程序。")
                break
            else:
                print("无效的选项，请重新输入！")

        conn.close()

if __name__ == '__main__':
    main()

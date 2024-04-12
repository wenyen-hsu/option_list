import tkinter as tk
from tkinter import messagebox

def on_button_click():
    entered_text = entry.get()
    if entered_text:
        label.config(text=f"Welcome, {entered_text}")
    else:
        messagebox.showinfo("Info", "Please enter a command name.")

root = tk.Tk()
root.title("Tkinter Basic Example")

# 设置窗口的起始大小
root.geometry('600x400')

# 创建标签
label = tk.Label(root, text="Enter a command name:")
label.grid(row=0, column=0, padx=10, pady=10)

# 创建输入框
entry = tk.Entry(root, width=30)  # 设置输入框的宽度
entry.grid(row=0, column=1, padx=10, pady=10)

# 创建按钮
button = tk.Button(root, text="Greet", command=on_button_click)
button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)  # 合并两列以居中显示按钮

# 创建一个退出按钮，绑定 root.destroy 方法来关闭窗口
exit_button = tk.Button(root, text="Exit", command=root.destroy)  # 新增行
exit_button.grid(row=2, column=1, padx=10, pady=10)  # 新增行

root.mainloop()


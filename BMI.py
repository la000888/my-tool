import tkinter as tk
from tkinter import messagebox

def bmi_level(bmi):
    if bmi < 18.5:
        return "偏瘦"
    elif bmi < 24:
        return "正常"
    elif bmi < 28:
        return "偏胖"
    else:
        return "肥胖"

def calc():
    try:
        w = float(entry_weight.get())
        h = float(entry_height.get())
        bmi = w / (h * h)
        level = bmi_level(bmi)
        result.config(text=f"BMI = {bmi:.1f}    等级：{level}")
    except ValueError:
        messagebox.showwarning("提示", "请输入正确的数字（身高用米，如 1.75）")

root = tk.Tk()
root.title("BMI 健康助手")
root.geometry("300x240")

tk.Label(root, text="体重（公斤）：").pack(pady=5)
entry_weight = tk.Entry(root)
entry_weight.pack(pady=5)

tk.Label(root, text="身高（米，如 1.75）：").pack(pady=5)
entry_height = tk.Entry(root)
entry_height.pack(pady=5)

tk.Button(root, text="计算 BMI", command=calc).pack(pady=10)

result = tk.Label(root, text="")
result.pack(pady=10)

root.mainloop()

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Student Grade Calculator")
root.geometry("320x340")


def calculate():
    try:
        m1 = float(entry1.get())
        m2 = float(entry2.get())
        m3 = float(entry3.get())

        if m1 < 0 or m1 > 100 or m2 < 0 or m2 > 100 or m3 < 0 or m3 > 100:
            messagebox.showerror("Invalid Marks", "Marks should be between 0 and 100.")
            return

        total = m1 + m2 + m3
        per = total / 3

        if per >= 75:
            grade = "A"
        elif per >= 60:
            grade = "B"
        elif per >= 40:
            grade = "C"
        else:
            grade = "F"

        lbl_res.config(
            text=f"Total: {total}\nPercentage: {per:.2f}%\nGrade: {grade}"
        )

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid marks.")


tk.Label(root, text="Subject 1 Marks:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Subject 2 Marks:").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="Subject 3 Marks:").pack()
entry3 = tk.Entry(root)
entry3.pack()

btn = tk.Button(root, text="Calculate", command=calculate)
btn.pack(pady=10)

lbl_res = tk.Label(root, text="Result will appear here")
lbl_res.pack()

root.mainloop()

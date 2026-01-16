import tkinter as tk

root = tk.Tk()

root.title("Мій перший GUI-додаток Tkinter")

root.geometry("450x300")
root.config(bg="#f0f0f0")

def update_label_content():
    """
    Отримуе текст з поля ентри, оновлюе вмист лабел и зминуе колир тексту лабел  на жовтий (використовуючи .config()).
    """

    input_text = text_entry.get()


    if input_text:
        new_text = f"введено текст: ' {input_text}'"
    else:
        new_text = "Кнопку натиснуто! введить текст вище."

    main_label.config(
        text=new_text,
        fg="yellow"
    )
frame1 = tk.Frame(root, bg="#d9d9d9", padx=15, pady=15)
frame1.pack(pady=15, padx=15)


frame2 = tk.Frame(root, bg="#cccccc", padx=15, pady=15)
frame2.pack(pady=10, padx=15)
main_label = tk.Label(
    frame1,
    text="Привіт! створи великий зелений лейбл.",
    font=("Arial", 20, "bold"),
    fg="green",
    bg="#d9d9d9"
)
main_label.pack()

text_entry = tk.Entry(
    frame2,
    width=35,
    font=("Arial", 12),
    bd=2,
    relief=tk.SUNKEN
)
text_entry.pack(pady=10)
action_button = tk.Button(
    frame2,
    text="Оновити Лейбл",
    command=update_label_content,
    font=("Arial", 12),
    bg="#007bff",
    fg="white",
    activebackground="#0056b3",
)
action_button.pack(pady=10, ipadx=10, ipady=5)



root.mainloop()


# first guiApp
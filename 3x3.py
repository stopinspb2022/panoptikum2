
def main():
    pass

if __name__ == '__main__':
    main()

def print_info(widget, depth=0):
    widget_class=widget.winfo_class()
    winfo_children=widget.winfo_children()
    widget_width = widget.winfo_width()
    widget_height = widget.winfo_height()
    widget_x = widget.winfo_x()
    widget_y = widget.winfo_y()
    widget_rootx = widget.winfo_rootx()
    widget_rooty = widget.winfo_rooty()

    widget_viewable = widget.winfo_viewable()
    widget_parent = widget.winfo_parent()

    print("   "*depth + f"{widget_class}  width={widget_width} height={widget_height} x={widget_x} y={widget_y}  viewable={widget_viewable}  parent={widget_parent}  rootx={widget_rootx} rooty={widget_rooty}    ")

    for child in widget.winfo_children():
        print_info(child, depth+1)

def checkbutton_changed():
    if enabled.get() == 1:
        showinfo(title="Info", message="Включено")
    else:
        showinfo(title="Info", message="Отключено")

def select():
    header.config(text=f"Выбрана ячейка ---> {selected_language.get()}")

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

root = Tk()
root.title("Gena")
root.geometry("500x500")

label1 = ttk.Label(text="Привет Гена!")


for r in range(3):
    for c in range(3):
        btn = ttk.Button(text=f"({r},{c})", name=f"({r},{c})")
        btn.grid(row=r, column=c)

ttk.Entry().grid(pady= 8)
label1.grid()

enabled = IntVar()
enabled_checkbutton = ttk.Checkbutton(text="Включить", variable=enabled, command=checkbutton_changed)
enabled_checkbutton.grid(padx=10, pady=10)

header = ttk.Label(text="Выберите язык")
header.grid()
python = "Python"
java = "Java"
javascript = "JavaScript"
lang = StringVar(value=python)    # по умолчанию будет выбран элемент с value=python
selected_language = StringVar()
position = {"padx":6, "pady":6, "anchor":NW}
python_btn = ttk.Radiobutton(text=python, value=python, variable=selected_language, command=select)
python_btn.grid()
javascript_btn = ttk.Radiobutton(text=javascript, value=javascript, variable=selected_language, command=select)
javascript_btn.grid()
java_btn = ttk.Radiobutton(text=java, value=java, variable=selected_language, command=select)
java_btn.grid()

btn1 = ttk.Button(text="Большая кнопка 1")
# columnspan=2 - растягиваем на три столбца
btn1.grid(columnspan=3, ipadx=70, ipady=6, padx=5, pady=5)

root.update()     # обновляем информацию о виджетах
print_info(root)

root.mainloop()

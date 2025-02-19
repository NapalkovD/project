# 19.02.2025
"""
Официальная документация: https://customtkinter.tomschimansky.com/documentation/
Релиз на GitHub: https://github.com/TomSchimansky/CustomTkinter
"""

import customtkinter as ctk

date = {
    {"Категория"



    }
}



def handle_pressing_widget_button():
        dialog_window = ctk.CTkToplevel()
        dialog_window.title("Добавление траты")
        dialog_window.geometry("750x420")

        lbl_0 = ctk.CTkLabel(master=dialog_window, text="Добавьте товар", font=my_font)
        lbl_1 = ctk.CTkLabel(master=dialog_window, text="Суть:", font=my_font)
        lbl_2 = ctk.CTkLabel(master=dialog_window, text="Категория товара", font=my_font)#главный ключ
        entry_answer = ctk.CTkEntry(master=dialog_window, font=my_font, width=200,placeholder_text="Название")#побочный ключ
        price_answer = ctk.CTkEntry(master=dialog_window, font=my_font, width=200, placeholder_text="Цена")#значение

        elems = ["Еда", "Транспорт", "Одежда","Быт.товары","Лекарства","Крупные траты"]

        widget_combobox = ctk.CTkComboBox(master=dialog_window)
        widget_combobox = ctk.CTkComboBox(master=dialog_window)
        widget_combobox.configure(font=my_font, values=elems, state="readonly", width=300)
        widget_combobox.set("Еда")

        def close():
            dialog_window.destroy()

        def add():

            dialog_window.destroy()

        widget_close = ctk.CTkButton(master=dialog_window)
        widget_close.configure(text="Вернуться", font=my_font, command=close)

        widget_add = ctk.CTkButton(master=dialog_window)
        widget_add.configure(text="Добавить", font=my_font, command=add)


        rows, columns = 6, 3
        for i in range(rows):
            dialog_window.rowconfigure(index=i, weight=1)
        for i in range(columns):
            dialog_window.columnconfigure(index=i, weight=1)
        lbl_0.grid(row=0, column=0,columnspan=3)
        lbl_1.grid(row=1,column=0)
        lbl_2.grid(row=2, column=0,columnspan=1)
        entry_answer.grid(row=1, column=1)
        price_answer.grid(row=1,column=2)
        widget_combobox.grid(row=2,column=1,columnspan=3)
        widget_close.grid(row=3,column=0)
        widget_add.grid(row=4,column=0)

def handle_pressing_widget_button1():
    global widget_button,scrollable_frame,widget_button1,widget_label,widget_button2
    widget_button.grid_forget()
    widget_button1.grid_forget()

    widget_label.grid(row=0,column=0)
    scrollable_frame.grid(row=1,column=0)
    widget_button2.grid(row=2,column=0)
def retern():
    widget_label.grid_forget()
    scrollable_frame.grid_forget()
    widget_button2.grid_forget()

    widget_button.grid(row=1, column=0)
    widget_button1.grid(row=2, column=0)


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("Траты")
root.geometry("1000x500")
my_font = ctk.CTkFont(family="Roboto", size=30)
# кнопка - Button
widget_button = ctk.CTkButton(master=root)
widget_button.configure(text="Добавить трату", font=my_font, command=handle_pressing_widget_button)

widget_button1 = ctk.CTkButton(master=root)
widget_button1.configure(text="Показать историю трат", font=my_font, command=handle_pressing_widget_button1)

widget_label = ctk.CTkLabel(master=root)
widget_label.configure(text="История трат", font=my_font)

scrollable_frame = ctk.CTkScrollableFrame(master=root)
scrollable_frame.configure( width=600,height=300)

widget_button2 = ctk.CTkButton(master=root)
widget_button2.configure(text="Вернуться", font=my_font, command=retern)

# widget_button2 = ctk.CTkButton(master=root)
# widget_button2.configure(text="Вернуться", font=my_font, command=retern)

rows, columns = 3,1
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

widget_button.grid(row=1, column=0)
widget_button1.grid(row=2, column=0)

root.mainloop()











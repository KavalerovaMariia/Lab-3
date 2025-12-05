import tkinter as tk
from tkinter import messagebox
import random
#Выберите любимую игру, найдите по ней арт или связанную картинку в поисковике
#Реализуйте форму генератора ключа, которая должна включать в себя,
# как минимум, поле для генерируемого ключа, кнопку запуска,
# найденную картинку на фоне и поле ввода текста, если того требует вариант.
window = tk.Tk()
window.geometry('2500x1538')
bg_img = tk.PhotoImage(file='arcane.png')
#Реализуйте генератор ключа. Ключ состоит из набора символов, состоящих из латинских букв A-Z и цифр 0-9.
# В зависимости от варианта может потребоваться ввод первой части ключа (указан в варианте).
# Ключ генерируется по некоторым правилам. В заданиях со сдвигом считать,
# что буквы и цифры последовательно как бы нанесены на бесконечную ленту, которую можно двигать влево и вправо.
#Назначить весовые коэффициенты символам, генерировать с учётом,
# чтобы сумма весовых коэффициентов одного блока попала в интервал.
# Пример: пусть A=1, B=2,… Пусть интервал – 30…35 -> YABD-NBCO-DGIK -> Суммы: 32-34-31
#XXXX - XXXX - XXXX (вид ключа)
def keygen():
    key_letters = {}
    alphabet = ["A", "B", "C", "D","E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for i in range(1,27):
        key_letters[i] = alphabet[i-1]
    print(list(key_letters.items()))

    while True:
        key_part = []
        key_part.append(random.choice(list(key_letters.items()))) #рандомный выбор кортежа из ключа и значения
        key_part.append(random.choice(list(key_letters.items())))
        key_part.append(random.choice(list(key_letters.items())))
        key_part.append(random.choice(list(key_letters.items())))
        print(key_part)
        summa_list = []
        letters_list = []
        for c in range(0, 4):
            summa = key_part[c][0]
            summa_list.append(summa)
            letters = key_part[c][1]
            letters_list.append(letters)

        if (sum(summa_list) < 35) and ((sum(summa_list)) > 30):
            letters_str = " ".join(str(x) for x in letters_list)

            return letters_str
            break

        else:
            key_part.append(random.choice(list(key_letters.items())))  # рандомный выбор кортежа из ключа и значения
            key_part.append(random.choice(list(key_letters.items())))
            key_part.append(random.choice(list(key_letters.items())))
            key_part.append(random.choice(list(key_letters.items())))


keygen()


def close():
    window.destroy()

def generatee():
    key_part1 = keygen()
    key_part2 = keygen()
    key_part3 = keygen()
    key_part4 = keygen()
    lbl_1st_part.configure(text = " - ".join([(key_part1),(key_part2),(key_part3),(key_part4)])) #так (configure) появляется новое значение после вычислений следующих за "сгенерировать!"

lbl_bg = tk.Label(window, image=bg_img)
lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='center')


lbl_B = tk.Label(     # с помощью label создаем надписи
    frame,
    bg = "#68228B", #цвет фона
    text='KEYGEN',
    #anchor = "w",
    font = ("Comfortaa",40),
)

lbl_B.grid(column=0, row=0, padx=10, pady=15)


lbl_keyy = tk.Label(frame,
                 text='это уникальный ключ для ПО',
                 anchor = "w",
                 font=('Comfortaa', 10))
lbl_keyy.grid(column=1,columnspan = 2, row=0, padx=10, pady=15)
lbl_1st_part = tk.Label(frame,
                 text='это уникальный ключ для ПО',
                 anchor = "w",
                 font=('Comfortaa', 10))

lbl_1st_part = tk.Label(frame, text='XXXX-XXXX-XXXX-XXXX', font=('Comfortaa', 10))
lbl_1st_part.grid(column=1, row=2)

btn_calc = tk.Button( #button - кнопкаа
    frame,
    bd = 3, #толщина контура
    bg = "#CD2626", #цвет фона
    #fg = "#8DEEEE", #цвет текста
    anchor = "w",
    font = ("Comfortaa",15), #шрифт текста,
    height=1,
    width=15,
    relief = "flat",
    activebackground="#68228B",
    text='Сгенерировать!',
    command=generatee)

btn_calc.grid(column=0, row=3, sticky = "w")
btn_exit = tk.Button(frame, text='Cancel', command=close)
btn_exit.grid(column=2, row=3, padx=10, pady=15)

window.mainloop()

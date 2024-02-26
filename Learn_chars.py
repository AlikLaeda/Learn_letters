from tkinter import *
import tkinter.font as tkFont
import random
import time

window = Tk()  
window.title('Игра угадай букву')  
window.geometry('600x350')

# Настраиваем шрифты для всего окна
default_font = tkFont.nametofont("TkDefaultFont")
default_font.configure(size=14)
default_font = tkFont.nametofont("TkTextFont")
default_font.configure(size=14)

points = 0
fonts=[
    'Times New Roman',
    'Georgia',
    'Arial',
    'Tahoma',
    'Verdana',
    'Trebuchet MS',
    'Lucida Sans Unicode',
    'Impact',
    'Comic Sans MS',
    'Courier New',
    'Lucida Console'
]
chars = ['j','j','J','g','g','G']
new_char = 'j'
new_font = 'Arial'

def dec_points():
    global points
    points -= 1
    q_point['text'] = 'Очков ' + str(points) + ' из 50'
    q_char['text'] = 'нет'
    time.sleep(0.7)


def enc_points():
    global points
    points+= 1
    q_point['text'] = 'Очков ' + str(points) + ' из 50'
    q_point.update()
    q_char['text'] = 'да'
    q_char.update()
    time.sleep(0.7)
    if points == 50:
        pass

def clic_g():
    if q_char['text'].lower() == 'g':
        enc_points()
    else:
        dec_points()
    
    new_rand()


def clic_j():
    if q_char['text'].lower() == 'j':
        enc_points()
    else:
        dec_points()
    
    new_rand()

def init_form():
    pass



q_point = Label(window, text="Очков 0 из 50")
q_point.grid(column=1, row=1, columnspan=2,  sticky=E+W+N+S)

q_char = Label(window, text=new_char, font=(new_font, 25))
q_char.grid(column=1, row=2, columnspan=2,  sticky=E+W+N+S)

def new_rand():
    global new_char, new_font, q_char
    new_char = random.choice(chars)
    new_font = random.choice(fonts)
    q_char['text'] = new_char
    q_char.config(font=(new_font, 25))

new_rand()

q_space= Label(window, text=" ", font=("Arial", 25))
q_space.grid(column=1, row=3)

btn_g = Button(window, text="джи", command=clic_g) 
btn_g.grid(column=1, row=4)

btn_j = Button(window, text="джей", command=clic_j) 
btn_j.grid(column=2, row=4)

# Включаем обработчик событий окна
window.mainloop()


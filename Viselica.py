from tkinter import *
import random
root = Tk()
root.title("Виселица")
canvas = Canvas(root, width=1200, height=600)
canvas.pack()
gridCanvas = Canvas(root, width=1200, height=100)
gridCanvas.pack(side=BOTTOM, fill=NONE)

def but():
    y = 0
    while y < 600:
        x = 0
        while x < 1200:
            canvas.create_rectangle(x, y, x+33, y+27, fill="white", outline="blue")
            x = x+33
        y = y+27

faq = '''Привет, игрок! Давай поиграем!

Принцип игры:
Компьютер загадывает слово — пишет на бумаге первую
и последнюю букву слова и отмечает места для осталь-
ных букв. Также рисуется виселица.
Загаданное компьютером слово является именем сущест-
вительным, нарицательным в именительном падеже един-
ственного числа, либо множественного числа при отсу-
тствии у слова формы единственного числа. Игрок пред-
лагает букву, которая может входить в это слово. Если
такая буква есть в слове, то компьютер пишет её над
соответствующими этой букве чертами — столько раз,
сколько она встречается в слове. Если такой буквы нет,
то к виселице добавляется круг в петле, изображающий
голову. Игрок продолжает отгадывать буквы до тех пор,
пока не отгадает всё слово. За каждый неправильный от-
вет компьютер добавляет одну часть туловища к виселице
(их 6: голова, туловище, 2 руки и 2 ноги). Если тулови-
ще в виселице нарисовано полностью, то игрок проигрыва-
ет, считается повешенным. Если игроку удаётся угадать
слово, он выигрывает.'''
canvas.create_text(600, 300, text=faq, fill="white", font=("Helvetica", "16"))
slova = list()
f = open('slova.txt', 'r')
for line in f:
    slova.append(line.strip("\n\r\t"))


def letterCoordinates(letterNumber):
    x1, y1 = 282 + (32 * letterNumber), 40
    return x1, y1


def arr():
    but()
    word = random.choice(slova)
    wo = word[1:-1]
    wor = []
    for i in wo:
        wor.append(i)

    length = len(word)
    first_letter_x = 282
    letter_x = first_letter_x

    canvas.create_text(first_letter_x, 40, text=word[0], fill="purple", font=("Helvetica", "18"))
    for i in range(length - 2):
        letter_x = letter_x + 32
        canvas.create_text(letter_x, 40, text="_", fill="purple", font=("Helvetica", "18"))

    canvas.create_text(letter_x + 32, 40, text=word[-1], fill="purple", font=("Helvetica", "18"))

    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    er = []
    win = []

    def chooseLetter(letter):
        if letter in wor:
            letterButtons[letter]["state"] = "disabled"

            for j in range(len(wor)):
                if wor[j] == letter:
                    letter_x, letter_y = letterCoordinates(j + 1)
                    canvas.create_text(letter_x, letter_y, text=letter, fill="purple", font=("Helvetica", "18"))
                    win.append(letter)


            if len(win) == length - 2:
                canvas.create_text(150, 400, text="Ты победил", fill="green", font=("Helvetica", "34"))
                for i in alphabet:
                    letterButtons[i]["state"] = "disabled"
        else:
            er.append(letter)
            letterButtons[letter]["state"] = "disabled"

            if len(er) == 1:
                golova()
            elif len(er) == 2:
                telo()
            elif len(er) == 3:
                rukaL()
            elif len(er) == 4:
                rukaP()
            elif len(er) == 5:
                nogaL()
            elif len(er) == 6:
                end()
                nogaP()
            root.update()

    letterButtons = {}
    canvas.create_line(10, 10, 10, 400, width=4, fill='black')
    canvas.create_line(10, 10, 90, 50, width=4, fill='black')

    def gen(u, row, column):
        letterButtons[u] = Button(gridCanvas, text=u, width=3, height=1, command=lambda: chooseLetter(u))
        letterButtons[u].grid(row=row, column=column)

    for i in range(len(alphabet)):
        gen(alphabet[i], i // 8, i % 8)


    def golova():
        canvas.create_oval(79, 59, 120, 80, width=4, fill='blue')
        root.update()

    def telo():
        canvas.create_line(100, 80, 100, 200, width=4, fill='blue')
        root.update()

    def rukaP():
        canvas.create_line(100, 80, 145, 100, width=4, fill='blue')
        root.update()

    def rukaL():
        canvas.create_line(100, 80, 45, 100, width=4, fill='blue')
        root.update()

    def nogaL():
        canvas.create_line(100, 200, 45, 300, width=4, fill='blue')
        root.update()

    def nogaP():
        canvas.create_line(100, 200, 145, 300, width=4, fill='blue')
        root.update()


    def end():
        canvas.create_text(150, 400, text="Ты проиграл", fill="red", font=("Helvetica", "34"))
        for i in alphabet:
            letterButtons[i]["state"] = "disabled"


btn01 = Button(root, text="Начать!", width=10, height=1, command=lambda: arr())
btn01.pack(side=BOTTOM, fill=None)
root.mainloop()

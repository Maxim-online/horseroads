#*************************************************************
#Импорты
#*************************************************************
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
from random import randint
#*************************************************************
#Функции
#*************************************************************
def horsePlaceInWindow():
    """Отображает лошадей на экране"""
    horse01.place(x=int(x01), y=20)
    horse02.place(x=int(x02), y=100)
    horse03.place(x=int(x03), y=180)
    horse04.place(x=int(x04), y=260)

def insertText(s:str):
    """Добавляет строчку в чат"""
    textDiary.insert(INSERT,s+'\n')
    textDiary.see(END)
    
def loadMoney():
    """Загружает сумму из файла"""
    try:
        with open('money.dat') as file:
            m=int(file.read())
    except:
        print(f'заданна сумма {defaultMoney} {valuta}')
        m = defaultMoney
    return m
def saveMoney(moneyToSave):
    """Сохраняет сумму в файл"""
    with open('money.dat', 'w') as file:
        file.write(f'{moneyToSave}')

def getValues(summa: int):
    value = []
    if summa >9:
        for i in range(0, 11):
            rate = i*(int(summa)//10)
            value.append(rate)
    else:
        value.append(0)
        if summa >0:
            value.append(summa)

    return value
        
def refreshCombo(eventObject):
    stavka01['values'] = getValues(money-summ02.get() - summ03.get() - summ04.get())
    stavka02['values'] = getValues(money-summ01.get() - summ03.get() - summ04.get())
    stavka03['values'] = getValues(money-summ01.get() - summ02.get() - summ04.get())
    stavka04['values'] = getValues(money-summ01.get() - summ02.get() - summ03.get())

    summ = summ01.get() + summ02.get() + summ03.get() + summ04.get()
    labelAllMoney['text'] = f'У вас на счету: {int(money-summ)} {valuta}'

    if summ01.get() >0:
        horse01Game.set(True)
    else:
        horse01Game.set(False)

    if summ02.get() >0:
        horse02Game.set(True)
    else:
        horse02Game.set(False)

    if summ03.get() >0:
        horse03Game.set(True)
    else:
        horse03Game.set(False)

    if summ04.get() >0:
        horse04Game.set(True)
    else:
        horse04Game.set(False)

    if summ > 0:
        startButton['state'] = 'normal'
    else:
        startButton['state'] = 'disabled'

def moveHorse():
    global x01, x02, x03, x04

    speed01 = (randint(1, timeDay + weather) + randint(1, int((7 - state01)) * 3)) / randint(10, 175)
    speed02 = (randint(1, timeDay + weather) + randint(1, int((7 - state02)) * 3)) / randint(10, 175)
    speed03 = (randint(1, timeDay + weather) + randint(1, int((7 - state03)) * 3)) / randint(10, 175)
    speed04 = (randint(1, timeDay + weather) + randint(1, int((7 - state04)) * 3)) / randint(10, 175)

    horsePlaceInWindow()

    if x01 <952  and x02 <952 and x03 <952 and x04 <952:
        root.after(5, moveHorse)

def runHorse():
    global money
    startButton["state"] = 'disabled'
    stavka01['state'] = 'disabled'
    stavka02['state'] = 'disabled'
    stavka03['state'] = 'disabled'
    stavka04['state'] = 'disabled'

    money -= summ01.get() + summ02.get() + summ03.get() + summ04.get()
    moveHorse()

def viewWeather():
    if timeDay == 1:
        day = 'ночь'
    elif timeDay == 2:
        day = 'утро'
    elif timeDay ==3:
        day = 'день'
    elif timeDay ==4:
        day == 'ночь'
    
    if weather ==1:
        sky = 'льёт сильный доджь'
    elif weather ==2:
        sky = 'дождик моросит'
    elif weather ==3:
        sky = 'облачно, на горизонте видны тучи'
    elif weather ==4:
        sky = 'безоблачно, ветер'
    elif weather ==5:
        sky = 'безоблачно, отличная погода'

    text = f'Сейчас на ипподроме {day}, {sky}!'
    insertText(text)

def getHealth(name, state, win):
    if state == 5:
        status = 'мучается несварением желудка'
    elif state == 4:
        status = 'плохо спала. Подёргивает веко'
    elif state == 3:
        status = 'среднее самочувствие. Можно и лучше'
    elif state == 2:
        status = 'в хорошем состоянии. Сытая'
    elif state == 1:
        status = 'не лошадь, а ракета'

    text = f'Лошадь {name} {status}. Ставка {win}:1'
    return text

def healthHorse():
    text1 = getHealth(nameHorse01, state01, winCoeff01)
    text2 = getHealth(nameHorse02, state02, winCoeff02)
    text3 = getHealth(nameHorse03, state03, winCoeff03)
    text4 = getHealth(nameHorse04, state04, winCoeff04)
    
    insertText(text1)
    insertText(text2)
    insertText(text3)
    insertText(text4)


#*************************************************************
#Значения переменных
#*************************************************************
WIDTH = 1024
HEIGHT = 600
x01, x02, x03, x04 = 20, 20, 20, 20

defaultMoney = 10000
valuta = '$'
moneny = None

nameHorse01='Даша'
nameHorse02= 'Роня'
nameHorse03 = "Варя"
nameHorse04= 'Настя'

state01 = randint(1,5)
state02 = randint(1,5)
state03 = randint(1,5)
state04 = randint(1,5)

weather = randint(1,5)

timeDay = randint(1,4)

winCoeff01 = int(100 + randint(1, 30 + state01 * 60))/100
winCoeff02 = int(100 + randint(1, 30 + state02 * 60))/100
winCoeff03 = int(100 + randint(1, 30 + state03 * 60))/100
winCoeff04 = int(100 + randint(1, 30 + state04 * 60))/100

reverse01 = False
reverse02 = False
reverse03 = False
reverse04 = False
play01 = True
play02 = True
play03 = True
play04 = True
fastSpeed01 = False
fastSpeed02 = False
fastSpeed03 = False
fastSpeed04 = False


#*************************************************************
#Формирование элементов в окне
#*************************************************************
root = Tk()
POS_X = root.winfo_screenwidth()//2-WIDTH//2
POS_Y = root.winfo_screenheight()//2-HEIGHT//2
root.title("ИППОДРОМ")
root.resizable(False, False)
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")

road_image = PhotoImage(file ="road.png")
road =  Label(root,image=road_image)
road.place(x=0, y=17)


horse01_image = PhotoImage(file = "horse01.png")
horse01 = Label(root, image = horse01_image)

horse02_image = PhotoImage(file = "horse02.png")
horse02 = Label(root, image = horse02_image)

horse03_image = PhotoImage(file = "horse03.png")
horse03 = Label(root, image = horse03_image)

horse04_image = PhotoImage(file = "horse04.png")
horse04 = Label(root, image = horse04_image)

horsePlaceInWindow()

startButton = Button(text="СТАРТ", font='arial 20', width=61, background='#37AA37')
startButton.place(x=20, y=370)

textDiary = Text(width=70, height=8, wrap=WORD)
textDiary.place(x=430, y=450)


scroll = Scrollbar(command = textDiary.yview, width=20)
scroll.place(x=990, y=450, height=132)
textDiary['yscrollcommand'] = scroll.set

money = loadMoney()
labelAllMoney = Label(text=f'Осталось средств: {money} {valuta}.', font='Arial 12')
labelAllMoney.place(x=20, y=565)

if money <=0:
    messagebox.showinfo('Стоп!', 'Нечего тут делать без денег!')
    quit()
labelHorse01 = Label(text='Ставка на лошадь №1')
labelHorse01.place(x=20, y=450)

labelHorse02 = Label(text='Ставка на лошадь №2')
labelHorse02.place(x=20, y=480)

labelHorse03 = Label(text='Ставка на лошадь №3')
labelHorse03.place(x=20, y=510)

labelHorse04 = Label(text='Ставка на лошадь №4')
labelHorse04.place(x=20, y=540)

horse01Game = BooleanVar()
horse01Game.set(0)
horseCheck01 = Checkbutton(text=nameHorse01, variable=horse01Game, onvalue=True, offvalue=False)
horseCheck01.place(x=150, y=448)

horse02Game = BooleanVar()
horse02Game.set(0)
horseCheck02 = Checkbutton(text=nameHorse02, variable=horse02Game, onvalue=True, offvalue= False)
horseCheck02.place(x=150, y=478)

horse03Game = BooleanVar()
horse03Game.set(0)
horseCheck03 = Checkbutton(text=nameHorse03, variable=horse03Game, onvalue=True, offvalue= False)
horseCheck03.place(x=150, y=508)

horse04Game = BooleanVar()
horse04Game.set(0)
horseCheck04 = Checkbutton(text=nameHorse04, variable=horse04Game, onvalue=True, offvalue= False)
horseCheck04.place(x=150, y=538)

stavka01 = ttk.Combobox(root)
stavka02 = ttk.Combobox(root)
stavka03 = ttk.Combobox(root)
stavka04 = ttk.Combobox(root)

stavka01['state'] = 'readonly'
stavka01.place(x=280, y=450)

stavka02['state'] = 'readonly'
stavka02.place(x=280, y=480)

stavka03['state'] = 'readonly'
stavka03.place(x=280, y=510)

stavka04['state'] = 'readonly'
stavka04.place(x=280, y=540)

summ01 = IntVar()
summ02 = IntVar()
summ03 = IntVar()
summ04 = IntVar()

stavka01['textvariable'] = summ01
stavka02['textvariable'] = summ02
stavka03['textvariable'] = summ03
stavka04['textvariable'] = summ04



stavka01.bind('<<ComboboxSelected>>', refreshCombo)
stavka02.bind('<<ComboboxSelected>>', refreshCombo)
stavka03.bind('<<ComboboxSelected>>', refreshCombo)
stavka04.bind('<<ComboboxSelected>>', refreshCombo)
refreshCombo('')

stavka01.current(0)
stavka02.current(0)
stavka03.current(0)
stavka04.current(0)

horseCheck01['state'] = 'disabled'
horseCheck02['state'] = 'disabled'
horseCheck03['state'] = 'disabled'
horseCheck04['state'] = 'disabled'

startButton['state'] = 'disabled'

startButton['command'] = runHorse

viewWeather()

healthHorse()

#insertText('test')
root.mainloop()
#! /usr/bin/env python3
from datetime import datetime
import time

def pause_sleep():
    time.sleep(2)
    print('\n')


def age_request():
    while True:
        try:
            q1 = int(input('Cколько тебе лет?\n'))
        except ValueError:
            pause_sleep()
            print('Попробуй ввести возраст заново, используй только цифры.')
        else:
            pause_sleep()
            god = currentYear - q1
            print('Значит ты родился в', god,'году.')
            break


def mult_table():
    while True:
        try:
            test1 = int(input('Сколько будет 6х4 ?\n'))
        except ValueError:
            pause_sleep()
            print('Для ввода ответа используй только цифры. Попробуй еще.')
            pause_sleep()
        else:
            while test1 != 24:
                pause_sleep()
                print('Ответ неверый. Подумай и введи правильный ответ.')
                test1 = int(input('Сколько будет 6х4 ?\n'))
            else:
                pause_sleep()
                print('Ответ правильный. Ты молодец!')
                pause_sleep() 
            break

currentYear = datetime.now().year

name = input('Как тебя зовут?\n')
pause_sleep() 

print('Привет,', name,'. А меня зовут linux, очень рад нашему знакомству!')
pause_sleep()

age_request()
pause_sleep()

let = currentYear - 1991
print('А я родился в 1991 году, сейчас мне', let,'лет.')
pause_sleep()

math = input('Я люблю математику, а ты уже знаешь таблицу умножения?\n')
x = 1
while x == 1:
    if math == 'да' or math == 'д' or math == 'знаю' or math == 'yes' or math == 'y':
        pause_sleep()
        print('Сейчас я это проверю...')
        pause_sleep()
        mult_table()
        pause_sleep()
        x = 0
    elif math == 'нет' or math == 'н' or math == 'no' or math == 'n':
        pause_sleep()
        print('Чему вас только в школе учат! Мне придеться рассазать об этом твоему учителю.')
        pause_sleep()
        print('Иди учи таблицу умножения. До встречи!')
        pause_sleep()
        x = 0
    else:
        pause_sleep()
        math = input('Я не понял твой ответ. Введи "да" или "нет". Можно ввести "yes" или "no".\n')
        




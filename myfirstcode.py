import random
from random import choice as rr
from random import randint as rrrr
from os import system as s
from requests import get as g
def PasswordGenerator():
    Alphabet = 'QWRTYUIOPASDDFGHJKLZMXNBCVqwertyuiopasdfghjklzxcvbnm1234567890_.-'
    z=rrrr(14,22)
    rrr = str("".join(rr(Alphabet) for r in range(z)))
    return(rrr)
    x=input('''enter "save" to save the password to mypass.txt''')
    if x == 'save':
        with open ('mypass.txt','w')as x2:
            x2.write(rrr)
            s('clear')
            return 'Saved succsesfully the pass '+rrr
def mifi(name,wap):
    if mifi == 'hi':
        return 'Hello'
    elif mifi == 'Hello':
        return 'hi'
    else:
        return 'This test module '
def TelegramNormalMessage(token,id,text):
    z=requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={text}')
    return z
def TeleBotMessage(token,messages):
    bot=telebot.TeleBot(token)
    def Welcome(message):
        bot.reply_to(message,messages)
        return 'Done !'
def ism(name):
    return name
def e(problem):
    exit(problem)
def FakeError():
    dj=rrrr(10,20)
    ss='None_Simpleflod_Type='+dj
    return ss
def _(text):#Method print using _
    return text
def close():
    exit()
def clear():
    s('clear')
def Me():
    return {'Myname':'Mustafa'}
def random_randint(a,b):
    x=rrrr(a,b)
    return x
def FakeEveryThing(len,string):
    len='123'
    string='-----'
    return len+string+len
def Return(text):
    return text
def Viral(name,date):
    return 'Hi i am '+name+' i was born on '+date+' Ilovu'
def print(text):
    print(text)

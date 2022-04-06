import time
import os
import random
def out_red(text):
    print("\033[31m {}" .format(text))
def out_yellow(text):
    print("\033[33m {}" .format(text))
def out_blue(text):
    print("\033[34m {}" .format(text))
def out_green(text):
    print("\033[32m {}" .format(text))
logins = "AdminUser, UnionUser"
passwords = "harington1890, UnionUser"
login = input("Введите свой логин : ")
if login in logins:
  time.sleep(0.8)
  password = input("Введите свой пароль : ")
  if password in passwords:
    time.sleep(1)
    os.system("clear")
    time.sleep(0.6)
    out_green("WiFi Jumper")
    time.sleep(1)
    print("Russia")
    time.sleep(0.5)
    out_blue("Russia")
    time.sleep(0.5)
    out_red("Russia")
    time.sleep(0.8)
    wificrack = input("Введите Ip или название сети : ")
    time.sleep(0.6)
    choice = "y"
    
    while choice.lower() == "y":
      time.sleep(0.9)
      cracks = input("Нажмите на Y чтобы начать взлом или другую клавишу для выхода из программы ")
      time.sleep(2)
      out_green(" Please, wait...")
      time.sleep(19)
      out_yellow("Пароль сохранен в текстовом документе WiFi1.txt")
    time.sleep(1)
    print("Заверешение работы программмы...")
    time.sleep(1)
    out_green("Успешно!")
    time.sleep(1)
    os.system("clear")
  else:
    time.sleep(0.4)
    print("Ошибка! Не верный пароль")
else:
  time.sleep(0.4)
  print("Ошибка! Не верный логин")

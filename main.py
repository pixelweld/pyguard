import platform
import shutil

def show_disk_info():
    shutil.disk_usage('/')
    disk = shutil.disk_usage('/')
    
    total_gb = disk.total / (1024 ** 3)
    print('Всего места:', round(total_gb, 2), 'ГБ')
    
    used_gb = disk.used / (1024 ** 3)
    print('Заполнено:', round(used_gb, 2), 'ГБ')
    
    free_gb = disk.free / (1024 ** 3)
    print('Свободно:', round(free_gb, 2), 'ГБ')

def show_system_info():
    print('Операционная система:', platform.system())
    print('Версия ядра:', platform.release())
    print('Архитектура:', platform.machine())
    print('Имя компьютера:', platform.node())

def wait_for_enter():
    input('Нажмите Enter, чтобы вернуться в меню...')

def skobki_tu():
    print('===')

while True:

    print("=== PyGuard ===")
    print('2. Информация о диске')
    print('1. Информация о системе')
    print('0. Выход')
    #ввод
    inp = input('>> ')

    if inp == '1':
        skobki_tu()
        show_system_info()
        skobki_tu()
        wait_for_enter()
    elif inp == '2':
        skobki_tu()
        show_disk_info() 
        skobki_tu() 
        wait_for_enter()
    elif inp == '0':
        print('Вы решили выйти')
        break
    else:
        print('Неизвестная команда')

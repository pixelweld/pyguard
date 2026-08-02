import platform

def show_system_info():
    print('Операционная система:', platform.system())
    print('Версия ядра:', platform.release())
    print('Архитектура:', platform.machine())
    print('Имя компьютера:', platform.node())

while True:

    print("=== PyGuard ===")
    print('1. Информация о системе')
    print('0. Выход')

    #ввод
    inp = input('> ')


    if inp == '1':
        print('===')
        show_system_info()
        print('===')
        input('Нажмите Enter, чтобы вернуться в меню...')
        
    elif inp == '0':
        print('Вы решили выйти')
        break
    else:
        print('Неизвестная команда')

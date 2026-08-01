print("=== PyGuard ===")
print('1. Информация о системе')
print('0. Выход')

#ввод
inp = input('> ')

if inp == '1':
    print('Информация о вашей системе: ')
elif inp == '0':
    print('Вы решили выйти' )
else:
    print('Неизвестная команда')
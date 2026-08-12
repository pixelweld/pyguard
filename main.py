import platform
import shutil
import psutil
import socket
import time

def show_cpu_info():
    physical = psutil.cpu_count(logical=False)
    logical = psutil.cpu_count(logical=True)
    print('Физических ядер:', physical)
    print('Потоков:', logical)

def show_zvezdi():
    
    n = int(input('Введите количество звезд: '))
    print()
    
    middle = n // 2 + 1

    for i in range(1, middle + 1):
        print(i * '*')

    for j in range(middle - 1, 0, -1):
        print(j * '*')


def show_uptime_info():
    boot_time = psutil.boot_time()
    current_time = time.time()
    vse_vremya = current_time - boot_time
    minutes = int((vse_vremya % 3600) // 60)
    seconds = int(vse_vremya % 60)
    hours = int(vse_vremya // 3600)
    print('Система работает:', hours, 'ч.', minutes, 'мин.', seconds, 'сек.')
    
def show_battery_info():
    battery = psutil.sensors_battery()
    print('Заряд батареи:', round(battery.percent, 3), '%')
    
    zaryad = battery.power_plugged


def show_network_info():
    network = psutil.net_io_counters()
    
    for i in range(10):
        filled = '#' * (i + 1)
        empty = '-' * (9 - i)
        print('\rАнализ:', filled + empty, end='')
        time.sleep(0.1)
    print()
    print('===')
    
    network_after = psutil.net_io_counters()
    received_speed_mb = (network_after.bytes_recv - network.bytes_recv) / 1024 ** 2
    sent_speed_mb = (network_after.bytes_sent - network.bytes_sent) / 1024 ** 2
    print('Скорость получения:', round(received_speed_mb, 2), 'МБ/с')
    print('Скорость отправки:', round(sent_speed_mb, 2), 'МБ/с')
    
    interfaces = psutil.net_if_addrs()
    received_mb = network.bytes_recv / 1024 ** 2
    sent_mb = network.bytes_sent / 1024 ** 2
    
    print('Информация о сети(c момента запуска ПК):')
    print('Получено:',round(received_mb, 2),'МБ')
    print('Отправлено:',round(sent_mb, 2),'МБ')

    for interface_name, addresses in interfaces.items():
        for address in addresses:
            if address.family == socket.AF_INET:
                print(
                    'Интерфейс:', interface_name,
                    '| IPv4:', address.address
                )
    
def get_ram(process):
    return process['ram_mb']

def show_process_info():
    processes = psutil.pids()
    print('Запущено процессов:',len(processes))
    
    process_iter = psutil.process_iter(['pid', 'name', 'memory_info'])
    process_list = []
    
    for process in process_iter:
        info = process.info
        ram_mb = info['memory_info'].rss / (1024 ** 2)        
        
        process_data = {
            'pid': info['pid'], 
            'name': info['name'], 
            'ram_mb': ram_mb
            }
        process_list.append(process_data)
    process_list.sort(key=get_ram, reverse=True)
    for process in process_list:
        
        print(
            'PID:', process['pid'],
            '|Процесс:', process['name'],
            '|RAM:', round(process['ram_mb'], 1),'МБ'
        )
        

def show_resources_info():
    cpu = psutil.cpu_percent(interval=1)
    print('(CPU)Загрузка процессора(из 100%):', round(cpu, 2),'%', sep='')
    cpudan = psutil.virtual_memory()
    print('Всего RAM:', round((cpudan.total / 1024 ** 3), 1),'ГБ')
    print('Занято RAM:', round((cpudan.used / 1024 ** 3), 1),'ГБ')
    print('Доступно RAM:', round((cpudan.available / 1024 ** 3), 1),'ГБ')
    print('Использовано RAM:', round(cpudan.percent, 1),'%', sep='')
    
def show_disk_info():
    
    disk = shutil.disk_usage('/')
    
    total_gb = disk.total / (1024 ** 3)
    print('Всего места:', round(total_gb, 2), 'ГБ')
    
    used_gb = disk.used / (1024 ** 3)
    print('Заполнено:', round(used_gb, 2), 'ГБ')
    
    free_gb = disk.free / (1024 ** 3)
    print('Свободно:', round(free_gb, 2), 'ГБ')
    
    disk_percent = disk.used / disk.total * 100
    print('Диск заполнен на:', round(disk_percent, 1), '%')

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

    print()
    print("=== PyGuard ===")
    print('1. Информация о системе')
    print('2. Информация о диске')
    print('3. (CPU)Загрузка процессора и (RAM)оперативная память')
    print('4. Запущенные процессы')
    print('5. Информация о сети')
    print('6. Информация о батарее')
    print('7. Время работы системы')
    print('8. Информация о процессоре')
    print()
    print('01. Звёзды')
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
    elif inp == '3':
        skobki_tu()
        show_resources_info()
        skobki_tu()
        wait_for_enter()
    elif inp == '4':
        skobki_tu()
        show_process_info()
        skobki_tu()
        wait_for_enter()
    elif inp == '5':
        skobki_tu()
        show_network_info()
        skobki_tu()
        wait_for_enter()
    elif inp == '6':
        skobki_tu()
        show_battery_info()
        skobki_tu()
        wait_for_enter()
    elif inp == '7':
        skobki_tu()
        show_uptime_info()
        skobki_tu()
        wait_for_enter()
    elif inp == '8':
        skobki_tu()
        show_cpu_info()
        skobki_tu()
        wait_for_enter()
    elif inp == '01':
        print()
        show_zvezdi()
        print()
        wait_for_enter()
    elif inp == '0':
        print('Вы решили выйти')
        break
    else:
        print('Неизвестная команда')
        

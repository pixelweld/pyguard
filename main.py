import platform
import shutil
import psutil
import socket
import time

def show_network_info():
    network = psutil.net_io_counters()
    
    for i in range(21):
        filled = '#' * (i + 1)
        empty = '-' * (20 - i)
        print('\rАнализ:', filled + empty, end='', flush=True)
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

    print("=== PyGuard ===")
    print('1. Информация о системе')
    print('2. Информация о диске')
    print('3. (CPU)Загрузка процессора и (RAM)оперативная память')
    print('4. Запущенные процессы')
    print('5. Информация о сети')
    print()
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
    elif inp == '0':
        print('Вы решили выйти')
        break
    else:
        print('Неизвестная команда')
        

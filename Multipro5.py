# 5. Użyj `multithreading` do równoczesnego monitorowania różnych zasobów systemowych,
#takich jak zużycie CPU, pamięci i dysku. Aktualizuj wyniki co sekundę.

import threading
import time
import psutil

def monitor_cpu():
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        print(f"CPU Usage: {cpu_usage}%")
        time.sleep(10)

def monitor_memory():
    while True:
        memory_usage = psutil.virtual_memory().percent
        print(f"Memory Usage: {memory_usage}%")
        time.sleep(10)

def monitor_disk():
    while True:
        disk_usage = psutil.disk_usage('/').percent  # Użyj odpowiedniej ścieżki dla swojego systemu
        print(f"Disk Usage: {disk_usage}%")
        time.sleep(10)

if __name__ == "__main__":
    threading.Thread(target=monitor_cpu).start()
    threading.Thread(target=monitor_memory).start()
    threading.Thread(target=monitor_disk).start()

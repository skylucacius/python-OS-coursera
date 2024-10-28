import shutil, psutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total
    return free > 20
    
def check_cpu_usage():
    usage = psutil.cpu_percent(0.1)
    return usage < 75

if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR")
else:
    print("Everything is OK!")
import psutil

def gb_mb_converter(in_bytes):
    in_gb=round(in_bytes/1024**3,2)

    if in_gb < 1:
        in_mb=str(in_bytes/1024**2)+"MB"
        return in_mb
    else:
        return str(in_gb)+"GB"
    
def system_status(sentence):

    #for battery status 
    if "BATTERY" in sentence :
        battery=psutil.sensors_battery()
        if battery :
            print("batery is ",battery.percent,"%")
            if battery.power_plugged:
                return "batery is ",battery.percent,"%","and , power is plugged"
            else:
                return "batery is ",battery.percent,"%","and ,power is not plugged"
        else:
            return "battery not found "
    
    #for ram and storage 
    elif "RAM" in sentence or "MEMORY" in sentence or " STORAG" in sentence:

        #FOR RAM 
        mem=psutil.virtual_memory()

        total_ram=gb_mb_converter(mem.total)
        used_ram=gb_mb_converter(mem.used)
        free_ram=gb_mb_converter(mem.free)

        #FOR STORAGE 
        sto=psutil.disk_usage('/')

        total_sto=gb_mb_converter(sto.total)
        used_sto=gb_mb_converter(sto.used)
        free_sto=gb_mb_converter(sto.free)

        return "total ram is", total_ram, "used ram is",used_ram, "and left free ram is",free_ram, "total storage is", total_sto, "used storage is",used_sto, "and left free storage is",free_sto
        
    elif "SYSTEM STATUS" in sentence:
        full_status = {
            "cpu": psutil.cpu_percent(),
            "memory": psutil.virtual_memory().percent,
            "disk": psutil.disk_usage('/').percent,
            "net": psutil.net_io_counters()
            }
        return full_status
    
    else:
        return "cant load that status "
    
# for test
# while True:
#     a=str(input("enter :"))
#     a=a.upper()
#     print(system_status(a))


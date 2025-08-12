import psutil

# #for memory 
# mem = psutil.virtual_memory()
# print(f"Total: {mem.total}, Used: {mem.used}, Free: {mem.free}")
# print("\n",mem.percent)
# in_mb=mem.total/1024**2
# in_gb=mem.total/1024**3

# print("in mb ", in_mb)
# print("in gb ", in_gb)

# #net status
# net = psutil.net_io_counters()
# print(f"Bytes Sent: {net.bytes_sent}, Bytes Received: {net.bytes_recv}")


#full
snapshot = {
    "cpu": psutil.cpu_percent(),
    "memory": psutil.virtual_memory().percent,
    "disk": psutil.disk_usage('/').percent,
    "net": psutil.net_io_counters()
}
print(snapshot)



# #battery 
# import psutil

# battery = psutil.sensors_battery()

# if battery:
#     print(f"Battery percent: {battery.percent}%")
#     print(f"Plugged in: {battery.power_plugged}")
#     print(f"Time left: {battery.secsleft // 60} minutes")
# else:
#     print("No battery is detected on this system.")

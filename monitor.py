import psutil

print("----Menu:----")
print("1.Check Server Health")
print("2.Exit")

choice=int(input("Enter your choice: "))

if choice==1:
    print("------------------Server Health Dashboard-------------------")
    cpu=psutil.cpu_percent(interval=1)
    memory=psutil.virtual_memory().percent
    disk=psutil.disk_usage('/').percent
    print(f"CPU Usage:{cpu}%")
    print(f"Memory Usage:{memory}%")
    print(f"Disk Usage:{disk}%")
    print("-------------------------------------------------------------")
elif choice==2:
    print("Exiting the program...")
else:
    print('Invalid Choice"')
    exit()

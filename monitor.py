import psutil
import requests
from datetime import datetime

print("----Menu:----")
print("1.Check Server Health")
print("2.Check Users from API")
print("3.save health log to file")
print("4.View health log from file")
print("5. Exit")



def userdetails():
    try:
        url = "https://jsonplaceholder.typicode.com/users"
        response=requests.get(url)
        data=response.json()
        for user in data:
            print(user['username'])
    except exception as e:
        print("Error:",e)

choice=int(input("Enter your choice: "))

if choice==1:
    print("------------------Server Health Dashboard-------------------")
    cpu=psutil.cpu_percent(interval=1)
    memory=psutil.virtual_memory().percent
    disk=psutil.disk_usage('/').percent
    print(f"CPU Usage:{cpu}%")
    print(f"Memory Usage:{memory}%")
    print(f"Disk Usage:{disk}%")
    if(disk>90):
        print("disk threshold exceeded")
    print("-------------------------------------------------------------")
elif choice==2:
    userdetails()
elif choice==3:
    cpu=psutil.cpu_percent(interval=1)
    memory=psutil.virtual_memory().percent
    disk=psutil.disk_usage('/').percent
    with open("health.log","a") as f:
        log_msg=f"{datetime.now()} CPU:{cpu}% Memory:{memory}% Disk:{disk}%"
      
        f.write(log_msg+'\n')
        if disk<90:
            f.write("disk threshold exceeded\n")
elif choice==4:
    try:
        with open("health.log","r") as f:
            logs=f.read()
            print(logs)
    except FileNotFoundError:
        print("Health log file not found.")
    
else:
    print('Invalid Choice"')

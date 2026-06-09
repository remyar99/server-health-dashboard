import psutil
import requests
from datetime import datetime
import subprocess

print("----Menu:----")
print("1.Check Server Health")
print("2.Check Users from API")
print("3.save health log to file")
print("4.View health log from file")
print("5.Network diagnostics")
print("6.Process status check")
print("7. Exit")



def userdetails():
    try:
        url = "https://jsonplaceholder.typicode.com/users"
        response=requests.get(url)
        data=response.json()
        for user in data:
            print(user['username'])
    except exception as e:
        print("Error:",e)
def hostdetails():
    host=input("Enter the host to ping").strip().lower()
    result=subprocess.run(["ping","-c","4",host],capture_output=True,text=True)
    print(result.stdout)
def dnslookup():
    hostname=input("Enter the hostname to lookup")
    result=subprocess.run(["nslookup",hostname],capture_output=True,text=True)
    print(result.stdout)
def webstatus():
    url=input("Enter the website URL:")
    try:
        response=requests.get(url)
        print(f"Website Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print("Error accessing the website:",e)
def process_check():
    process_name=input("Enter the name of the process to check").strip().lower()
    result=subprocess.run(["ps","-ef"],capture_output=True,text=True)
    for line in result.stdout.splitlines():
        if process_name in line:
            print(line)
            found=True
    if found==True:
        print(f"{process_name} is running")
    else:
        print(f"{process_name} is not running")
    

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
elif choice==5:
    network_choice=int(input("1.Ping a host\n2.View IP address\n3.website status\n"))
    if network_choice==1:
        hostdetails()
    elif network_choice==2:
        dnslookup()
    elif network_choice==3:
        webstatus()
    else:
        print("Invalid Choice")
   
elif choice==6:
    process_check()
elif choice==7:
    print("Exiting the program...")
else:
    print("Invalid")

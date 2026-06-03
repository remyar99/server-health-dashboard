import psutil
import requests

print("----Menu:----")
print("1.Check Server Health")
print("2.Check Users from API")
print("3. Exit")



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
    print("-------------------------------------------------------------")
elif choice==2:
    userdetails()
elif choice==3:
    print("Exiting the program...")
else:
    print('Invalid Choice"')
    exit()

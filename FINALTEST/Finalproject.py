import psutil 

monitoring = True

class Main:
    while monitoring:
        choice = input("1.Activate the monitoring app \n2. List the active monitorings \n3. Create an alarm \n4. Show alarm \n5. Exit" )
        if choice == "1":
            print(psutil.cpu_percent())
            print(psutil.virtual_memory())
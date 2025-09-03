import psutil
import time
import threading
import matplotlib.pyplot as plt
import numpy as np






# what we will doing is that we will make this project in two parts 
#            first will be the data collection part where we will collect the data using psutil


#and in second part we will plot the graph and if got time we will be also adding the name of the apps which were not getting used but still using very 
# much of the cpu and ramm

cpu_points=[]
time_points=[]



# how we will collect the data ???
def monitor_cpu():
    

    start= time.time()
    while time.time() - start <= 20:
        cpu = psutil.cpu_percent(interval=1)
        print(f"CPU USAGE IS : {cpu}\t")


def monitor_ram():
    
    start_ram= time.time()
    while time.time() - start_ram <=20:
        ram= psutil.virtual_memory()
        threshold = 1*1024*1024
        if ram.available<= threshold:
            print(f"RAM IS : {ram}")
            time.sleep(2)



cpu_thread = threading.Thread(target=monitor_cpu)
ram_thread = threading.Thread(target=monitor_ram)


# here we have completed the data i.e. we are now going to use matplot lib  to plot the graphs  

# cpu_points= np.array([cpu])
# time_points= np.array([time])

plt.plot(time_points,cpu_points)

plt.show()












cpu_thread.start()
ram_thread.start()


cpu_thread.join()
ram_thread.join()


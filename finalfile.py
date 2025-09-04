# this is final file which contains all the changes and is working fine , it has very less

import psutil
import time
import threading
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO
# from matplotlib.animation import FuncAnimation





cpu_points = []
ram_points = []
time_points = []


plt.ion() 
fig, (ax1, ax2) = plt.subplots(2,1, figsize=(10, 8))

url = "https://wallpapercave.com/wp/wp11032877.jpg"

response = requests.get(url)
img = Image.open(BytesIO(response.content))

# Convert to format compatible with matplotlib
img = img.convert("RGB")



def monitor_cpu_ram():
    start = time.time()
    while time.time() - start <= 20:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        elapsed = time.time() - start
        cpu_points.append(cpu)
        ram_points.append(ram)
        time_points.append(elapsed)
        ax1.clear()
        ax2.clear()
        print(f"CPU USAGE: {cpu}%\tRAM USAGE: {ram}%")


        ax1.imshow(img , extent=[0,20,0,100],aspect='auto',alpha=0.2,zorder=0)
        ax2.imshow(img , extent=[0,20,0,100],aspect='auto',alpha=0.2,zorder=0)

        ax1.plot(time_points, cpu_points, label='CPU Usage (%)',color='green')
        ax2.plot(time_points, ram_points, label='RAM Usage (%)',color='blue')
        ax1.set_xlabel('Time (s)')
        ax1.set_ylabel('CPU Usage (%)')
        ax2.set_ylabel('RAM Usage (%)')
        ax1.set_title('CPU and RAM Usage Over Time')
        ax1.set_ylim(0,100)
        ax2.set_ylim(0,100)
        ax1.legend()
        ax2.legend()
        ax1.grid()
        ax2.grid()
        plt.tight_layout()
        plt.pause(0.1)
      

#till here everything is fine, working and good ,also the graph is working fine and showing data in real time :D



monitor_cpu_ram()





plt.ioff()
plt.show()




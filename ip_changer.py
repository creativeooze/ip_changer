import time
import os
import requests

def ma_ip():
    url = 'https://www.myexternalip.com/raw'
    get_ip = requests.get(url,proxies=dict(http='socks5://127.0.0.1:9050',https='socks5://127.0.0.1:9050'))
    return get_ip.text

def change():
    os.system("sudo service tor reload")
    print('[+] Your IP has been Changed to : '+str(ma_ip()))

time.sleep(3)
print("Change your SOCKES to 127.0.0.1:9050 \n")
os.system("sudo service tor start")
x = input("Time in which you want the ip to change(in seconds): ")

while True:
    try:
        change()
        time.sleep(int(x))
    except KeyboardInterrupt:
        print("\nClosing Tor")
        os.system("sudo service tor stop")
        quit()

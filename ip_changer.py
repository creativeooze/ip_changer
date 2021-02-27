import time
import os
import subprocess
import requests

def ma_ip():
    url = 'https://www.myexternalip.com/raw'
    get_ip = requests.get(url,proxies=dict(http='socks5://127.0.0.1:9050',https='socks5://127.0.0.1:9050'))
    return get_ip.text

def change():
    os.system("service tor reload")
    print('[+] Your IP has been Changed to : '+str(ma_ip()))

os.system("service tor start")

time.sleep(3)
print("\033[1;32;40m change your  SOCKES to 127.0.0.1:9050 \n")
os.system("service tor start")
x = 300

while True:
    try:
        time.sleep(int(x))
        change()
    except KeyboardInterrupt:
        print("\nClosing Tor")
        quit()

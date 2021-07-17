import time
import os
import requests
import platform

def ma_ip():
    url = 'https://www.myexternalip.com/raw'
    get_ip = requests.get(url,proxies=dict(http='socks5://127.0.0.1:9050',https='socks5://127.0.0.1:9050'))
    return get_ip.text

def linux():
    os.system("sudo service tor start")
    while True:
        try:
            os.system("sudo service tor reload")
            print('[+] Your IP has been Changed')
            time.sleep(int(x))
        except KeyboardInterrupt:
            print("\nClosing Tor")
            os.system("sudo service tor stop")
            quit()

def darwin():
    os.system("brew services start tor")
    while True:
        try:
            os.system("brew services reload tor")
            print('[+] Your IP has been Changed')
            time.sleep(int(x))
        except KeyboardInterrupt:
            print("\nClosing Tor")
            os.system("brew services stop tor")
            quit()

time.sleep(3)
print("Change your SOCKES to 127.0.0.1:9050 \n")
x = input("Time in which you want the ip to change(in seconds): ")
pname = platform.system()

if(pname == "Linux"):
    linux()

if(pname == "Darwin"):
    darwin()

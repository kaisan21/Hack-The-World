#!/usr/bin/env python3
import os
import subprocess
import sys
import time
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

def clear():
    os.system('clear')

def banner():
    print(Fore.CYAN + "=" * 60)
    print(Fore.GREEN + """
  _    _            _     _______ _            __          __        _     _ 
 | |  | |          | |   |__   __| |           \ \        / /       | |   | |
 | |__| | __ _  ___| | __   | |  | |__   ___    \ \  /\  / /__  _ __| | __| |
 |  __  |/ _` |/ __| |/ /   | |  | '_ \ / _ \    \ \/  \/ / _ \| '__| |/ _` |
 | |  | | (_| | (__|   <    | |  | | | |  __/     \  /\  / (_) | |  | | (_| |
 |_|  |_|\__,_|\___|_|\_\   |_|  |_| |_|\___|      \/  \/ \___/|_|  |_|\__,_|
    """)
    print(Fore.RED + "       [+] Version: 1.0.0 | Developer: Kaisan [+]")
    print(Fore.CYAN + "=" * 60 + "\n")

def run_cmd(cmd):
    try:
        subprocess.run(cmd, shell=True)
    except Exception as e:
        print(f"{Fore.RED}[!] Error: {e}")

def main_menu():
    while True:
        clear()
        banner()
        print(f"{Fore.YELLOW}[1]{Fore.WHITE} Network Reconnaissance (Nmap)")
        print(f"{Fore.YELLOW}[2]{Fore.WHITE} Web Vulnerability Scanning (SQLMap/Nikto)")
        print(f"{Fore.YELLOW}[3]{Fore.WHITE} WiFi Hacking (Aircrack-ng Suite)")
        print(f"{Fore.YELLOW}[4]{Fore.WHITE} Brute Force Attacks (Hydra)")
        print(f"{Fore.YELLOW}[5]{Fore.WHITE} Exploit Framework (Metasploit)")
        print(f"{Fore.YELLOW}[0]{Fore.WHITE} Exit")
        
        choice = input(f"\n{Fore.GREEN}HTW > {Fore.WHITE}")

        if choice == '1':
            target = input(f"{Fore.BLUE}Enter Target IP/Domain: ")
            print(f"{Fore.YELLOW}[*] Running Intense Scan...")
            run_cmd(f"nmap -A -T4 {target}")
            input("\nPress Enter to return...")

        elif choice == '2':
            url = input(f"{Fore.BLUE}Enter URL (with http/s): ")
            print(f"{Fore.YELLOW}[*] Testing for SQL Injection...")
            run_cmd(f"sqlmap -u {url} --batch --banner")
            input("\nPress Enter to return...")

        elif choice == '3':
            print(f"{Fore.YELLOW}[*] Available Interfaces:")
            run_cmd("iwconfig")
            iface = input(f"{Fore.BLUE}Enter Interface (e.g., wlan0): ")
            print(f"{Fore.YELLOW}[*] Enabling Monitor Mode...")
            run_cmd(f"airmon-ng start {iface}")
            run_cmd(f"airodump-ng {iface}mon")
            input("\nPress Enter to return...")

        elif choice == '4':
            service = input(f"{Fore.BLUE}Enter Service (ssh/ftp/http-post-form): ")
            ip = input(f"{Fore.BLUE}Enter Target IP: ")
            user = input(f"{Fore.BLUE}Enter Username: ")
            passlist = "/usr/share/wordlists/rockyou.txt"
            print(f"{Fore.YELLOW}[*] Starting Hydra Brute Force...")
            run_cmd(f"hydra -l {user} -P {passlist} {ip} {service}")
            input("\nPress Enter to return...")

        elif choice == '5':
            print(f"{Fore.YELLOW}[*] Launching Metasploit Framework...")
            run_cmd("msfconsole")

        elif choice == '0':
            print(f"{Fore.CYAN}Exiting... Happy Hacking, Kaisan.")
            sys.exit()
        
        else:
            print(f"{Fore.RED}[!] Invalid Selection.")
            time.sleep(1)

if __name__ == "__main__":
    if os.getuid() != 0:
        print(f"{Fore.RED}[!] Please run as ROOT (sudo python3 htw.py)")
        sys.exit()
    main_menu()
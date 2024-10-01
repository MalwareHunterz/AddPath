#!/usr/bin/env python3
import os
import subprocess
import sys
import shutil
import time

# Color definitions
RESET = "\033[0m"
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
HIGHLIGHT = "\033[95m"  # Highlight color for files added by AddPath

# Banner
BANNER = f"""
{CYAN}
    ___       __    ______        __  __  
   /   | ____/ /___/ / __ \\____ _/ /_/ /_ 
  / /| |/ __  / __  / /_/ / __ `/ __/ __ \\
 / ___ / /_/ / /_/ / ____/ /_/ / /_/ / / /
/_/  |_\\__,_/\\__,_/_/    \\__,_/\\__/_/ /_/ 

  AddPath Script - by MalwareHunterz  
{RESET}
"""

LOG_FILE = '/usr/local/bin/AddPath_log.txt'

def print_banner():
    print(BANNER)
    time.sleep(0.3)  # Faster animation speed

def check_executable(file_path):
    """Ensure the file is executable, if not, make it executable."""
    if not os.access(file_path, os.X_OK):
        print(f"{YELLOW}[+] Making {file_path} executable...{RESET}")
        os.chmod(file_path, 0o755)

def add_to_log(file_name):
    """Add a file to the AddPath log."""
    with open(LOG_FILE, 'a') as log_file:
        log_file.write(file_name + "\n")

def get_logged_files():
    """Retrieve the list of files that were added using AddPath."""
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as log_file:
            return [line.strip() for line in log_file.readlines()]
    return []

def add_to_path(file_path):
    """Copy the file to /usr/local/bin and add to PATH."""
    destination = '/usr/local/bin/'
    if os.path.isfile(file_path):
        check_executable(file_path)
        destination_path = os.path.join(destination, os.path.basename(file_path))
        print(f"{GREEN}[+] Adding {file_path} to {destination}{RESET}")
        shutil.copy(file_path, destination_path)
        print(f"{GREEN}[+] {file_path} added to PATH.{RESET}")
        add_to_log(os.path.basename(file_path))
    else:
        print(f"{RED}[-] {file_path} not found.{RESET}")
        
def remove_from_path():
    """List all files in /usr/local/bin and allow the user to remove a file."""
    path_files = os.listdir('/usr/local/bin/')
    logged_files = get_logged_files()
    
    # Sort files alphabetically
    path_files = sorted(path_files)

    print(f"{CYAN}Files in /usr/local/bin:{RESET}")
    for idx, file in enumerate(path_files):
        if file in logged_files:
            print(f"{idx+1}. {HIGHLIGHT}{file} (Added by AddPath){RESET}")
        else:
            print(f"{idx+1}. {file}")
    
    choice = input(f"{YELLOW}Enter the number of the file to remove or 'q' to quit: {RESET}")
    if choice.isdigit():
        file_idx = int(choice) - 1
        if 0 <= file_idx < len(path_files):
            file_to_remove = path_files[file_idx]
            file_path = os.path.join('/usr/local/bin', file_to_remove)
            os.remove(file_path)
            print(f"{GREEN}[+] {file_to_remove} removed from PATH.{RESET}")
            # Remove from log if applicable
            if file_to_remove in logged_files:
                logged_files.remove(file_to_remove)
                with open(LOG_FILE, 'w') as log_file:
                    log_file.write("\n".join(logged_files) + "\n")
        else:
            print(f"{RED}[-] Invalid choice.{RESET}")
    else:
        print(f"{RED}[-] Operation canceled.{RESET}")

def install_addpath():
    """Install AddPath to /usr/local/bin."""
    script_path = os.path.abspath(__file__)
    destination = '/usr/local/bin/AddPath'
    check_executable(script_path)
    print(f"{GREEN}[+] Installing AddPath to {destination}...{RESET}")
    shutil.copy(script_path, destination)
    print(f"{GREEN}[+] AddPath installed successfully!{RESET}")
    print(f"{CYAN}[+] You can now run AddPath from anywhere in the terminal!{RESET}")
    add_to_log('AddPath')

def uninstall_addpath():
    """Uninstall AddPath from /usr/local/bin."""
    path = '/usr/local/bin/AddPath'
    if os.path.exists(path):
        os.remove(path)
        print(f"{GREEN}[+] AddPath uninstalled successfully!{RESET}")
        # Remove from log
        logged_files = get_logged_files()
        if 'AddPath' in logged_files:
            logged_files.remove('AddPath')
            with open(LOG_FILE, 'w') as log_file:
                log_file.write("\n".join(logged_files) + "\n")
    else:
        print(f"{RED}[-] AddPath not found in /usr/local/bin.{RESET}")

def print_help():
    """Display the help menu."""
    print(f"""
{CYAN}Usage:{RESET} AddPath [options]
Options:
  {GREEN}-h, --help       {RESET}Show this help message
  {GREEN}-u, --uninstall  {RESET}Uninstall AddPath
  {GREEN}-i, --install    {RESET}Install AddPath
  {GREEN}-t, --add        {RESET}Add a file to PATH
  {GREEN}-r, --remove     {RESET}Remove file from PATH
""")

def main():
    print_banner()
    if len(sys.argv) > 1:
        option = sys.argv[1]
        if option in ['-h', '--help']:
            print_help()
        elif option in ['-i', '--install']:
            install_addpath()
        elif option in ['-u', '--uninstall']:
            uninstall_addpath()
        elif option in ['-t', '--add']:
            if len(sys.argv) == 3:
                file_path = sys.argv[2]
                add_to_path(file_path)
            else:
                print(f"{RED}[-] Please provide the file to add to PATH.{RESET}")
        elif option in ['-r', '--remove']:
            remove_from_path()
        else:
            print(f"{RED}[-] Unknown option: {option}{RESET}")
            print_help()
    else:
        print_help()

if __name__ == "__main__":
    main()

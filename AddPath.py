#!/usr/bin/env python3
import os
import subprocess
import sys
import time

# Colors for terminal output
GREEN = '\033[92m'
RED = '\033[91m'
CYAN = '\033[96m'
RESET = '\033[0m'

# Path to install the executable
BIN_DIR = "/usr/local/bin/"

def print_banner():
    print(f"{CYAN}===========================================")
    print(f"          MalwareHunterz AddPath Script")
    print(f"===========================================\n{RESET}")
    print(f"{RED}Disclaimer: Use this script at your own risk. {RESET}")
    print(f"Moving files can affect your system.")
    print(f"{RED}MalwareHunterz is not responsible for any damage.\n{RESET}")
    print(f"{CYAN}===========================================\n{RESET}")

def list_path_contents():
    """List contents of the BIN_DIR and number them."""
    print(f"\n{CYAN}Current Path Contents in {BIN_DIR}:{RESET}")
    files = os.listdir(BIN_DIR)
    files = [f for f in files if os.path.isfile(os.path.join(BIN_DIR, f))]
    
    for idx, file in enumerate(files, 1):
        print(f"{idx}: {file}")
    
    return files

def install_script():
    """Install the AddPath script."""
    print(f"{GREEN}AddPath is not installed yet. Starting installation...{RESET}")
    install_sh = os.path.join(os.getcwd(), "Install.sh")
    try:
        print(f"Attempting to execute: {install_sh}")
        subprocess.run(["/bin/bash", install_sh], check=True)
        print(f"{GREEN}Installation completed! Restarting AddPath...{RESET}")
        time.sleep(1)
        subprocess.run([sys.executable, "/usr/local/bin/AddPath"], check=True)
        sys.exit(0)
    except subprocess.CalledProcessError as e:
        print(f"{RED}Installation failed: {e}{RESET}")
        if e.output:
            print(f"{RED}Output: {e.output.decode()}{RESET}")
        sys.exit(1)

def uninstall_script():
    """Uninstall a program from the PATH by removing it from BIN_DIR."""
    files = list_path_contents()

    if not files:
        print(f"{RED}No files found in {BIN_DIR}.{RESET}")
        return

    choice = input(f"{CYAN}Enter the number of the file to remove or type 'back' to return to main menu: {RESET}")
    
    if choice.lower() == 'back':
        return

    try:
        choice = int(choice)
        if 1 <= choice <= len(files):
            file_to_remove = files[choice - 1]
            file_path = os.path.join(BIN_DIR, file_to_remove)
            os.remove(file_path)
            print(f"{GREEN}Successfully removed {file_to_remove} from {BIN_DIR}.{RESET}")
        else:
            print(f"{RED}Invalid choice.{RESET}")
    except (ValueError, IndexError):
        print(f"{RED}Invalid input. Please enter a number.{RESET}")

def add_file_to_path(source_file):
    """Add a given file to the $PATH."""
    destination = os.path.join(BIN_DIR, os.path.basename(source_file))
    
    # Copy the file to /usr/local/bin without extension
    destination_without_extension = os.path.splitext(destination)[0]
    try:
        subprocess.run(['sudo', 'cp', source_file, destination_without_extension], check=True)
        subprocess.run(['sudo', 'chmod', '+x', destination_without_extension], check=True)
        print(f"{GREEN}File {source_file} has been added to {BIN_DIR} as {destination_without_extension}.{RESET}")
    except subprocess.CalledProcessError as e:
        print(f"{RED}Error adding file to path: {e}{RESET}")

def show_help():
    """Show help for command usage."""
    print(f"{CYAN}Usage: sudo AddPath [OPTIONS]\n")
    print("Options:")
    print("  -t, --target [FILE]    Specify the file to add to the PATH globally.")
    print("  -u, --uninstall        Uninstall a file from the PATH.")
    print("  -h, --help             Show this help message and exit.")
    print(f"{RESET}")

def check_installed():
    """Check if AddPath is installed in the system."""
    if not os.path.exists("/usr/local/bin/AddPath"):
        install_script()
    else:
        print(f"{GREEN}AddPath is already installed.{RESET}")

def main():
    """Main function to handle script logic."""
    print_banner()

    # Parse command-line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] in ['-h', '--help']:
            show_help()
            sys.exit(0)
        elif sys.argv[1] in ['-t', '--target']:
            if len(sys.argv) < 3:
                print(f"{RED}Error: Missing file target argument.{RESET}")
                sys.exit(1)
            source_file = sys.argv[2]
            add_file_to_path(source_file)
        elif sys.argv[1] in ['-u', '--uninstall']:
            uninstall_script()
        else:
            print(f"{RED}Error: Unknown option {sys.argv[1]}.{RESET}")
            show_help()
            sys.exit(1)
    else:
        print(f"{RED}Error: No options provided. Use -h for help.{RESET}")
        show_help()

if __name__ == "__main__":
    check_installed()
    main()

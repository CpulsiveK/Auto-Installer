import platform
import os
import pyfiglet


os_release_info = platform.freedesktop_os_release()
current_os = os_release_info['NAME']

welcome_message = pyfiglet.figlet_format("WELCOME TO AUTO-INSTALLER", justify="center", width=80)
print(welcome_message)

os_package_mangers = {
    'Fedora Linux': 'dnf',
    'Windows': 'winget',
    'Mac Os': 'brew'
}

softwares_to_install = []

def installer(current_os, softwares_to_install):
    if current_os and current_os in os_package_mangers:
            
            if "Linux" in current_os:
                for software in softwares_to_install:
                    os.system(f"sudo {os_package_mangers[current_os]} install -y {software}")
                    print(os_package_mangers[current_os])
            else:
                for software in softwares_to_install:
                    os.system(f"{os_package_mangers[current_os]} install -y {software}")
    
print(
    "Enter list of softwares you wish to be installed and enter 'done' to begin installation")

while True:
    softwares = input(">>> ")

    if softwares.lower() == "done":
        answer = input(f"Do you want to install these softwares {softwares_to_install}?(y/n): ")

        if answer.lower() == "y":
            break
        elif answer.lower() == "n":
            continue
        else:
            print("[Error] Wrong input!, please try again")
            continue

    softwares_to_install.append(softwares)

installer(current_os, softwares_to_install)
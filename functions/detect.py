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
    import urllib
    import requests
    from bs4 import BeautifulSoup
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

    if remote == True:
        try:
            if langage == "c" or langage == "c++":
                try:
                    command = re.search(r"((gcc|g\+\+) .*?)\\r\\n", str(payload)).group(1)
                    if command != '':
                        command = re.sub(' \S*\.cpp', ' /tmp/' + str(name) + '.cpp', command)
                        command = re.sub(' \S*\.c', ' /tmp/' + str(name) + '.c', command)
                        command = re.sub('-o \S*', '-o /tmp/' + str(name), command)
                        print(infos.GOOD + "COMPILING OPTIONS DETECTED : " + command)

                except: 
                    command = "gcc /tmp/" + str(name_ext) + " -o /tmp/" + str(name)
                    print(infos.INFO + "COMPILING OPTIONS NOT DETECTED, BY DEFAULT : " + command)


                payload_split = payload.splitlines()
                usage = re.search("(\.\/.*?)\',", str(payload_split)).group(1)
                if usage != '':
                    usage = re.sub('(\.\/.*? )', ' /tmp/' + str(name) + ' ', usage)
                    print(infos.GOOD + "USAGE DETECTED : " + usage)        

            elif langage == "sh":
                usage = re.search(r"(sh .*?)\\r\\n", str(payload)).group(1)
                if usage != '':
                    usage = re.sub(' \S*\.sh', ' /tmp/' + str(name_ext), usage)
                    print(infos.GOOD + "USAGE DETECTED : " + usage)

            elif langage == "ruby":
                usage = re.search(r"(ruby .*?)\\r\\n", str(payload)).group(1)
                if usage != '':
                    usage = re.sub(' \S*\.rb', ' /tmp/' + str(name_ext), usage)
                    print(infos.GOOD + "USAGE DETECTED : " + usage)

            elif langage == "perl":
                usage = re.search(r"(perl .*?)\\r\\n", str(payload)).group(1)
                if usage != '':
                    usage = re.sub(' \S*\.pl', ' /tmp/' + str(name_ext), usage)
                    print(infos.GOOD + "USAGE DETECTED : " + usage)

            elif langage == "python":
                usage = re.search(r"(python .*?)\\r\\n", str(payload)).group(1)
                if usage != '':
                    usage = re.sub(' \S*\.py', ' /tmp/' + str(name_ext), usage)
                    print(infos.GOOD + "USAGE DETECTED : " + usage)

            elif langage == "php":
                usage = re.search(r"(php .*?)\\r\\n", str(payload)).group(1)
                if usage != '':
                    usage = re.sub(' \S*\.php', ' /tmp/' + str(name_ext), usage)
                    print(infos.GOOD + "USAGE DETECTED : " + usage)


        except AttributeError:
            if langage == "c" or langage == "c++": 
                usage = "/tmp/" + str(name)
                print(infos.INFO + "USAGE NOT DETECTED, BY DEFAULT : " + usage)

            elif langage == "sh":
                usage = "sh /tmp/" + str(name_ext)
                print(infos.INFO + "USAGE NOT DETECTED, BY DEFAULT : " + usage)

            elif langage == "ruby":
                usage = "ruby /tmp/" + str(name_ext)
                print(infos.INFO + "USAGE NOT DETECTED, BY DEFAULT : " + usage)

            elif langage == "perl":
                usage = "perl /tmp/" + str(name_ext)
                print(infos.INFO + "USAGE NOT DETECTED, BY DEFAULT : " + usage)

            elif langage == "python":
                usage = "python /tmp/" + str(name_ext)
                print(infos.INFO + "USAGE NOT DETECTED, BY DEFAULT : " + usage)

            elif langage == "php":
                usage = "php /tmp/" + str(name_ext)
                print(infos.INFO + "USAGE NOT DETECTED, BY DEFAULT : " + usage)         


    elif remote == None:
        try:
            if langage == "c" or langage == "c++":
                try:
                    command = re.search(r"((gcc|g\+\+) .*?)\\r\\n", str(payload)).group(1)
                    if command != '':
                        command = re.sub(' \S*\.cpp', ' /tmp/exploit/' + str(name) + '.cpp', command)
                        command = re.sub(' \S*\.c', ' /tmp/exploit/' + str(name) + '.c', command)
                        command = re.sub('-o \S*', '-o /tmp/exploit/' + str(name), command)
                        print(infos.INFO + "COMPILING OPTIONS DETECTED : " + command)

                except:
                    command = "gcc /tmp/" + str(name_ext) + " -o /tmp/exploit/" + str(name)
                    print(infos.INFO + "COMPILING OPTIONS NOT DETECTED, BY DEFAULT : " + command)

                payload_split = payload.splitlines()
                usage = re.search("(\.\/.*?)\',", str(payload_split)).group(1)
                if usage != '':
                    usage = re.sub('(\.\/.*? )', ' /tmp/exploit/' + str(name) + ' ', usage)
                    print(infos.GOOD + "USAGE DETECTED : " + usage)

            elif langage == "sh":
                usage = re.search(r"(sh .*?)\\r\\n", str(payload)).group(1)
                if usage != '':
                    usage = re.sub(' \S*\.sh', ' /tmp/exploit/' + str(name_ext), usage)
                    print(infos.GOOD + "USAGE DETECTED : " + usage)

            elif langage == "ruby":
                usage = re.search(r"(ruby .*?)\\r\\n", str(payload)).group(1)
                if usage != '':
                    usage = re.sub(' \S*\.rb', ' /tmp/exploit/' + str(name_ext), usage)
                    print(infos.GOOD + "USAGE DETECTED : " + usage)

            elif langage == "perl":
                usage = re.search(r"(perl .*?)\\r\\n", str(payload)).group(1)
                if usage != '':
                    usage = re.sub(' \S*\.pl', ' /tmp/exploit/' + str(name_ext), usage)
                    print(infos.GOOD + "USAGE DETECTED : " + usage)

            elif langage == "python":
                usage = re.search(r"(python .*?)\\r\\n", str(payload)).group(1)
                if usage != '':
                    usage = re.sub(' \S*\.py', ' /tmp/exploit/' + str(name_ext), usage)
                    print(infos.GOOD + "USAGE DETECTED : " + usage)

            elif langage == "php":
                usage = re.search(r"(php .*?)\\r\\n", str(payload)).group(1)
                if usage != '':
                    usage = re.sub(' \S*\.php', ' /tmp/exploit/' + str(name_ext), usage)
                    print(infos.GOOD + "USAGE DETECTED : " + usage)


        except AttributeError:
            if langage == "c" or langage == "c++":
                usage = "/tmp/exploit/" + str(name)
                print(infos.INFO + "USAGE NOT DETECTED, BY DEFAULT : " + usage)

            elif langage == "sh":
                usage = "sh /tmp/exploit/" + str(name_ext)
                print(infos.INFO + "USAGE NOT DETECTED, BY DEFAULT : " + usage)

            elif langage == "ruby":
                usage = "ruby /tmp/exploit/" + str(name_ext)
                print(infos.INFO + "USAGE NOT DETECTED, BY DEFAULT : " + usage)

            elif langage == "perl":
                usage = "perl /tmp/exploit/" + str(name_ext)
                print(infos.INFO + "USAGE NOT DETECTED, BY DEFAULT : " + usage)

            elif langage == "python":
                usage = "python /tmp/exploit/" + str(name_ext)
                print(infos.INFO + "USAGE NOT DETECTED, BY DEFAULT : " + usage)

            elif langage == "php":
                usage = "php /tmp/exploit/" + str(name_ext)
                print(infos.INFO + "USAGE NOT DETECTED, BY DEFAULT : " + usage)



def CVEFound(equalize_parser, description, detect_cve_name, check):
    n = 0
    equalizer = ""
    del equalize_parser[0]
    header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36","X-Requested-With": "XMLHttpRequest"}

    try:
        if len(description) < 50:
            for i in range(0, len(description)):
                detect_edb = re.search('"(.*?)"', str(description[i])).group(0).strip('""')
                sock_edb = urllib.request.urlopen(exploit_db + "raw/" + detect_edb)
                payload = sock_edb.read()
                sock_edb.close()

                info.GuessLang(str(payload))
                equalizer = equalize_parser[i].find(detect_cve_name[n])
                if payload != "":
                    if equalizer != -1:
                        print(bcolors.RED + bcolors.BOLD + "CVE-" + bcolors.ENDC + bcolors.ENDC + detect_cve_name[n] + " : " + description[i] + info.findlang)
                        info.IsCheck(description, i, check)
                        n += 1
                        if n == len(detect_cve_name):
                            break
                    else:
                        print(bcolors.RED + bcolors.BOLD + "CVE-NONE" + bcolors.ENDC + bcolors.ENDC + " : " + description[i] + info.findlang)
                        info.IsCheck(description, i, check)
                else:
                    if equalizer != -1:
                        print(bcolors.RED + bcolors.BOLD + "CVE-" + bcolors.ENDC + bcolors.ENDC + detect_cve_name[n] + " : " + description[i])
                        info.IsCheck(description, i, check)
                        n += 1
                        if n == len(detect_cve_name):
                            break
                    else:
                        print(bcolors.RED + bcolors.BOLD + "CVE-NONE" + bcolors.ENDC + bcolors.ENDC + " : " + description[i])
                        info.IsCheck(description, i, check)

        else:
            print(infos.ERROR + "Too many results, be more specific !")

    except:
        print("")
        print(infos.ERROR + "Be careful, maybe not all CVEs are displayed.") 
        pass



def SearchExploit(software, check): 

    if software == None:
        pass

    else:
        print("\n" + infos.PROCESS + "SEARCHING...")
        header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36","X-Requested-With": "XMLHttpRequest"}
        url = exploit_db + "search?q=" + software
        print(infos.INFO + "SEARCHING FOR : " + url)
        sock_find = requests.get(url, headers = header)
        findme = BeautifulSoup(sock_find.text, 'html.parser')
        try:
            detect_cve_name = re.findall('\"cve\"\,\"code\"\:\"(.*?)\"', str(findme), re.DOTALL)
            description = re.findall('description\"\:(.*?)\,\"type_id', str(findme), re.DOTALL)
            equalize_parser = str(findme).split('description')
            if detect_cve_name == [] and description == []:
                print("\n" + infos.GOOD + "No CVE found for this software version !")
                print("")
            else:
                print(infos.GOOD + "EXPLOITS FOUND : " + "\n")
                if description == [] and detect_cve_name != []:
                    for i in range(0, len(detect_cve_name)):
                        print(bcolors.RED + bcolors.BOLD + "CVE-" + bcolors.ENDC + bcolors.ENDC + detect_cve_name[i] + " : " + "No description found.")
                        info.IsCheck(detect_cve_name, i, check)
                    print("")
                else:
                    CVEFound(equalize_parser, description, detect_cve_name, check)
                    print("")

        except RuntimeError:
            print(infos.ERROR + "Too many results, be more specific !\n")

        except:
            print(infos.ERROR + "Error during the detection !\n")



def DetectCVE(site, detect, check):
    if site == "exploit_db":
        if detect == None:
            pass

        else:
            print("\n" + infos.PROCESS + "DETECTING...")
            os_uname = os.uname()
            os_concat = os_uname[0] + ' ' + os_uname[2]
            os_version_number = re.search('(.*?)-', os_concat).group(1)
            print(infos.GOOD + "KERNEL FOUND : " + os_version_number)

            header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36","X-Requested-With": "XMLHttpRequest"}
            url = exploit_db + "search?text=" + os_version_number
            print(infos.INFO + "SEARCHING FOR : " + url)
            sock_detect = requests.get(url, headers = header)
            findme = BeautifulSoup(sock_detect.text, 'html.parser')
            equalize_parser = str(findme).split('description')
            try:
                detect_cve_name = []
                description = re.findall('description\"\:(.*?)\,\"type_id', str(findme), re.DOTALL)
                for z in description:
                    detect_cve_name.append("None")
                if detect_cve_name == [] and description == []:
                    print(infos.GOOD + "This machine does not seams vulnerable !")
                    print("")
                else:
                    print(infos.GOOD + "POSSIBLE EXPLOITS : " + "\n")
                    if description == [] and detect_cve_name != []:
                        for i in range(0, len(detect_cve_name)):
                            print(bcolors.RED + bcolors.BOLD + "CVE-" + bcolors.ENDC + bcolors.ENDC + detect_cve_name[i] + " : " + "No description found.")
                            info.IsCheck(detect_cve_name, i, check)
                        print("")
                    else:
                        CVEFound(equalize_parser, description, detect_cve_name, check)
                        print("")

            except RuntimeError:
                print(infos.ERROR + "Too many results, be more specific !\n")

            except:
                print(infos.ERROR + "Error during the detection !\n")

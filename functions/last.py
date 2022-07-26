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
    import random
    import requests


except ImportError:
    print("\n" + infos.ERROR + "Error. Have you installed the requirements properly?")
    print(infos.INFO + "Be sure to run the script as follows:")
    print(infos.INFO + "python3 cve-maker.py ....")
    print(infos.INFO + "./cve-maker.py ....\n")

opencve = "https://www.opencve.io/cve"

ua = open('headers.txt').read().splitlines()
header = {"User-Agent": random.choice(ua), "X-Requested-With": "XMLHttpRequest"}

def GetLastCritical():
    print("\n" + infos.INFO + "SEARCHING FOR : " + opencve + "?cvss=critical&search=")
    url = opencve + "?cvss=critical&search="
    sock_critical = requests.get(url, headers = header)

    criticals = re.findall("<strong>(CVE-.*)<\/strong>.*\n.*\n.*<td class=\"col-md-.\"><span class=\"badge badge-primary\">.<\/span> <a href='\/cve\?vendor=(.*?)&product=.*?'>(.*?)<\/a>.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*<tr class=\"cve-summary\">\n.*colspan=\"5\">(.*)<\/td>\n.*<\/tr>", sock_critical.text)
    print()
    for i in range(len(criticals)):
        print(bcolors.RED + bcolors.BOLD + criticals[i][0] + bcolors.ENDC + bcolors.ENDC + " : " + bcolors.OCRA + bcolors.BOLD + criticals[i][1].upper() + bcolors.ENDC + bcolors.ENDC + "/" + bcolors.PURPLE + bcolors.BOLD + criticals[i][2] + bcolors.ENDC + bcolors.ENDC + " - " + criticals[i][3])
    print()

def GetLast(software):
    print("\n" + infos.PROCESS + "SEARCHING FOR THE LASTS VULNS...")
    print(infos.INFO + "SEARCHING FOR : " + opencve + "?search=" + software)
    url = opencve + "?search=" + software
    sock_last = requests.get(url, headers = header)

    lasts = re.findall("<strong>(CVE-.*)<\/strong>.*\n.*\n.*<td class=\"col-md-.\"><span class=\"badge badge-primary\">.<\/span> <a href='\/cve\?vendor=(.*?)&product=.*?'>(.*?)<\/a>.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*<tr class=\"cve-summary\">\n.*colspan=\"5\">(.*)<\/td>\n.*<\/tr>", sock_last.text)
    print()
    if len(lasts) != 0:
        for i in range(len(lasts)):
            print(bcolors.RED + bcolors.BOLD + lasts[i][0] + bcolors.ENDC + bcolors.ENDC + " : " + bcolors.OCRA + bcolors.BOLD + lasts[i][1].upper() + bcolors.ENDC + bcolors.ENDC + "/" + bcolors.PURPLE + bcolors.BOLD + lasts[i][2] + bcolors.ENDC + bcolors.ENDC + " - " + lasts[i][3])
    else:
        print(bcolors.RED + bcolors.BOLD + "No CVE founded for " + software + bcolors.ENDC + bcolors.ENDC)
    print()

def GetDescription(cve,edb):

    global cves

    print("\n" + infos.PROCESS + "SEARCHING FOR CVE INFORMATIONS...")
    cves = []
    if cve != None or edb != None:
        if cve != None:
            if 'CVE-' not in cve:
                cve = "CVE-" + cve
            cves.append(cve)
        elif edb != None:
            edb = edb.strip('EDB-')
            url = "https://www.exploit-db.com/exploits/" + edb
            sock_cve = requests.get(url, headers = header)
            cve_name = re.findall("target=\"_blank\">.*\n(.*?-.*?)\n.*<\/a>",sock_cve.text)
            for cve in cve_name:
                cve = "CVE-" + cve.strip(' ')
                cves.append(cve)
            if cve_name == []:
                print()
                print(bcolors.RED + bcolors.BOLD + "No CVE founded for EDB-" + edb + bcolors.ENDC + bcolors.ENDC)

        if cves != None:
            for id_cve in cves:
                print(infos.INFO + "SEARCHING FOR " + opencve + "/" + cve)
                url = opencve + "/" + cve
                sock_description = requests.get(url, headers = header)
                print()

                description = re.findall("<div class=\"box-body\">.*\n.*<span class=\"dropcap\">(.*?)\n.*<\/div>", sock_description.text)
                try:
                    print(bcolors.RED + bcolors.BOLD + id_cve + bcolors.ENDC + bcolors.ENDC + " : " + description[0].replace('</span>',''))
                except IndexError:
                    if url == "":
                        print(bcolors.RED + bcolors.BOLD + "No CVE founded for EDB-" + edb + bcolors.ENDC + bcolors.ENDC)
                    else:
                        print(infos.ERROR + "Verify your CVE/EDB ID !")
                        print()
            
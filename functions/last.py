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
    import requests


except ImportError:
    print("\n" + infos.ERROR + "Error. Have you installed the requirements properly?")
    print(infos.INFO + "Be sure to run the script as follows:")
    print(infos.INFO + "python3 cve-maker.py ....")
    print(infos.INFO + "./cve-maker.py ....\n")

opencve = "https://www.opencve.io/cve"

def GetLastCritical():
    print("\n" + infos.INFO + "SEARCHING FOR : " + opencve + "?cvss=critical&search=")
    header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36","X-Requested-With": "XMLHttpRequest"}
    url = opencve + "?cvss=critical&search="
    sock_critical = requests.get(url, headers = header)

    criticals = re.findall("<strong>(CVE-.*)<\/strong>.*\n.*\n.*<td class=\"col-md-.\"><span class=\"badge badge-primary\">.<\/span> <a href='\/cve\?vendor=(.*?)&product=.*?'>(.*?)<\/a>.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*<tr class=\"cve-summary\">\n.*colspan=\"5\">(.*)<\/td>\n.*<\/tr>", sock_critical.text)
    print()
    for i in range(len(criticals)):
        print(bcolors.RED + bcolors.BOLD + criticals[i][0] + bcolors.ENDC + bcolors.ENDC + " : " + bcolors.OCRA + bcolors.BOLD + criticals[i][1].upper() + bcolors.ENDC + bcolors.ENDC + "/" + bcolors.PURPLE + bcolors.BOLD + criticals[i][2] + bcolors.ENDC + bcolors.ENDC + " - " + criticals[i][3])
    print()

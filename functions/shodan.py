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
    import shodan
    import requests
    from bs4 import BeautifulSoup


except ImportError:
    print("\n" + infos.ERROR + "Error. Have you installed the requirements properly?")
    print(infos.INFO + "Be sure to run the script as follows:")
    print(infos.INFO + "python3 cve-maker.py ....")
    print(infos.INFO + "./cve-maker.py ....\n")

cve_details = "https://www.cvedetails.com/cve/"


def ProductVersionIdentify(cve):

    global vendors_versions
    global products_versions

    vendors_versions = []
    products_versions = []

    print("\n" + infos.INFO + "SEARCHING FOR : " + cve_details + cve)
    header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36","X-Requested-With": "XMLHttpRequest"}
    url = cve_details + cve
    sock_cve_details = requests.get(url, headers = header)

    cve_defaults_table = BeautifulSoup(sock_cve_details.text, 'lxml')

    for i in range(len(cve_defaults_table.find_all('table'))):
        if "Product Type" in str(cve_defaults_table.find_all('table')[i]):
            bs4_table = cve_defaults_table.find_all('table')[i]

    product_version_re = re.findall("<a href=\"\/vendor.*\">(.*)<\/a> <\/td>\n.*\n<a href=\"\/product.*\">(.*)<\/a> <\/td>\n.*<td>\n(.*)<\/td>", str(bs4_table))
    for result in product_version_re:
        vendors_versions.append(str(result[0] + " " + result[2].strip('\t')))
        products_versions.append(str(result[1] + " " + result[2].strip('\t')))

    print(infos.PROCESS + "DETERMINATION OF IMPACTED PRODUCTS...")

def Shodan(api_key,vendors_versions,products_versions,cve, find):

    api = shodan.Shodan(api_key)

    try: 
        os.makedirs("/tmp/reports")
    except OSError:
        if not os.path.isdir("/tmp/reports"):
            Raise

    if find == None:
        print(infos.INFO + "SEARCHING FOR : " + str(vendors_versions).strip('[]') + ", " + str(products_versions).strip('[]') )
        print()
        print(infos.PROCESS + "CONNECTING TO SHODAN...\n")
        for vendor_version in vendors_versions:
            if "*" in vendor_version:
                result = api.search(vendor_version[:-2])
            else:
                result = api.search(vendor_version)

            if result['total'] != 0:
                report_path = "/tmp/reports/" + cve
                try: 
                    os.makedirs(report_path)
                except OSError:
                    if not os.path.isdir(report_path):
                        Raise
            
                report_name = report_path + "/" + vendor_version
                with open(report_name, "w") as report:
                    for match in result['matches']:
                        report.write("IP : {}".format(match['ip_str'] + "\n"))
                        report.write(match['data'] + "\n\n")
            
                print(infos.GOOD + "REPORT CREATED : " + report_name + " - " + str(result['total']) + " results.")

        for product_version in products_versions:
            if "*" in product_version:
               result = api.search(product_version[:-2])
            else:
                result = api.search(product_version)

            if result['total'] != 0:
                report_path = "/tmp/reports/" + cve
                try: 
                    os.makedirs(report_path)
                except OSError:
                    if not os.path.isdir(report_path):
                        Raise
            
                report_name = report_path + "/" + product_version
                with open(report_name, "w") as report:
                    for match in result['matches']:
                        report.write("IP : {}".format(match['ip_str'] + "\n"))
                        report.write(match['data'] + "\n\n")
            
                print(infos.GOOD + "REPORT CREATED : " + report_name + " - " + str(result['total']) + " results.")

    else:
        print()
        print(infos.INFO + "SEARCHING FOR : " + vendors_versions)
        print()
        print(infos.PROCESS + "CONNECTING TO SHODAN...\n")
        result = api.search(vendors_versions)
        if result['total'] != 0:    
            report_name = "/tmp/reports/" + vendors_versions
            with open(report_name, "w") as report:
                for match in result['matches']:
                    report.write("IP : {}".format(match['ip_str'] + "\n"))
                    report.write(match['data'] + "\n\n")
            
            print(infos.GOOD + "REPORT CREATED : " + report_name + " - " + str(result['total']) + " results.")

    print()

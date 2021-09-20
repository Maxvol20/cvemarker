<a target="_blank" href="https://img.shields.io/badge/platform-linux-success.svg" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/platform-linux-success.svg">
</a>
<a target="_blank" href="https://img.shields.io/badge/version-2.3-yellow" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/version-2.4.1-yellow">
</a>
<a href="https://www.python.org/" rel="nofollow">
    <img src="https://img.shields.io/badge/python-3.7-red">
</a>
<a href="https://github.com/msd0pe-1/cve-maker-master/blob/master/LICENSE" rel="nofollow">
    <img src="https://img.shields.io/badge/license-GPLv3-9cf.svg">
</a>
<h1>CVE-MAKER</h1>

Use this software <strong>only for legal purposes</strong>. (Example: Vulnerable training machines.)<br />
I am in no way responsible for your actions.<br />
Use python 3.7<br />
<strong>Made by msd0pe</strong><br />

<h2>WHAT IS IT ?</h2>

Cve-maker is a python tool to detect, find, compile and execute a CVE on the current or a remote machine.<br />
It is intended to save you time.
You can easily find your CVEs on https://www.exploit-db.com/ or with the Search option.

<h2>HOW IT WORKS ?</h2>

Cve-maker will search on CVE databases for the payload associated with the CVE that you provide it with parameters.<br />
It creates it in the directory "/tmp/exploits/" and compiles it if necessary. It then proposes you to execute it or not.<br /><br />

<p align="center">
  <img src="https://user-images.githubusercontent.com/47142249/133314342-b71b3f9e-d375-4b56-83f0-638e1a6547b1.PNG">
</p>

<h2>RESEARCH</h2>
<p align="center">
  <img src="https://user-images.githubusercontent.com/47142249/133314331-74ed111f-2dd6-432b-bfd9-80ea37cf7582.PNG">
</p>
Search your CVEs by entering keywords !

<h2>SHODAN</h2>
<p align="center">
  <img src="https://user-images.githubusercontent.com/47142249/133314344-eab96b1e-af9b-40bc-a794-fb5b943262cb.PNG">
</p>
Search directly impacted devices around the world !

<h2>DETECTION</h2>
<p align="center">
  <img src="https://user-images.githubusercontent.com/47142249/71582391-5a20fc80-2b0a-11ea-8136-9ccd4026e381.PNG">
</p>
The detection option will search if a CVE match with your Kernel version !
But not all possible CVEs are displayed: those between 2 versions (e. g. Linux Kernel 2.6.10 < 2.6.31) must be found manually

<h2>REMOTE</h2>
<p align="center">
    <img src="https://user-images.githubusercontent.com/47142249/71582460-9f452e80-2b0a-11ea-9e36-f2c186c69279.PNG">
</p>
Attack remotely with a Reverse Shell, a Bind Shell or a SSH connection !

<h2>INSTALLATION</h2>
Download the project:
<code>git clone https://github.com/msd0pe-1/cve-maker/</code><br />
You only need to execute install.sh to get the libraries useful to the program : <code>sh install.sh</code><br />

<h2>USAGE</h2>
<pre>
    <code>
Usage: python cve-maker.py [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -d, --detect          detect vulnerabilities on the current machine
  -i, --check           check if the edb-id is verified
  -r, --remote          attack a target remotely
  -n, --noexec          don't execute the exploit
  -f FIND, --find=FIND  looking for an exploit by its vulnerable software
  -c CVE, --cve=CVE     looks for the CVE from its name
  -e EDB, --edb=EDB     looks for the CVE from its EDB-ID
  -l LANG, --lang=LANG  langage of the exploit. [Default: c]
  --critical            show the last criticals vulnerabilities
  --shodan              search targets from a given CVE

  Langages:
    sh  ruby  perl  python  php  c++  c  metasploit  text

  Examples:
    python cve-maker.py -f "Apache 2.4"
    python cve-maker.py -e 12345 -l ruby -n
    python cve-maker.py -c 2019-98765 --shodan
    python cve-maker.py -f "php 8.1.0" --shodan
    python cve-maker.py --critical

  Tool to detect, find, compile and execute a CVE on the current or a remote machine.
  Source code put in public domain by msd0pe,no Copyright
  Any malicious or illegal activity may be punishable by law
  Use at your own risk
    </code>
</pre>

<h2>CONTRIBUTING</h2>

This project is in active development. Feel free to suggest a new feature or open a pull request !

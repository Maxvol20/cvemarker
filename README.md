<h1>CVE-MAKER</h1>

This tool is usefull to complete https://github.com/jondonas/linux-exploit-suggester-2<br />
Use python 2.7<br />
<strong>Made by msd0pe</strong><br />

<h2>WHAT IS IT ?</h2>

Cve-maker is a python tool to find, compile and execute a CVE on the current machine.<br />
It is intended to save you time.
You can easily find your CVEs on https://www.exploit-db.com/

<h2>HOW IT WORKS ?</h2>

Cve-maker will search on CVE databases for the payload associated with the CVE that you provide it with parameters.<br />
It creates it in the directory "/tmp/exploit/" and compiles it if necessary. It then proposes you to execute it or not.<br /><br />

<p align="center">
  <img src="https://user-images.githubusercontent.com/47142249/60006167-37e88680-9670-11e9-94c1-d085e3fc993c.png"
</p>

<h2>INSTALLATION</h2>
Installation of the prerequisites: <code>apt-get install gcc g++ git python2.7</code><br />

Download the project:
<code>git clone https://github.com/msd0pe-1/cve-maker-master/</code><br />
  
You only need to execute install.sh to get the libraries useful to the program : <code>sh install.sh</code><br />

<h2>USAGE</h2>
<pre>
    <code>
Usage: python cve-maker.py [options] site

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -c CVE, --cve=CVE     looks for the CVE from its name.
  -e EDB, --edb=EDB     looks for the CVE from its EDB-ID.
  -g GCC, --gcc=GCC     add options to compilation.
  -l LANG, --lang=LANG  langage of the exploit. [Default: c]

  Available 0day sites:
    exploit_db

  Langages:
    sh  ruby  perl  python  php  c++  c

  Examples:
    python cve-maker -e 12345 -l ruby exploit_db   
    python cve-maker -c 2019-98765 -g "-lpthread" exploit_db

  Tool to find, compile and execute a CVE on the current machine.
  Source code put in public domain by msd0pe,no Copyright
  Any malicious or illegal activity may be punishable by law
  Use at your own risk
    </code>
</pre>

<h2>EXAMPLES</h2>

If you want to get the CVE thanks to its EDB-ID : 12345, coded in Ruby:<br />
<code>python cve-maker -e 12345 -l ruby exploit_db</code><br /><br />

If you have the CVE name, and it needs the gcc option "-lpthread" to be compiled correctly :<br />
<code>python cve-maker -c 2019-98765 -g "-lpthread" exploit_db</code>

<h2>CONTRIBUTING</h2>

This project is in active development. Feel free to suggest a new feature or open a pull request !

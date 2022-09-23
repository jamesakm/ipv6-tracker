# ipv6-tracker

# Script dependencies

Python3

Modules - re,ipaddress,os and subprocess

Usage :
======

Clone the ipv6-extracter.py to your local machine.

$git clone https://github.com/jamesakm/ipv6-tracker.git


Script execution  :
-------------------

Make the script as executable

$ chmod 755 ipv6-extracter.py

$ ./ipv6-extracter.py

OR

$python3 ipv6-extracter.py

Enter the log file location : Web access log

Enter result file name for the host : host name


If there are IPV6 addresses present in the given access log you can see the result in the generated hostname.txt file, with the counts.


EXAMPLE :
-------

$./ipv6-extracter.py

Enter the log file location : host01_accesslog_sample.log

Enter result file name for the host : host01

$cat hostname.txt
   
    406 fd50:a72b:9d01:8000:8edc:d4ff:fe67:3406



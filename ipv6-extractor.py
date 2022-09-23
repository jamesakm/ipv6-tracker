#!/usr/bin/python3

#IPV6 address filter from a log file
#Script dependencies - Python3
#Modules - re,ipaddress,os and subprocess

#Contact jmathew@in.rm.com

import re,ipaddress,os,subprocess

#Input log file location
logfile = input("\nEnter the log file location : ")
result = input("\nEnter the Proxy name : ")

#Fucntion for List of each line
def process_line(line):
  global new_list
  data_into_list = line.split(" ")
  new_list = [item.replace('"', '') for item in data_into_list]
  for data in new_list:
   ipv6print(data)

#Destination IPV6 URLs
  for line in new_list:
    httpok = line.startswith("http://[")
    if httpok == True:
      ipv6url = str(re.findall(r'\[(.*?)\]', line)).replace("[", '').replace("'", '').replace("]", '')
      ipv6print(ipv6url)
    else:
      ipv6print(line)

#Function to print the IPV6 URLs/IPs
def ipv6print (data):
    try:
        ip = ipaddress.ip_address(data)
        ipt = (type(ip))
        newipt = str(ipt)
        ipv = (newipt.replace(">", '').replace("<", '').replace("'", '')).endswith("IPv6Address")
        if ipv == True:
          file_object = open(result, "a")
          file_object.write(str(ip) + "\n")
          file_object.close()
    except (ValueError,IOError) as err:
        pass

#File read
with open(logfile, encoding='latin1') as fobj:
  for line in fobj:
    process_line(line)

#Occurance of IPV6 addresses
subprocess.call('sort -n ' + result + '|  uniq -c | sort -r  >' + result+'.txt', shell=True)
subprocess.call('rm -rf ' + result, shell=True)



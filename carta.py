#!/usr/bin/env python3
import ipaddress
import regex
import copy

log_data_freq={}

subnets_group = {
    "108.162.0.0/16" : [],
    "212.129.32.128/25" : [],
    "173.245.56.0/23" : [],
}

def count_freq(fdata):
    for line in fdata:
        pattern = regex.search('.*(?= - -)',line)
        if pattern[0] in log_data_freq:
            log_data_freq[pattern[0]]+=1
        else:
            log_data_freq[pattern[0]] = 1

    return log_data_freq

def check_subnet():
    log_data_copy = copy.deepcopy(log_data_freq)
    for key in subnets_group.keys():
        subnet = ipaddress.ip_network(key)
        for k in log_data_copy.keys():
            ip = ipaddress.ip_address(k)
            if ip in subnet:
                subnets_group[key].append(k)
                del log_data_freq[k]

    return subnets_group

def read_data():
    fdata=[]
    with open("nginx.log") as data:
        fdata = data.readlines()

    return fdata

def main():
    data = read_data()
    with open('index.html', 'w') as f:
        f.write(f"<!DOCTYPE html>\n<html>\n<body>\n<p>\n<dl>\n")
        for key, value in count_freq(data).items():
            f.write(f"<dt>Address {key} was encountered {value} time(s).</dt>\n")
        f.write("</dt>\n</p>\n\n<p>\n<dt>\n")
        for k, v in check_subnet().items():
            f.write(f"<dt>Bucket {k} contains {len(v)} unique ip addresses.</dt>\n")
        f.write(f"</dl>\n</p>\n</body>\n</html>")

main()

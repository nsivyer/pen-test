import sys,os,nmap

nm = nmap.PortScanner()
#expecting ip addres in CIDR format:
#162.210.139.0/32
target = sys.argv[1]
tf = target.split("/")[0]
target_file = "/opt/nsivyer/pen-test/results/" + tf
f = open(target_file, 'w')

nm.scan(hosts=target, arguments='-n -sS -sU -PN --max-retries 1 --min-rate 300 --top-ports 5000')
print(nm.command_line())
for host in nm.all_hosts():
    for proto in nm[host].all_protocols():
        if (proto != "udp" and proto != "tcp"):
            continue
        lport = list(nm[host][proto].keys())
        lport.sort()
        for port in lport:
            f.write('%s,%s,%s,%s\n' % (host,proto,port,nm[host][proto][port]['state']))
f.close()

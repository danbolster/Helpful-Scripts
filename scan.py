import subprocess


portlist = [21,22,25,80,135,139,445,1443,3306,3389]

file = open("hosts.txt",'a')

def scan():
    for ip in range(1,256):
        check(ip)


def check(ip):
    for port in portlist:
        cmd = 'nc -nvv w 1 -z 10.1.1.' + str(ip) + ' ' + str(port)
        output = subprocess.check_output(cmd)
        if 'Connection' in output:
            file.write('10.1.1.' + str(ip))     
            print('found host!')
            return

def main():
    scan()
    file.close()

main()


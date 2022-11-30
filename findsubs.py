import requests 
import sys

# sub domains
list_file = open("list.txt","r")
subs = list_file.read()
list_file.close()

lista =list(subs.split("\n"))

args = sys.argv

def defualt_domains():
    if("-u" in args):
        base_url = args[args.index("-u") + 1]
    else:
        #usag
        pass


    for subdomain in lista:
        r = requests.get("http://"+str(subdomain)+"."+base_url)
        if(r.status_code == 200 ):
            print(subdomain + " exists on the site !!" + " , status_code = "+ str(r.status_code))
        else:
            print(subdomain + " does not exists on the site :) ")


defualt_domains()
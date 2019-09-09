#!/usr/bin/python

from zipfile import ZipFile
#import os

def get_user():
    finpass = open('/etc/passwd','r')
    fout = open('/root/tmp/pass.out.txt','w')

    shll = ["/bin/bash","/bin/false"]
    for ln in finpass:
        lst = ln.rsplit(":")
        if int(lst[2].rstrip("\n")) > 500 and lst[6].rstrip("\n") in shll:
          fout.writelines( ln )
    fout.close()
    finpass.close()

def get_group():
    finpass = open('/etc/passwd','r')
    fingrp = open('/etc/group','r')
    fgout = open('/root/tmp/group.out.txt','w')

    arrgrp = []

    for lnp in finpass:
        gr = lnp.rsplit(":")
        if int(gr[2]) > 500:
            arrgrp.append(gr[3])

    for lng in fingrp:
        lst = lng.rsplit(":")
        if lst[2].rstrip("\n") in arrgrp:
            fgout.writelines( lng )
    finpass.close()
    fingrp.close()
    fgout.close()

def get_shadow():
    finpass = open('/etc/passwd','r')
    finshw = open('/etc/shadow','r')
    fsout = open('/root/tmp/shadow.out.txt','w')
    shll = ["/bin/bash", "/bin/false"]

    arrusr = []

    for lnp in finpass:
        gr = lnp.rsplit(":")
        if int(gr[2]) > 500 and gr[6].rstrip("\n") in shll:
            arrusr.append(":" + gr[0] + ":")

    for lng in finshw:
        lst = lng.rsplit(":")
        if (":"+lst[0].rstrip("\n")+":") in arrusr:
            fsout.writelines(lng)

#    print(arrusr)
    finpass.close()
    finshw.close()
    fsout.close()

def main():
    get_user()
    get_group()
    get_shadow()

    file_paths = ['/root/tmp/pass.out.txt','/root/tmp/group.out.txt','/root/tmp/shadow.out.txt']

    # printing the list of all files to be zipped
    print('Following files will be zipped:')
    for file_name in file_paths:
        print(file_name)

    # writing files to a zipfile
    with ZipFile('user_data.zip', 'w') as zip:
        # writing each file one by one
        for file in file_paths:
            zip.write(file)

    print('All files zipped successfully!')

if __name__ == '__main__':main()

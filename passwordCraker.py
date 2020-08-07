#!/usr/bin/env python3


# passwordCracker.py
# Author: Nik alleyne
# Author Blog: www.securitynik.com
# Date: 2019-02-15

import crypt
from subprocess import call
from sys import exit, argv
from time import sleep

# This function handles usage information
def usage():
    print("password_file: A file consisting of passwords you would like to use.")
    print("./passwordCraker.py <password_file>")
    exit(0)


# This function checks to see if the username is found within the file
def passwordCracker(passwordFile):
    # Store the password we are trying to crack as a variable
    passwordToCrack = "$6$uPdhX/Zf$Kp.rcb4AWwtx0EJq235tzthWXdIEoJnhZjOHbil3od1AyMf3t8Yi6dAPlhbHVG9SLx5VSIPrXTZB8ywpoOJgi."
    print("[*] we will be looking for a match for password '{}'".format(passwordToCrack));
    print("[*] Starting password cracking ...")
    print("[*] Loading password file '{}' into memory ...".format(passwordFile))
    
    # Load the file entered on the command line into memory
    passwordFile = open(passwordFile, 'r')

    # Store salt as variable
    passwordSalt = "$6$uPdhX/Zf$"
    passwordFound = False;

    # Read the file line by line
    for line in passwordFile.readlines():
        sleep(2)
        passwordFound = crypt.crypt(line.strip(),salt=passwordSalt)
        if ( passwordFound == passwordToCrack.strip() ):
            print("[+] MATCH FOUND! Password is:{}".format(line).strip())
            print("[+] Password {} \n MATCHES \n Password {} ".format(passwordToCrack,passwordFound))
            exit(0)
        else:
            print("[-] Trying password:{}".format(line).strip())




if __name__ == '__main__':
    call("clear")
    print("passwordCrakcer.py")
    print("Author: Nik Alleyne")
    print("Author Blog: www.securitynik.com")

    # Check the number of arguments being entered on the command line
    if ( len(argv) != 2 ):
        usage()
        
    # calls the passwordCracker function
    passwordCracker(argv[1])
    

# Do not run this in in the same dir files are in!

import os
import subprocess
import sys
import time

the_output = subprocess.check_output('ls -1 /Users/chumlee/DestinationDir/ | wc -l', shell=True)
file_number = 20
if int(the_output) < file_number:
    print('DestinationDir is not mounted!!!')
    sys.exit()
else: 
    os.popen('sh /Users/chumlee/fooDir/cpfiles.sh')
    time.sleep(2)
    
the_output = subprocess.check_output('ls -1 /Users/chumlee/fooDir/dafoo/ | wc -l', shell=True)

i = 0

while int(the_output) > 0:
    print("File is not done being copied.")
    time.sleep(10)
    the_output = subprocess.check_output('ls -1 /Users/chumlee/fooDir/dafoo/ | wc -l', shell=True)
    i += 1
    if i > 39:
        break;
if i < 39:
    print("File is copied.")
else:
    print("File may still not be copied.")         

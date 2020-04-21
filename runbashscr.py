import os
import subprocess
import sys

the_output = subprocess.check_output('ls -1 /Users/chumlee/fooDir/ | wc -l', shell=True)
file_number = 20
if int(the_output) < file_number:
    print('fooDir is not mounted!!!')
    sys.exit()
    
os.popen('sh /Users/chumlee/tmpdownload/trybash.sh')

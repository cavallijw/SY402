from cgitb import text
import os
import hashlib
from unittest import skip

disablelist = []
readylist = []
textfile = open("filer.txt", "a+")

for root, dirs, files in os.walk("/"):
    for filename in files:
        result = os.path.join(root,filename)
        if "run" in result or "sys" in result or "tmp" in result or "proc" in result or "lib" in result:
            skip
        else:
            for i in files:
                result2 = os.path.join(root, i)
                try:
                    filey = open(result2,"rb")
                    result = hashlib.sha256(filename.encode())
                    hexform = result.hexdigest()
                    hexform = hexform + "\n"
                    readylist.append(hexform)
                except:
                    disablelist.append(hexform)
textfile.write(readylist)
textfile.write(disablelist)
textfile.close()
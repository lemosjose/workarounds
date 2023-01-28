import typing 
import sys 
# curl replacement for this workaround 
import os
import urllib.request 
#Not going to use os.fencode when calling sys.argv since this is not a *nix solution, but instead the replacement of a *nix tool for windows system
#future GUI for windows
#from PySide6 import QtCore, QtWidgets, QtGui
#error handling 
import re 

#make a pre-definition of the array
downloadLinks = []

def OpenFile(file):
    if not os.path.isfile(file) or not os.path.exists(file):
        print("the file is not a file or it does not exist at all")
        raise SystemExit()
    with open(file, "r") as f:
        for link in f.readlines():
            downloadLinks.append(link.rstrip())


def GetFileName(url: str):
    Filename = re.search('[^/]+$', url)
    return Filename.group(0)


def main() -> None:
    for TargetContent in downloadLinks:
        filename = GetFileName(str(TargetContent))
        file = urllib.request.urlopen(TargetContent) 
        fsFile = open(str(filename), 'xb')
        fsFile.write(file.read())
        fsFile.close()

if len(sys.argv) <= 1:
    print("no file passed")
    raise SystemExit()
    
Target = str(sys.argv[1])

sys.argv.remove(sys.argv[0])

for i in sys.argv:
    
    OpenFile(i)

main()
    
            






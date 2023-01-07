import typing 
import sys 
# curl replacement for this workaround 
import os
import re
import urllib.request 
#Not going to use os.fencode when calling sys.argv since this is not a *nix solution, but instead the replacement of a *nix tool for windows system


#error handling 

def OpenFile(file) -> list:
    if not os.path.isfile(file) or not os.path.exists(file):
        print("the file is not a file or it does not exist at all")
        raise SystemExit()
    with open(file) as f:
        content = f.readlines()
        return content 



def main(file) -> None:
    content = OpenFile(file)
    for TargetContent in content:
        file = urllib.request.urlopen(TargetContent) 
    #exception handling to take possible error in HTTP request for a URL provided in the file
            
        #if ():
         #   open(unquote()
        final_file = open(os.path.basename(TargetContent), 'xb')
        final_file.write(file.read())
        final_file.close()


Target = str(sys.argv[1])

main(Target)
    
            






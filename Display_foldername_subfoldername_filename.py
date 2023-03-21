##Take directory name from user as input & display foldername,subfoldername & file names
from sys import *
import os

def DirectoryWatcher(path):
    flag=os.path.isabs(path)        ##---> Check given path is absolute or not & this method not check path is present or not but it is checking path start from "/" or not

    if flag==False:                 #If path is not absolute then enter in if block
        path=os.path.abspath(path)      ##If path is not absolute then convert to absolute

    exists=os.path.isdir(path)          #Check whether specified path is in existing dir or not & isdir() method travel all path for searching files

    if exists:
        for foldername,subfoldername,filename in os.walk(path):     ##walk method is in module of os & os is platform specific module. os.walk() method take 3 variable name compulsory
            print("Current folder is:"+foldername)

            for subf in subfoldername:          ##Used to traverse subfolder
                print("Subfolder of"+foldername+"is:"+subf)

            for filen in filename:              ##Used to traverse files
                print("File inside"+foldername+"is:"+filen)

            print("")

    else:
        print("Inside path")

def main():
    print("Application name:"+argv[0])

    if(len(argv)!=2):
        print("Invalid number of arguments")
        exit()

    if(argv[1]=="--h") or (argv[1]=="--H"):
        print("This script is used to traverse directory")
        exit()

    if(argv[1]=="--u") or (argv[1]=="--U"):
        print("Usage ApplicationName Absolutepath_of_dir")
        exit()

    try:
        DirectoryWatcher(argv[1])

    except ValueError:
        print("Error:Invalid data type input")

    except Exception:
        print("Error:Invalid Input")

if __name__=="__main__":
    main()
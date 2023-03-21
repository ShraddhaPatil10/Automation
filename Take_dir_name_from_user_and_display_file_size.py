##Take directory name from user as input & display file size
from sys import *
import os

def DirectoryCalculateSize(path):
    flag=os.path.isabs(path)

    if flag==False:
        path=os.path.abspath(path)

    exists=os.path.isdir(path)

    if exists:
        for foldername,subfolder,filename in os.walk(path):
            print("Current folder is:"+foldername)

            for filen in filename:
                print("File Inside"+foldername+"is:"+filen,end=" ")

                print("With size:",os.path.getsize(os.path.join(foldername,filen)))
                ##os.path.getsize()---> It is used to get the size of file

            print(" ")

    else:
        print("Invalid Path")

def main():
    print("Application name:",argv[0])

    if(len(argv)!=2):
        print("Invalid number of arguments")
        exit()

    if(argv[1]=="--u") or (argv[1]=="--U"):
        print("Usage:ApplicationName AbsolutePath_of_dir")
        exit()

    if(argv[1]=="--h") or (argv[1]=="--H"):
        print("This script is used to traverse the directory")
        exit()

    try:
        DirectoryCalculateSize(argv[1])

    except ValueError:
        print("Error:Invalid datatype input")

    except Exception:
        print("Error:Invalid Input")

if __name__=="__main__":
    main()


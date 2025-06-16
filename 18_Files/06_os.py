import os
import shutil

a=os.listdir("dir") # get a list of directory and files within a directory
print(a)
print(os.getcwd()) # get current working directory
print(os.path.exists("dir")) # check whether a file exits or not if exit--> true else--> False
#os.remove("Sample.txt") # removes/delete a file not a directory
os.rmdir("dir")  # removes only empty directory cannot delete directory with files
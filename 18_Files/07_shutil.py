import shutil
#shutil.rmtree("dir")  # remove the complete directory with file as well 
#shutil.copy("John_Doe.txt","john.txt") # copy a file to another file if not created it will create it and if already there's anything it will overwrite it 
shutil.move("john.txt","dir/") # move the files to new directory 

# make a file manager 
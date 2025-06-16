# Append to an existing file called John Doe.txt 
# It should add data about John Doe Hometown



f=open("John_Doe.txt","a")

string='''
John Doe intially lived in Phoenix Arizona . He is a very nice guy
'''
f.write(string)
f.close()
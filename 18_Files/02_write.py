# write to a file called John Doe.txt 
# It should contain data about John Doe

# when writing it will overwrite the content 
f=open("John_Doe.txt","w")
string='''
John Doe is a nice guy .He live in Nyc and he works with Python
His favorite package is Pandas
'''
f.write(string)
f.close()
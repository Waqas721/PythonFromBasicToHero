#create a list containing the table of 5

# number=[]
# for i in range(1,11):
#     number.append(i)
# table=list(map(lambda x:x*5,number))
# print(table)


# a=5
# table=[]
# for i in range(1,11):
#     table.append(a*i)
# print(table)
# print(",".join(map(str, table)))

table=[5* i for i in range(1,11)]
print(table)
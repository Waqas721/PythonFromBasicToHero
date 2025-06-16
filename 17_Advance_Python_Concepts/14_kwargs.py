def marks(**kwargs):
    # Kwargs is a dictionary with all the key value pairs which were passed to marks
    for item in kwargs.keys():
        print(f"The marks of {item} is {kwargs[item]}")
'''       
If you want to pass a dictionary to marks, you must unpack it using **:
data = {"Shubham":34, "Vikrant":44, "Jack":34, "Marie":90}
marks(**data)
''' 

marks(Shubham=34, Vikrant=44, Jack=34, Marie=90)

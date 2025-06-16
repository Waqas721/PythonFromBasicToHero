s={34,23,1,3,22}
print(s)
s.add(32)
s.add(233)
#s.add(22) # only one time it will be shown 
s.remove(1) 
#s.remove(3444)  # if not present it will show an error
s.discard(3444)  # remove iff it's present in the set else do nothing
s.pop() # Removes random element
print(s)


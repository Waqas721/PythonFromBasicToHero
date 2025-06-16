# Two types of modules in python 
# - Build In Modules
# - External Modules
# List of all the build in modules : https://docs.python.org/3/py-modindex.html 

import math
import os 
import mymodules
import requests

print(math.sqrt(16))
print(mymodules.greet("Waqas"))
r=requests.get("https://www.google.com")
print(r.text)


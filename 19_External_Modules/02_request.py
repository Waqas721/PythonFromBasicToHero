# https://requests.readthedocs.io/en/latest/ for documentation

import requests 
r = requests.get('https://api.github.com/users/Waqas721')

with open("codewithwaqas.txt",'w') as f:
    f.write(r.text)
    
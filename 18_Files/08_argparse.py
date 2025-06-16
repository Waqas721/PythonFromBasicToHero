import argparse

parser=argparse.ArgumentParser(description="Simple calculalor")
parser.add_argument("num1",type=float,help="First number")
parser.add_argument("num2",type=float,help="Second number")
parser.add_argument("operation",choices=["add","sub","div","mul"],help="Operations to perform")

args=parser.parse_args()

#print(args)

if(args.operation=="add"):
    print(f"THe result is {args.num1+args.num2}")
    
elif(args.operation=="sub"):
    print(f"THe result is {args.num1-args.num2}")
    
elif(args.operation=="mul"):
    print(f"THe result is {args.num1*args.num2}")
    
elif(args.operation=="div"):
    print(f"THe result is {args.num1/args.num2}")
else:
    print("some error occured")
    
'''
in terminal:
python .\08_argparse.py 4 9 add
THe result is 13.0

'''
    
    
#example from notes
'''
import argparse

# Create the parser
parser = argparse.ArgumentParser(description="A simple command-line utility.")

# Add arguments
parser.add_argument("filename", help="The file to process.")
parser.add_argument("-n", "--number", type=int, default=1, help="Number of times to repeat the output.")

# Parse arguments
args = parser.parse_args()

# Try to open and read the file
try:
    with open(args.filename, "r") as file:
        content = file.read()
    
    # Print the content the specified number of times
    for _ in range(args.number):
        print(content)

except FileNotFoundError:
    print("File not found.")
'''
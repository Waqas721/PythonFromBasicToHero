try:
    file = open("waqas.txt", "r")
    for line in file: # Efficient for large files
           print(line.strip()) # Remove newline characters
    file.close()
except FileNotFoundError:
      print("File not found.")
   
# String formating

template="Dear {} You are awesome. Tak this {}$ bag"
a="John"
a1=10000
b="Jack"
b1=1000
c="Marie"
c1=300

s1=template.format(a,a1)
print(s1)

print(f"Dear {a} You are awesome. Tak this {a1} $ bag")
print("Dear %s, You are awesome. Take this %d $ bag" % (b, b1))


print(ord('A')) # Output: 65
print(chr(65)) # Output: 'A'

pi = 3.14159265
print(f"Pi rounded to 2 decimal places: {pi:.2f}")

text = "Python"
print(f"{text:>10}") # Right align
print(f"{text:<10}") # Left align
print(f"{text:^10}") # Center align
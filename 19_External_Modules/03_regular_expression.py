import re
text = "The quick brown fox jumps over the lazy dog."

# Search for a pattern
# match = re.search("brown", text)
# print(match)
# if match:
#     print("Match found!")
#     print("Start index:", match.start())
#     print("End index:", match.end())

# Find all occurrences of a pattern
# matches = re.findall("the", text, re.IGNORECASE) # Case-insensitive search
# print("Matches:", matches)

# Replace all occurrences of a pattern
# new_text = re.sub("fox", "cat", text)
# print("New text:", new_text)

# Compile a regex for efficiency (if used multiple times)
# https://regexr.com/
pattern = re.compile(r"\b\w+\b") # Matches whole words
words = pattern.findall(text)
print("Words:", words)
import re

txt = "jiafkjnmsdvbwfiosdncnsvfhebcowq"
pattern = r"[ ,.]"
x = re.sub(pattern, ":", txt)
print(x)
import re

txt = "pqrsabcdefghuvwxyztuvwxyz"
x = re.split(r'[A-Z]',txt)
print(x)
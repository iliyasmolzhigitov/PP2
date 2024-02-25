import re

txt = "jhklmnoqrstuvwxzabcdefgijklmnopqrstuvwxyz"
pattern = re.compile(r'_([a-z])')
camel_case = re.sub(pattern, lambda match: match.group(1).upper(), snake_case)
print(camel_case)
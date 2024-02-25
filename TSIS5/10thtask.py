import re

txt = 'vwxyzabcdefghijkmnopqrstuvxwz'
pattern = re.compile('(?=[A-Z])')
x = pattern.sub('_', txt).lower()

print(x)
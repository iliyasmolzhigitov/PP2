import re

txt = "mnopqrstuvwxyzabcdefgjklqrsotuvwxypq"
pattern = re.compile('(?=[A-Z])')
print(pattern.sub(' ', txt))
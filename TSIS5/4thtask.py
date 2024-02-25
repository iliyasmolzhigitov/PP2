import re

txt = "HelloWorldIAmHere"
print(re.findall("[A-Z]{1}[a-z]+", txt))
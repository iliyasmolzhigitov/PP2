import re

txt = "abcdefgab"
print(re.search(r'a.*b$', txt))
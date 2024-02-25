import re

txt = "abcDEFGhijkLMNoPQRstuvwxyz"
print(re.search("a{1}b{2,3}",txt))
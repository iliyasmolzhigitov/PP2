import re

txt = "abc_def_ghi_jkl_mno"
print(re.findall("[a-z]+_[a-z]+", txt))
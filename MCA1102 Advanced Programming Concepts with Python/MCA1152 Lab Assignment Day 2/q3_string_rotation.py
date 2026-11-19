# 3. Check whether a string is a rotation of another string. 
# Sample   
# Input: "abcd", "cdab" 
# Output: True 
# Input: "abcd", "cdba" 
# Output: False

s1 = "abcd"
s2 = "cdab"

merged = s1 + s2

is_rotation = s2 in merged

print(is_rotation)